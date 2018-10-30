import brickpi
import time
import batmobile

interface=brickpi.Interface()


#print "I got here at least"

motor_base_speed = 6.0 #maybe update
motor_left_speed = motor_base_speed
motor_right_speed =motor_base_speed

desired_distance = 30

while True:
	#print"I got here too"
	#move
	batmobile.keepRolling(motor_right_speed,motor_left_speed) # Making assumption on which is which
	
	#calculate where I am
	
	usReading = interface.getSensorValue(3)
	#print usReading
	#print usReading[0]
	distance_error =0
	if usReading:
		measured_distance =float( usReading[0])
	
		distance_error = measured_distance - desired_distance
	else:
		print"No reading"
	#calculate how to move now
	
	motor_left_speed = motor_base_speed + 0.5*distance_error
	motor_right_speed = motor_base_speed - 0.5*distance_error
	
	print motor_left_speed,  ", " , motor_right_speed
	
	time.sleep (0.1)
	
	
	
	
	
	
