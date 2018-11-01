import batmobile
import time
import random
import math

L01 = batmobile
NUMBER_OF_PARTICLES = 100
p_x = [0] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [0] * NUMBER_OF_PARTICLES
p_theta = [0] * NUMBER_OF_PARTICLES
weight = [1/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated


#the errors, need to be generated each time called
#TODO: make these correct
error_e = 0
error_f = 0
error_g = 0
mu = 0 # update with actual value
sigma =0
#random.gauss(mu, sigma) generates random number smapled from mean mu and SD sigma


#updates arrays accordingly now
#still confused about why this generates 100 points
for i in range(0. 3):
    for j in range(0, 3):
        L01.forward(10)
        time.sleep(3.5)
        for k in range(0, 99):
            error_e = random.gauss(mu,sigma)
            error_f = random.gauss(mu,sigma)
            p_x[k] += (10 + error_e) * math.cos(theta)
            p_y[k] += (10 + error_e) * math.sin(theta)
            p_theta[k] += error_f
        print "drawParticles:" + str([p_x, p_y, p_theta])
    L01.left_90(1)
    time.sleep(2)

    for l in range (0,99):
        error_g = random.gauss(mu,sigma)
        p_theta[k] += 90 + error_g
    print "drawParticles:" + str([p_x, p_y, p_theta])

print "Square complete!"
