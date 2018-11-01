import batmobile
import time
import random
import math

def average(w, array_in[]): #weighted average calculator
    avg = 0
    for a in range(0, 99):
        avg += w * array_in[a]
    return avg

def navigateToWaypoint(float X, float Y):
        #needs to do a turn then a move of correct distance

L01 = batmobile
NUMBER_OF_PARTICLES = 100
p_x = [0] * NUMBER_OF_PARTICLES # At the start every particle has its intial coords as 0,0,0
p_y = [0] * NUMBER_OF_PARTICLES
p_theta = [0] * NUMBER_OF_PARTICLES
weight = [1/NUMBER_OF_PARTICLES] * NUMBER_OF_PARTICLES # In an actual example these would be updated

error_e = 0 #the errors, need to be generated each time called
error_f = 0 #TODO: make these correct
error_g = 0
mu = 0 # update with actual value
sigma_e = 0 #different sigmas
sigma_f = 0 #random.gauss(mu, sigma) generates random number smapled from mean mu and SD sigma
sigma_g = 0

def main():
    turn_angle = 0
    distance = 0
    current_x = 0
    current_y = 0
    while True: #enter input co-ords, rotate, move, REPEAT
        w_x = raw_input("Enter X value of the waypoint: ")
        w_y = raw_input("Enter Y value of the waypoint: ")
        #the maths needs to go here

        for l in range (0,99):
            error_g = random.gauss(mu,sigma_g)
            p_theta[k] += 90 + error_g
        for k in range(0, 99):          #this code is only relevant for correction once a move has been logged
            error_e = random.gauss(mu,sigma_e)
            error_f = random.gauss(mu,sigma_f)
            p_x[k] += (10 + error_e) * math.cos(p_theta[k])
            p_y[k] += (10 + error_e) * math.sin(p_theta[k])
            p_theta[k] += error_f


X = average(weight[0], p_x) #currently the weights are all the same so can just say the first weight value
Y = average(weight[0], p_y)
navigateToWaypoint(X, Y)
