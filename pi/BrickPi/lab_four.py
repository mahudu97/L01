#!/usr/bin/env python

import batmobile as L01
import time
import random
import math
import particleDataStructures as world

# initialise particles
NUMBER_OF_PARTICLES = 100
p_x = [0.0] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [0.0] * NUMBER_OF_PARTICLES
p_theta = [0.0] * NUMBER_OF_PARTICLES
weights = [1.0/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated

mu = 0 # update with actual value
# sigma values for 20cm dist and pi/2 rotations
    #TODO: assumes linear sclaing
sigma_e = 0.2 #0.1
sigma_f = 0.09038 #0.04519
sigma_g = 0.0698 #0.03490

# current estimate of L01's position
estimate_theta = 0.0
estimate_x = 0.0
estimate_y = 0.0

# from particle Data Structures
mymap = world.Map()
particles = world.Particles() # for printing
world.init_world(mymap)


# estimate L01 position based on particles
def update_estimate():
    estimate_x = 0.0
    estimate_y = 0.0
    estimate_theta = 0.0
    for i in range(NUMBER_OF_PARTICLES):
        estimate_x += p_x[i]*weights[i]
        estimate_y += p_y[i]*weights[i]
        estimate_theta += p_theta[i]*weights[i]


# normalise weights
def normalise():
    total = sum(weights)
    for i in range(NUMBER_OF_PARTICLES):
        weights[i] /= total


#
def resample():
    global p_x
    global p_y
    global p_theta
    global weights

    # build array with cumulative weights
    cumulative_weights = [0] * NUMBER_OF_PARTICLES
    cumulative_weights[0] = weights[0]
    for i in range(1, NUMBER_OF_PARTICLES):
        cumulative_weights[i] = cumulative_weights[i-1] \
                                    + weights[i]

    # tmp particle arrays
    p_x_tmp = [0.0] * NUMBER_OF_PARTICLES
    p_y_tmp = [0.0] * NUMBER_OF_PARTICLES
    p_theta_tmp = [0.0] * NUMBER_OF_PARTICLES

    for i in range(NUMBER_OF_PARTICLES):
        rand = random.uniform(0.0,1.0)
        for j in range(NUMBER_OF_PARTICLES):
            if cumulative_weights[j] - rand >= 0:
                # add new particle
                p_x_tmp[i]     = p_x[j]
                p_y_tmp[i]     = p_y[j]
                p_theta_tmp[i] = p_theta[j]
                break

    # overrite final arrays
    p_x     = p_x_tmp
    p_y     = p_y_tmp
    p_theta = p_theta_tmp

    # set weights to 1/N
    weights = [1.0/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES





def calculate_likelihood(x, y, theta, z): #current state of particle (x,y,0) plus sonar reading z
    # adjust for systematic sonar error
    if z >45:
        z = 0.99*z

    # sonar is placed 9cm infront of centre of rotation
    adj_z = z + 9

    # calc current particles distance to each wall's infinite line form
    ma =((168 -   0)*(  0 - x) - (  0 -   0)*(  0 - y))/((168 -   0)*math.cos(theta) - (  0 -   0)*math.sin(theta))
    mb =((168 - 168)*(  0 - x) - ( 84 -   0)*(168 - y))/((168 - 168)*math.cos(theta) - ( 84 -   0)*math.sin(theta))
    mc =((210 - 126)*( 84 - x) - ( 84 -  84)*(126 - y))/((210 - 126)*math.cos(theta) - ( 84 -  84)*math.sin(theta))
    md =((210 - 210)*( 84 - x) - (168 -  84)*(210 - y))/((210 - 210)*math.cos(theta) - (168 -  84)*math.sin(theta))
    me =(( 84 - 210)*(168 - x) - (168 - 168)*(210 - y))/(( 84 - 210)*math.cos(theta) - (168 - 168)*math.sin(theta))
    mf =(( 84 -  84)*(168 - x) - (210 - 168)*( 84 - y))/(( 84 -  84)*math.cos(theta) - (210 - 168)*math.sin(theta))
    mg =((  0 -  84)*(210 - x) - (210 - 210)*( 84 - y))/((  0 -  84)*math.cos(theta) - (210 - 210)*math.sin(theta))
    mh =((  0 -   0)*(210 - x) - (  0 - 210)*(  0 - y))/((  0 -   0)*math.cos(theta) - (  0 - 210)*math.sin(theta))

    # find most suitbale m
    walls = mymap.walls
    smallest_m = ma
    sm_index = 10
    predicted_m = [ma,mb,mc,md,me,mf,mg,mh]
    # find smallest m - and make sure it is feasible
    for index in range (len( predicted_m)):
        # postive m, smaller than current smallest
        if predicted_m[index]>0 and predicted_m[index] <=smallest_m:
            m_x = x+predicted_m[index]*math.cos(theta)
            m_y = y+predicted_m[index]*math.sin(theta)
            # current wall's info
            lineX = [ walls[index][0], walls[index][2]]
            lineY = [ walls[index][1], walls[index][3]]

            # deal with cases where 2nd entry less than first
            lineX.sort()
            lineY.sort()

            # is m feasible (intersects actuall wall, not just the inf line)
            if m_x >= lineX[0]  and m_x <= lineX[1] \
                and m_y >= lineY[0]  and m_y <= lineY[1]:
                smallest_m = predicted_m[index]
                sm_index = index

    # didn't find a feasible m
    if sm_index == 10:
        return 0

    # calculate likelihood
    mean = smallest_m
    #sd of sonar
    # at 100cm - s.d. = 0.2cm
    # TODO: ASK GTA ABOUT SCALING
    sd_100 = 0.2
    sd = (smallest_m / 100) * sd_100
    gauss = math.e**(-0.5*(float(adj_z-mean)/sd)**2)
    K = 0.0 # get actual constant for robustnus
    likelihood = gauss + K
    return likelihood


# call after checking for a valid sonar reading
def update_particles(z):
    for p in particles.data:
        # update weights
        p[3] *= calculate_likelihood(p[0], p[1], p[2], z)


# getting a sonar reading
def read_sonar():
    usReadings = []
    for i in range(11):
        usReadings.append(L01.interface.getSensorValue(L01.us_port))
        time.sleep(0.0045)
    usReadings.sort()
    if usReadings[5] :
        return usReadings[5][0]
    else:
        print "Failed US reading"
        return read_sonar()

# TODO: 3.3
def navigateToWaypoint( X, Y):
    global estimate_x
    global estimate_y
    global estimate_theta
    global p_x
    global p_y
    global p_theta
    global weights
    global mu
    global sigma_e
    global sigma_f
    global sigma_g

    x_diff = X-estimate_x
    y_diff = Y-estimate_y
    dist = (x_diff**2 + y_diff**2)**0.5
    angleDest = math.atan2(y_diff,x_diff) # returns an angle between - pi  and pi

    angleRotate = angleDest - estimate_theta

    L01.left_90(angleRotate/1.5708)
    time.sleep(2.5)
    for k in range (NUMBER_OF_PARTICLES):
        error_g = random.gauss(mu,sigma_g)
        p_theta[k] += angleRotate + error_g
    #   particles_rot.append((5*p_x[k], 5*p_y[k], p_theta[k]))
    #print "drawParticles:" + str(particles_rot)  # should print out the drawParticles

    L01.forward(dist)
    time.sleep(dist*0.2)
    #particles = []
    for k in range(NUMBER_OF_PARTICLES):          #this code is only relevant for correction once a move has been logged
        error_e = random.gauss(mu,sigma_e)
        error_f = random.gauss(mu,sigma_f)
        p_x[k] += (dist + error_e) * math.cos(angleDest)
        p_y[k] += (dist + error_e) * math.sin(angleDest)
        p_theta[k] += error_f
    #    particles.append((5*p_x[k], 5*p_y[k], p_theta[k]))
    #print "drawParticles:" + str(particles)  # should print out the drawParticles


L01.interface.terminate()