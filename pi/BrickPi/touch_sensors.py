import batmobile
import time

x = 'a'

while (x != 'c'):

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
