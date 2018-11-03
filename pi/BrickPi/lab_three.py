import batmobile
import time
import random
import math

L01 = batmobile
NUMBER_OF_PARTICLES = 100
p_x = [0] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [0] * NUMBER_OF_PARTICLES
p_theta = [0] * NUMBER_OF_PARTICLES
weights = [1/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated


#the errors, need to be generated each time called
#TODO: make these correct
error_e = 0
error_f = 0
error_g = 0
mu = 0 # update with actual value
sigma_e = 0
sigma_f = 0
sigma_g = 0
#different sigmas
#random.gauss(mu, sigma) generates random number smapled from mean mu and SD sigma


#updates arrays accordingly now
#still confused about why this generates 100 points
for i in range(0, 3):
    for j in range(0, 3):
        L01.forward(10)
        time.sleep(3.5)
        particles = []
        for k in range(0, 99):
            error_e = random.gauss(mu,sigma_e)
            error_f = random.gauss(mu,sigma_f)
            p_x[k] += (10 + error_e) * math.cos(p_theta[k])
            p_y[k] += (10 + error_e) * math.sin(p_theta[k])
            p_theta[k] += error_f
            particles.append((p_x[k], p_y[k], p_theta[k]))
        print "drawParticles:" + str(particles)  # should print out the drawParticles
    L01.left_90(1)                                         # did it in same way as testDraw
    time.sleep(2)

    particles_angle = []
    for l in range (0,99):
        error_g = random.gauss(mu,sigma_g)
        p_theta[l] += 90 + error_g
        particles_angle.append((p_x[l], p_y[l], p_theta[l]))
        
    print "drawParticles:" + str(particles_angle)

print "Square complete!"
