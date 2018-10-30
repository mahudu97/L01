import brickpi
import time
import sys
import batmobile

interface=brickpi.Interface()
interface.initialize()
motors = [0,3]
touch_port = [0,1]
us_port = 3
interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(uv_port, brickpi.SensorType.SENSOR_ULTRASONIC);

# angle = float(input("Enter an angle (rad): "))
# #Move 20cm Back
# angle_reverse = 5.897
# angle_turn = radTurn*1.5

#interface.increaseMotorAngleReferences(motors,[angle,angle])


motor_base_speed =6
motor_left_speed = motor_base_speed
motor_right_speed =motor_base_speed

desired_distance = 30

while true:

	#move
	interface.setMotorRotationSpeedReferences(motors,[motor_left_speed,motor_right_speed]) # Making assumption on which is which
	
	#calculate where I am
	
	usReading = interface.getSensorValue(us_port)
	measured_distance = usReading[0]
	
	distance_error = measured_distance-desired_distance
	
	#calculate how to move now
	
	motor_left_speed = motor_base_speed - 0.5*distance_error
	motor right_speed = motor_base_speed + 0.5*distance_error
	
	
	
	
	
	
	
	