import brickpi
import time

import sys

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]
touch_port [0,1]
interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)

pr = 420
dr = 31.5
ir = 700
pl = 420
dl = 31.5
il = 650

radTurn = 4.07435
radMove = 0.29488210557


interface.motorEnable(motors[0])
interface.motorEnable(motors[1])


motorParams_right = interface.MotorAngleControllerParameters()
motorParams_right.maxRotationAcceleration = 6.0
motorParams_right.maxRotationSpeed = 12.0
motorParams_right.feedForwardGain = 255/20.0
motorParams_right.minPWM = 15.0
motorParams_right.pidParameters.minOutput = -255a
motorParams_right.pidParameters.maxOutput = 255
motorParams_right.pidParameters.k_p = pr
motorParams_right.pidParameters.k_i = ir
motorParams_right.pidParameters.k_d = dr

motorParams_left = interface.MotorAngleControllerParameters()
motorParams_left.maxRotationAcceleration = 6.0
motorParams_left.maxRotationSpeed = 12.0
motorParams_left.feedForwardGain = 255/20.0
motorParams_left.minPWM = 15.0
motorParams_left.pidParameters.minOutput = -255
motorParams_left.pidParameters.maxOutput = 255
motorParams_left.pidParameters.k_p = pl
motorParams_left.pidParameters.k_i = il
motorParams_left.pidParameters.k_d = dl

interface.setMotorAngleControllerParameters(motors[0],motorParams_right)
interface.setMotorAngleControllerParameters(motors[1],motorParams_left)



logFile= "ATL_" + str(int(pr))+"_" + str(int(ir))+ "_" +str(int(dr))+ "_" +str(int(pl))+ "_" +str(int(il))+ "_" +str(int(dl))+".txt"
interface.startLogging(logFile)

angle = float(input("Enter an angle (rad): "))
#Move 20cm Back
angle_reverse = 5.897
angle_turn = radTurn*1.5
interface.increaseMotorAngleReferences(motors,[angle,-angle])
count = 0
while not interface.motorAngleReferencesReached(motors) or (interface.getSensorValue(touch_port[0]) == 1) or (interface.getSensorValue(touch_port[1]) == 1):
	#timer to stop loop
	count+=1
	

	motorAngles = interface.getMotorAngles(motors)
	if motorAngles :
		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
	time.sleep(0.01)
	
	# Bump on the right side
	if(interface.getSensorValue(touch_port[0]) == 1):
		###
		interface.increaseMotorAngleReferences(motors,[-angle_reverse,-angle_reverse])
		##turn Left
		interface.increaseMotorAngleReferences(motors,[angle_turn,-angle_turn])
	# Bump on the left side
	if(interface.getSensorValue(touch_port[1]) == 1):
		###
		interface.increaseMotorAngleReferences(motors,[-angle_reverse,-angle_reverse])
		##Turn Right
		interface.increaseMotorAngleReferences(motors,[-angle_turn,angle_turn])
	#if count>500:
	#	break

print "Destination reached!"

interface.stopLogging()




interface.terminate()
