import brickpi
import time

import system

#We expect 7 command line arguments. The script name and 2*3 PID - 3 for each motorAngleReferencesReached

if len(sys.argv) < 7 :
	print "Program expects command line arguments with PID values for both motors. Should look like script.py pr ir dr pl il dl"
	exit()


interface=brickpi.Interface()
interface.initialize()

motors = [0,3]

pr = sys.argv[1]
ir = sys.argv[2]
dr = sys.argv[3]
pl = sys.argv[4]
il = sys.argv[5]
dl = sys.argv[6]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])


motorParams_right = interface.MotorAngleControllerParameters()
motorParams_right.maxRotationAcceleration = 6.0
motorParams_right.maxRotationSpeed = 12.0
motorParams_right.feedForwardGain = 255/20.0
motorParams_right.minPWM = 18.0
motorParams_right.pidParameters.minOutput = -255
motorParams_right.pidParameters.maxOutput = 255
motorParams_right.pidParameters.k_p = pr
motorParams_right.pidParameters.k_i = ir
motorParams_right.pidParameters.k_d = dr

motorParams_left = interface.MotorAngleControllerParameters()
motorParams_left.maxRotationAcceleration = 6.0
motorParams_left.maxRotationSpeed = 12.0
motorParams_left.feedForwardGain = 255/20.0
motorParams_left.minPWM = 18.0
motorParams_left.pidParameters.minOutput = -255
motorParams_left.pidParameters.maxOutput = 255
motorParams_left.pidParameters.k_p = pl
motorParams_left.pidParameters.k_i = il
motorParams_left.pidParameters.k_d = dl

interface.setMotorAngleControllerParameters(motors[0],motorParams_right)
interface.setMotorAngleControllerParameters(motors[1],motorParams_left)


while True:

	
	logFile= "ATL_" + str(pr)+"_" + str(ir)+ "_" +str(dr)+ "_" +str(pl)+ "_" +str(il)+ "_" +str(dl)+".txt"
	interface.startLogging(logFile)

	#angle = float(input("Enter an angle (rad): "))
	angle = 6.2832 #2pi const

	interface.increaseMotorAngleReferences(motors,[angle,-angle])

	while not interface.motorAngleReferencesReached(motors) :
		motorAngles = interface.getMotorAngles(motors)
		if motorAngles :
			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
		time.sleep(0.1)

	print "Destination reached!"

interface.stopLogging(logFile)




interface.terminate()
