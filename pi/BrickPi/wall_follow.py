import batmobile as bat
import time


distance = 30
base = 6
p=0.1

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


	
	
	
	
