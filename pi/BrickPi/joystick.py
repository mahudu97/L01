import batmobile
import keyboard as key

def main():
	bat = batmobile

	while True:
		entry = raw_input("Enter a letter: ")
		try:
			if entry == ('w'): #^[[A
				bat.forward(10)
				continue
			if entry == ('s'): #^[[B
				bat.backward(10)
				continue
			if entry == ('a'): #^[[D
				bat.left_90(1)
				continue
			if entry == ('d'): #^[[C
				bat.right_90(1)
				continue
			if entry == ('q') or: 
				bat.turnLeft()
				continue
			if entry == ('e') or:
				bat.turnRight()
				continue

		except:
			if entry == 'k':
				break



	print "++++++++++++++++++++++++++++++++++++++++++++++++\n\nJoystick has been terminated. Run again to use\n\n++++++++++++++++++++++++++++++++++++++++++++++++"


if  __name__ =='__main__':main()
