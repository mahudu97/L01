import batmobile
import time


while not interface.motorAngleReferencesReached(motors) or (interface.getSensorValue(touch_port[0]) == 1) or (interface.getSensorValue(touch_port[1]) == 1):
	
	# Bump on the right side
	if(interface.getSensorValue(touch_port[0]) == 1):
		
		batmobile.backward(20)
		time.sleep(2.5)
		##turn Left
		batmobile.left_90(1.5)

	# Bump on the left side
	if(interface.getSensorValue(touch_port[1]) == 1):
		###
		batmobile.backward(20)
		time.sleep(2.5)
		##Turn Right
		batmobile.right_90(1.5)		
		time.sleep(2.5)
	

print "Destination reached!"


interface.terminate()
