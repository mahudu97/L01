import batmobile
import time

L01 = batmobile

#L01.forward(100)
#time.sleep(5)

#L01.backward(40)
#time.sleep(5)

#L01.left_90(4)
#time.sleep(5)

#L01.right_90(1)
#time.sleep(5)

for i in range (360/5):
    L01.right_90(5/90)
    time.sleep(0.5)

print "Square complete!"
