import batmobile as bat
import time


bat.interface.sensorEnable(bat.us_port, bat.brickpi.SensorType.SENSOR_ULTRASONIC)

distance = 30
base = 9
p=0.15

while True:
	# returns tuple 
	usReading = bat.interface.getSensorValue(bat.us_port)

	error = p*(distance - usReading[0])

	speedL = base - 0.5*error
	speedR = base + 0.5*error

	bat.keepRolling(speedR,speedL)

	if usReading :
		print usReading
	else:
		print "Failed US reading"

	time.sleep(0.05)

bat.interface.terminate()





# #print "I got here at least"

# motor_base_speed = 6.0 #maybe update
# motor_left_speed = motor_base_speed
# motor_right_speed =motor_base_speed

# desired_distance = 30
# batmobile.keepRolling(motor_right_speed,motor_left_speed) # Making assumption on which is which

# while True:
# 	#print"I got here too"
# 	#move
	
# 	#calculate where I am
	
# 	usReading = batmobile.interface.getSensorValue(3)
# 	#print usReading
# 	#print usReading[0]
# 	distance_error =0

# 	if usReading:
# 		measured_distance =float( usReading[0])
	
# 		distance_error = measured_distance - desired_distance
# 	else:
# 		print"No reading"
# 	#calculate how to move now
	
# 	motor_left_speed = motor_base_speed + 0.5*distance_error
# 	motor_right_speed = motor_base_speed - 0.5*distance_error
	
# 	print motor_left_speed,  ", " , motor_right_speed
	
# 	time.sleep (0.05)
	
# 	batmobile.keepRolling(motor_right_speed,motor_left_speed) # Making assumption on which is which

	
	
	
	
