import batmobile
import keyboard as key 

while true:

    try:
        if key.is_pressed('w'):
            batmobile.forward(2)
            break
        if key.is_pressed('s'):
            batmobile.backward(2)
            break
        if key.is_pressed('a'):
            batmobile.left_90(1)
            break
        if key.is_pressed('d'):
            batmobile.right_90()
            break
        if key.is_pressed('q'):
            batmobile.turnLeft()
            break
        if key.is_pressed('e'):
            batmobile.turnRight()
            break
        except:
            if key.is_pressed('k'):
                break


print "++++++++++++++++++++++++++++++++++++++++++++++++\n\nJoystick has been terminated. Run again to use\n\n++++++++++++++++++++++++++++++++++++++++++++++++"
