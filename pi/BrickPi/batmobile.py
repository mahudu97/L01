import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

###########################SETTERS######################################
maxACC = 6.0

kp_left = 420.0
ki_left = 650.0
kd_left = 200.0
PWM_left= 18.0

kp_right = 420.0
ki_right = 700.0
kd_right = 500.0
PWM_right= 18.0

radTurn = 4.07435
radMove = 0.29488210557

# SETTING SENSOR PARAMS
touch_port [0,1]
interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)

# SETTING MOTOR PARAMS
motors = [0,3]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams_left = interface.MotorAngleControllerParameters()
motorParams_left.maxRotationAcceleration = maxACC
motorParams_left.maxRotationSpeed = 12.0
motorParams_left.feedForwardGain = 255/20.0
motorParams_left.minPWM = PWM_left
motorParams_left.pidParameters.minOutput = -255
motorParams_left.pidParameters.maxOutput = 255
motorParams_left.pidParameters.k_p = kp_left
motorParams_left.pidParameters.k_i = ki_left
motorParams_left.pidParameters.k_d = kd_left

motorParams_right = interface.MotorAngleControllerParameters()
motorParams_right.maxRotationAcceleration = maxACC
motorParams_right.maxRotationSpeed = 12.0
motorParams_right.feedForwardGain = 255/20.0
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
