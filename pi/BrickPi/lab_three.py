import batmobile
import time
import random
import math
import numpy as np

# def lab_three():
L01 = batmobile
NUMBER_OF_PARTICLES = 100
p_x = [100] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [100] * NUMBER_OF_PARTICLES
p_theta = [0] * NUMBER_OF_PARTICLES
weights = [1/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated


#the errors, need to be generated each time called
#TODO: make these correct
mu = 0 # update with actual value
sigma_e = 0.1
sigma_f = 0.04519
sigma_g = 0.03490
#different sigmas
#random.gauss(mu, sigma) generates random number smapled from mean mu and SD sigma

lines=[]
lines.append((500,500,700,500))
lines.append((700,500,700,300))
lines.append((700,300,500,300))
lines.append((500,300,500,500))  # tuples for the ref lines

for l in lines:
    print "drawLine:" +str(l)


#updates arrays accordingly now
#still confused about why this generates 100 points
for i in range(4):
    for j in range(4):
        L01.forward(10)
        time.sleep(2)
        particles = []
        for k in range(100):
            error_e = random.gauss(mu,sigma_e)
            error_f = random.gauss(mu,sigma_f)
            p_x[k] += (10 + error_e) * math.cos(p_theta[k])
            p_y[k] += (10 + error_e) * math.sin(p_theta[k])
            p_theta[k] += error_f           
            particles.append((5*p_x[k], 5*p_y[k], p_theta[k]))
        print "drawParticles:" + str(particles)  # should print out the drawParticles
        
    L01.left_90(1)                                         # did it in same way as testDraw
    time.sleep(2)

    particles_angle = []
    for l in range (100):
        error_g = random.gauss(mu,sigma_g)
        p_theta[l] -= 1.5708 + error_g
        particles_angle.append((5*p_x[l], 5*p_y[l], p_theta[l]))
        
    print "drawParticles:" + str(particles_angle)

#minx = 10000
#maxx = -1
#miny = 10000
#maxy = -1
#for x in p_x:
#    for y in p_y:
#        if x**2 + y**2 < minx**2 + miny**2:
#            minx = x
#            miny = y
#        if x**2 + y**2 > maxx**2 + maxy**2:
#            maxy = y
#            maxx = x
#            
#diam = (maxx-minx)**2 + (maxy-miny)**2
#radius = diam**0.5 / 2
#print "radius of spread = " + str(radius)

# d = []
# for i in range(100):
#     dist_i = (p_x[i]**2 + p_y[i]**2)**0.5
#     d = np.append(d, dist_i)

# return np.std(d)


print "Square complete!"
