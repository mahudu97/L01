import batmobile
import keyboard as key 

while true:
	entry = input("Enter a letter: ")
    try:
        if entry == ('w'):
            batmobile.forward(2)
            continue
        if entry == ('s'):
            batmobile.backward(2)
            continue
        if entry == ('a'):
            batmobile.left_90(1)
           continue
        if entry == ('d'):
            batmobile.right_90()
            continue
        if entry == ('q'):
            batmobile.turnLeft()
            continue
        if entry == ('e'):
            batmobile.turnRight()
            continue
    except:
        if entry == ('k'):
            break


print "++++++++++++++++++++++++++++++++++++++++++++++++\n\nJoystick has been terminated. Run again to use\n\n++++++++++++++++++++++++++++++++++++++++++++++++"
