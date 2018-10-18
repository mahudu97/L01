import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])


motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
# motorParams.pidParameters.k_p = 100
# motorParams.pidParameters.k_i = 0.0
# motorParams.pidParameters.k_d = 0.0

# interface.startLogging("AngleTuningLog100_0_0.txt")
#
# while True:
#
# 	angle = float(input("Enter an angle (rad): "))
#
# 	interface.increaseMotorAngleReferences(motors,[angle,-angle])
#
# 	while not interface.motorAngleReferencesReached(motors) :
# 		motorAngles = interface.getMotorAngles(motors)
# 		if motorAngles :
# 			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
# 		time.sleep(0.1)
#
# 	print "Destination reached!"
#
# interface.stopLogging("AngleTuningLog100_0_0.txt")

kp_test = [100,200,300,400,500,600,700,800,900,1000]

ki_test = [0,100,200,300,400,500,600,700,800,900,1000]

kd_test = [0,100,200,300,400,500,600,700,800,900]

for pCurr in kp_test:
	motorParams.pidParameters.k_p = pCurr
	print "KP"
	for iCurr in ki_test:
		motorParams.pidParameters.k_i = iCurr
		print "KI"
		for dCurr in kd_test:
			print "KD"

			motorParams.pidParameters.k_d = dCurr

			interface.setMotorAngleControllerParameters(motors[0],motorParams)
			interface.setMotorAngleControllerParameters(motors[1],motorParams)

			logFile = "AngleTuningLog"+str (pCurr) + "_" + str(iCurr) + "_" + str(dCurr) + ".txt"


			interface.startLogging(logFile)

			angle = 6.2832 #2pi radians ie a circle

			interface.increaseMotorAngleReferences(motors,[angle,-angle])
			count =0

			while not interface.motorAngleReferencesReached(motors) :
				count+=1
				motorAngles = interface.getMotorAngles(motors)
				if motorAngles :
					print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
				time.sleep(0.01)
				if count>150:
					break


			print "Destination reached!"


			interface.stopLogging()



interface.terminate()
