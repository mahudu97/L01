import batmobile

bat = batmobile

while true:
	entry = input("Enter a letter: ")
    try:
        if entry == ('w'):
            bat.forward(2)
            continue
        if entry == ('s'):
            bat.backward(2)
            continue
        if entry == ('a'):
            bat.left_90(1)
           continue
        if entry == ('d'):
            bat.right_90()
            continue
        if entry == ('q'):
            bat.turnLeft()
            continue
        if entry == ('e'):
            bat.turnRight()
            continue
    except:
        if entry == ('k'):
            break


print "++++++++++++++++++++++++++++++++++++++++++++++++\n\nJoystick has been terminated. Run again to use\n\n++++++++++++++++++++++++++++++++++++++++++++++++"
