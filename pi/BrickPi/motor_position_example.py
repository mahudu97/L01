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
motorParams.pidParameters.k_p = 500.0
motorParams.pidParameters.k_i = 200.0
motorParams.pidParameters.k_d = 100.0

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)


while True:
	pCurr =float(input("Enter K_P: "))
	iCurr =float(input("Enter K_I: "))
	dCurr =float(input("Enter K_D: "))

	motorParams.pidParameters.k_p = pCurr
	motorParams.pidParameters.k_i = iCurr
	motorParams.pidParameters.k_d = dCurr

	logFile= "ATL_" + str(pCurr)+"_" + str(iCurr)+ "_" +str(dCurr)+".csv"
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
