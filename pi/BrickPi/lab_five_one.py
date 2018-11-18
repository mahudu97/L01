import particleDataStructures as world
import batmobile as L01
import time
import math



def read_sonar():
	usReadings = []
	for i in range(11):
		usReadings.append(L01.interface.getSensorValue(L01.us_port))
		time.sleep(0.0045)
	usReadings.sort()
	if usReadings[5]:
		# print "I measured a distance of "+ str(usReadings[5])
		return usReadings[5][0]
	else:
		print "Failed US reading"
		return read_sonar()



def spin_me(x,y):
	theta = 0
	for i in range(72):
		z = read_sonar()
		x2 = x + z*math.cos(theta)
		y2 = y + z*math.sin(theta)
		print "drawLine:" + str((x,y,x2,y2))
		theta += 0.0872665
		L01.left_90(0.05555555556)
		time.sleep(1)


mymap = world.Map()
world.init_world(mymap)


spin_me(200,300)