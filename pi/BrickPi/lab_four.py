import batmobile as L01
import time
import random
import math
import particleDataStructures as world

NUMBER_OF_PARTICLES = 100
p_x = [0.0] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [0.0] * NUMBER_OF_PARTICLES
p_theta = [0.0] * NUMBER_OF_PARTICLES
weights = [1.0/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated


mu = 0 # update with actual value
sigma_e = 0.037
sigma_f = 0.037
sigma_g = 0.021

estimate_theta = 0.0
estimate_x = 0.0
estimate_y = 0.0

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

    # print "Silly test " + str(estimate_x) +" "+ str(estimate_y) +" "+str(estimate_theta)
    x_diff = X-estimate_x
    y_diff = Y-estimate_y
    dist = (x_diff**2 + y_diff**2)**0.5
    angleDest = math.atan2(y_diff,x_diff) # returns an angle between - pi  and pi

    angleRotate = angleDest - estimate_theta

    L01.left_90(angleRotate/1.5708)
    time.sleep(2.5)
    #particles_rot = []
    for k in range (100):
        error_g = random.gauss(mu,sigma_g)
        p_theta[k] += angleRotate + error_g
    #   particles_rot.append((5*p_x[k], 5*p_y[k], p_theta[k]))
    #print "drawParticles:" + str(particles_rot)  # should print out the drawParticles

    L01.forward(dist)
    time.sleep(dist*0.2)
    #particles = []
    for k in range(100):          #this code is only relevant for correction once a move has been logged
        error_e = random.gauss(mu,sigma_e)
        error_f = random.gauss(mu,sigma_f)
        p_x[k] += (dist + error_e) * math.cos(angleDest)
        p_y[k] += (dist + error_e) * math.sin(angleDest)
        p_theta[k] += error_f
    #    particles.append((5*p_x[k], 5*p_y[k], p_theta[k]))
    #print "drawParticles:" + str(particles)  # should print out the drawParticles

    # now to update current guess of position
    estimate_x = 0.0
    estimate_y = 0.0
    estimate_theta = 0.0
    for i in range(100):
        estimate_x += p_x[i]*weights[i]
        estimate_y += p_y[i]*weights[i]
        estimate_theta += p_theta[i]*weights[i]
    #print "Silly test 2 " + str(estimate_x) +" "+ str(estimate_y) +" "+str(estimate_theta)



#this is the function we need 3.1 of week 5 practical
def calculate_likelihood(x, y, theta, z): #current state of particle (x,y,0) plus sonar reading z
    #adding positional offset to z
    sonar_reading = z + 9  # guestimate placeholder. change to actual value

    #General Formula: m = ((By − Ay )*(Ax − x) − (Bx − Ax )*(Ay − y))/((By − Ay )*math.cos(theta) − (Bx − Ax )*math.sin(theta))
    ma =((168 −   0)*(  0 − x) − (  0 −   0)*(  0 − y))/((168 −   0)*math.cos(theta) − (  0 −   0)*math.sin(theta))
    mb =((168 − 168)*(  0 − x) − ( 84 −   0)*(168 − y))/((168 − 168)*math.cos(theta) − ( 84 −   0)*math.sin(theta))
    mc =((210 − 126)*( 84 − x) − ( 84 −  84)*(126 − y))/((210 − 126)*math.cos(theta) − ( 84 −  84)*math.sin(theta))
    md =((210 − 210)*( 84 − x) − (168 −  84)*(210 − y))/((210 − 210)*math.cos(theta) − (168 −  84)*math.sin(theta))
    me =(( 84 − 210)*(168 − x) − (168 − 168)*(210 − y))/(( 84 − 210)*math.cos(theta) − (168 − 168)*math.sin(theta))
    mf =(( 84 −  84)*(168 − x) − (210 − 168)*( 84 − y))/(( 84 −  84)*math.cos(theta) − (210 − 168)*math.sin(theta))
    mg =((  0 −  84)*(210 − x) − (210 − 210)*( 84 − y))/((  0 −  84)*math.cos(theta) − (210 − 210)*math.sin(theta))
    mh =((  0 −   0)*(210 − x) − (  0 − 210)*(  0 − y))/((  0 −   0)*math.cos(theta) − (  0 − 210)*math.sin(theta))

    predicted_m = [ma,mb,mc,md,me,mf,mg,mh]
    # find smallest m - and make sure it is feasible
    for m in predicted_m:
        
    # get likelihood