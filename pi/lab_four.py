#!/usr/bin/env python

import batmobile as L01
import time
import random
import math
import particleDataStructures as world


# current estimate of L01's position
estimate_theta = 0.0
estimate_x = 84.0
estimate_y = 30.0


# initialise particles
NUMBER_OF_PARTICLES = 100
p_x = [estimate_x] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [estimate_y] * NUMBER_OF_PARTICLES
p_theta = [estimate_theta] * NUMBER_OF_PARTICLES
weights = [1.0/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated

mu = 0 # update with actual value
# sigma values for 20cm dist and pi/2 rotations
sigma_e = 0.1
sigma_f = 0.04519
sigma_g = 0.03490


# from particle Data Structures
mymap = world.Map()
particles = world.Particles() # for printing
for i in range(100):
    particles.data.append((estimate_x,estimate_y, estimate_theta, weights[0]))

world.init_world(mymap)


# estimate L01 position based on particles
def update_estimate():
    global p_x
    global p_y
    global p_theta
    global weights
    estimate_x = 0.0
    estimate_y = 0.0
    estimate_theta = 0.0
    for i in range(NUMBER_OF_PARTICLES):
        estimate_x += p_x[i]*weights[i]
        estimate_y += p_y[i]*weights[i]
        estimate_theta += p_theta[i]*weights[i]


# normalise weights
def normalise():
    global weights
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

def updatePos():
    global p_x
    global p_y
    global p_theta
    global weights
    global estimate_x
    global estimate_y
    global estimate_theta
    estimate_x = 0.0
    estimate_y = 0.0
    estimate_theta = 0.0

    for i in range(100):
        estimate_x += p_x[i]*weights[i]
        estimate_y += p_y[i]*weights[i]
        estimate_theta += p_theta[i]*weights[i]




def calculate_likelihood(x, y, theta, z): #current state of particle (x,y,0) plus sonar reading z
    # adjust for systematic sonar error
    if z >45:
        z = 0.99*z

    # sonar is placed 9cm infront of centre of rotation
    adj_z = z + 9

    print adj_z

    #variables used to catch divide by zeros
    c = math.cos(theta)
    s = math.sin(theta)
    if c==0:
        c+=0.00000001
    if s==0:
        s+=0.00000001
        

    # calc current particles distance to each wall's infinite line form
    ma =((168 -   0)*(  0 - x) - (  0 -   0)*(  0 - y))/((168 -   0)*c - (  0 -   0)*s)
    mb =((168 - 168)*(  0 - x) - ( 84 -   0)*(168 - y))/((168 - 168)*c - ( 84 -   0)*s)
    mc =((210 - 126)*( 84 - x) - ( 84 -  84)*(126 - y))/((210 - 126)*c - ( 84 -  84)*s)
    md =((210 - 210)*( 84 - x) - (168 -  84)*(210 - y))/((210 - 210)*c - (168 -  84)*s)
    me =(( 84 - 210)*(168 - x) - (168 - 168)*(210 - y))/(( 84 - 210)*c - (168 - 168)*s)
    mf =(( 84 -  84)*(168 - x) - (210 - 168)*( 84 - y))/(( 84 -  84)*c - (210 - 168)*s)
    mg =((  0 -  84)*(210 - x) - (210 - 210)*( 84 - y))/((  0 -  84)*c - (210 - 210)*s)
    mh =((  0 -   0)*(210 - x) - (  0 - 210)*(  0 - y))/((  0 -   0)*c - (  0 - 210)*s)

    # find most suitbale m
    walls = mymap.walls
    smallest_m = 999999
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
    sd = 2
    gauss = math.e**(-0.5*(float(adj_z-mean)/sd)**2)
    K = 0.0 # get actual constant for robustnus
    likelihood = gauss + K
    return likelihood


# call after checking for a valid sonar reading
def update_particles(z):
    global p_x
    global p_y
    global p_theta
    global weights
    for i in range(100):
        # update weights
        weights[i] *= calculate_likelihood(p_x[i], p_y[i], p_theta[i], z)


# getting a sonar reading
def read_sonar():
    usReadings = []
    for i in range(11):
        usReadings.append(L01.interface.getSensorValue(L01.us_port))
        time.sleep(0.0045)
    usReadings.sort()
    if usReadings[5] :
        print "I measured a distance of "+ str(usReadings[5])
        return usReadings[5][0]
    else:
        print "Failed US reading"
        return read_sonar()

# TODO: 3.3
def navigateToWaypoint(X, Y):  # X,Y are cords of dest
    global estimate_x
    global estimate_y
    global estimate_theta
    global p_x
    global p_y
    global p_theta
    global mu
    global sigma_e
    global sigma_f
    global sigma_g


    #print "Silly test " + str(estimate_x) +" "+ str(estimate_y) +" "+str(estimate_theta)
    x_diff = X-estimate_x
    y_diff = Y-estimate_y
    dist = (x_diff**2 + y_diff**2)**0.5
    angleDest = math.atan2(y_diff,x_diff) # returns an angle between - pi  and pi
    angleRotate = angleDest - estimate_theta
    L01.left_90(angleRotate/1.5708)
    time.sleep(2.5)

    e = sigma_e * math.sqrt(dist/10)
    f = sigma_f * math.sqrt(dist/10)
    g = sigma_g * math.sqrt(dist/10)
    
    #update all the particles angle
    for k in range (100):
        error_g = random.gauss(mu,g)
        p_theta[k] += angleRotate + error_g
        
        
    L01.forward(dist)
    time.sleep(dist*0.08)
    for k in range(100):          #this code is only relevant for correction once a move has been logged
        error_e = random.gauss(mu,e)
        error_f = random.gauss(mu,f)
        p_x[k] += (dist + error_e) * math.cos(angleDest)
        p_y[k] += (dist + error_e) * math.sin(angleDest)
        p_theta[k] += error_f

waypoints = [(180,30),(180,54),(138,54),(138,168),(114,168),(114,84),(84,84),(84,30)]


for x,y in waypoints:
    print "What am I doing?: Navigate to waypoint"
    navigateToWaypoint(x,y)
    print "What am I doing?: Read Sonar"
    reading = read_sonar()
    print "What am I doing?: Update particles"
    update_particles(reading)
    print "What am I doing?: Normalize"
    normalise()
    print weights
    print str(sum(weights))
    print "What am I doing?: Resample"
    resample()
    print "What am I doing?: Update"
    updatePos()
    print "What am I doing?: Print"
    particles.data =[]
    for k in range(100):
        particles.data.append((p_x[k], p_y[k], p_theta[k]))
    particles.draw()

L01.interface.terminate()
