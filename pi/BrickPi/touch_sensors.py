import time
import batmobile

cruise = batmobile.maxVEL

batmobile.keepRolling(cruise, cruise)


while True:
	# get touch sensor values
	pressed0 = batmobile.interface.getSensorValue(batmobile.touch_port[0])
	pressed1 = batmobile.interface.getSensorValue(batmobile.touch_port[1])

	if pressed0[0] or pressed1[0]:
		batmobile.interface.setMotorPwm(batmobile.motors[0],0)
		batmobile.interface.setMotorPwm(batmobile.motors[1],0)
		if pressed0[0] and pressed1[0]:
			print ("both")
			batmobile.backward(20)
			time.sleep(1.5)
			##Turn Around
			batmobile.right_90(2)
			time.sleep(1.5)
			batmobile.keepRolling(cruise, cruise)



		# Bump on the left side
		elif pressed0[0]:
			if pressed1[0]:
				print ("both")
				batmobile.backward(20)
				time.sleep(1.5)
				##Turn Around
				batmobile.right_90(2)
				time.sleep(1.5)
				batmobile.keepRolling(cruise, cruise)
			else: 
				print ("left")
				batmobile.backward(20)
				time.sleep(1.5)
				#reverse
				batmobile.turnLeft(-1)
				time.sleep(1.5)
				batmobile.keepRolling(cruise, cruise)


		# Bump on the right side
		elif pressed1[0]:
			if pressed0[0]:
				print ("both")
				batmobile.backward(20)
				time.sleep(1.5)
				##Turn Around
				batmobile.right_90(2)
				time.sleep(1.5)
				batmobile.keepRolling(cruise, cruise)
				
			else:
				print ("right")
				batmobile.backward(20)
				time.sleep(1.5)
				##Turn Right
				batmobile.turnRight(-1)
				time.sleep(1.5)
				batmobile.keepRolling(cruise, cruise)



batmobile.interface.terminate()
