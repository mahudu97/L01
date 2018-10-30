import brickpi
import time
import batmobile

interface = brickpi.Interface()



while True:
	
	batmobile.keepRolling(0.1)
	
	if(interface.getSensorValue(batmobile.touch_port[1]) == 1) and (interface.getSensorValue(batmobile.touch_port[0]) == 1) :
		print ("both")
		batmobile.backward(20)
		time.sleep(2.5)
		##Turn Right
		batmobile.turnRight(-1)		
		time.sleep(2.5)
		continue
	
	# Bump on the right side
	if(interface.getSensorValue(batmobile.touch_port[0]) == 1):
		print ("left")
		batmobile.backward(20)
		time.sleep(2.5)
		##turn Left
		batmobile.turnLeft(-1)
		time.sleep(2.5)
		continue

	# Bump on the left side
	if(interface.getSensorValue(batmobile.touch_port[1]) == 1):
		###
		print ("right")
		batmobile.backward(20)
		time.sleep(2.5)
		##Turn Right
		batmobile.turnRight(-1)		
		time.sleep(2.5)
		continue
	
	
	



interface.terminate()
