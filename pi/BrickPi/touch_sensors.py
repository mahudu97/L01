import brickpi
import time
import sys
import batmobile

interface=brickpi.Interface()
interface.initialize()
motors = [0,3]
touch_port [0,1]
interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)

logFile= "ATL_" + str(int(pr))+"_" + str(int(ir))+ "_" +str(int(dr))+ "_" +str(int(pl))+ "_" +str(int(il))+ "_" +str(int(dl))+".txt"
interface.startLogging(logFile)

angle = float(input("Enter an angle (rad): "))
#Move 20cm Back
angle_reverse = 5.897
angle_turn = radTurn*1.5

interface.increaseMotorAngleReferences(motors,[angle,angle])

count = 0

while not interface.motorAngleReferencesReached(motors):
	if(interface.getSensorValue(touch_port[1]) == 1) and (interface.getSensorValue(touch_port[0]) == 1) :
		print ("both")
		# batmobile.backward(20)
		# time.sleep(2.5)
		# ##Turn Right
		# batmobile.turnRight(-1)		
		# time.sleep(2.5)
		continue
	
	# Bump on the right side
	if(interface.getSensorValue(touch_port[0]) == 1):
		print ("left")
		# batmobile.backward(20)
		# time.sleep(2.5)
		# ##turn Left
		# batmobile.turnLeft(-1)
		# time.sleepd(2.5)
		continue

	# Bump on the left side
	if(interface.getSensorValue(touch_port[1]) == 1):
		###
		print ("right")
		# batmobile.backward(20)
		# time.sleep(2.5)
		# ##Turn Right
		# batmobile.turnRight(-1)		
		# time.sleep(2.5)
		continue
	
	
	
	
	x = input("Please tell me someone I should know, or enter 'quit': ")


interface.terminate()

interface.stopLogging()
interface.terminate()
