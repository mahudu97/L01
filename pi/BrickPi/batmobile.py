import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

###########################SETTERS######################################
maxACC = 8.0
maxVEL = 12.0

kp_left = 400
ki_left = 1000
kd_left = 35
PWM_left= 18.0

kp_right = kp_left
ki_right = ki_left
kd_right = kd_left
PWM_right= 18.0

radTurn = 3.505
radMove = 0.29398398748182

#SETTING SENSOR PARAMS
touch_port = [1,2]
# touch_port = [left,right]
interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)

us_port = 3
interface.sensorEnable(us_port, brickpi.SensorType.SENSOR_ULTRASONIC)

# SETTING MOTOR PARAMS
motors = [0,3]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams_left = interface.MotorAngleControllerParameters()
motorParams_left.maxRotationAcceleration = maxACC
motorParams_left.maxRotationSpeed = maxVEL
motorParams_left.feedForwardGain = 255/10.0
motorParams_left.minPWM = PWM_left
motorParams_left.pidParameters.minOutput = -255
motorParams_left.pidParameters.maxOutput = 255
motorParams_left.pidParameters.k_p = kp_left
motorParams_left.pidParameters.k_i = ki_left
motorParams_left.pidParameters.k_d = kd_left

motorParams_right = interface.MotorAngleControllerParameters()
motorParams_right.maxRotationAcceleration = maxACC
motorParams_right.maxRotationSpeed = maxVEL
motorParams_right.feedForwardGain =255/20.0
motorParams_right.minPWM = PWM_right
motorParams_right.pidParameters.minOutput = -255
motorParams_right.pidParameters.maxOutput = 255
motorParams_right.pidParameters.k_p = kp_right
motorParams_right.pidParameters.k_i = ki_right
motorParams_right.pidParameters.k_d = kd_right

# PUSHING PARAMS TO MOTOR CONTROLLER
interface.setMotorAngleControllerParameters(motors[0],motorParams_right)
interface.setMotorAngleControllerParameters(motors[1],motorParams_left)
#####################################################################################

# MOVEMENT FUNCTIONS

def forward( dist ):
    #convert dist in cm to revolutions of the wheels in rad
	angle = radMove*dist
	print("Moving forward by ", dist, "cm")
	interface.increaseMotorAngleReferences(motors,[angle,angle])
	return True

def backward (dist):
    #convert dist in cm to revolutions of the wheels in rad
	angle = radMove*dist
	print ("Moving backward by ", dist, "cm")
	interface.increaseMotorAngleReferences(motors,[-angle,-angle])
	return True


def keepRolling(speedR,speedL):
	interface.setMotorRotationSpeedReferences(motors,[speedL,speedR])
	return True

# TURNING FUNCTIONS

def left_90 (quantity):
    #convert quantity (of left 90 rotations about centre) to revolutions of the wheels in rad
	angle = radTurn*quantity
	print ("Rotating left by ", quantity*90, "degrees")
	interface.increaseMotorAngleReferences(motors,[angle,-angle])
	return True

def right_90 (quantity):
    #convert quantity (of right 90 rotations about center) to revolutions of the wheels in rad
	angle = radTurn*quantity
	print ("Rotating right by ", quantity*90, "degrees")
	interface.increaseMotorAngleReferences(motors,[-angle,angle])
	return True

#Needs to be tested:
def turnLeft(quantity):
    #convert quantity (of left 90 rotations about left wheel) to revolutions of the wheels in rad
	angle = radTurn*2*quantity
	print ("Turning left")
	interface.increaseMotorAngleReferences(motors,[angle,0])
	return True

def turnRight(quantity):
    #convert quantity (of right 90 rotations about right wheel) to revolutions of the wheels in rad
	angle = radTurn*2*quantity
	print ("Turning right")
	interface.increaseMotorAngleReferences(motors,[0,angle])
	return True


