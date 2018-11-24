import batmobile as bat
import time


bat.interface.sensorEnable(bat.us_port, bat.brickpi.SensorType.SENSOR_ULTRASONIC)

distance = 30

p=0.2

while True:
	# returns tuple 
	usReading = bat.interface.getSensorValue(bat.us_port)

	speed = -p*(distance - usReading[0])

	bat.keepRolling(speed,speed)

	if usReading :
		print usReading
	else:
		print "Failed US reading"

	time.sleep(0.05)

bat.interface.terminate()
