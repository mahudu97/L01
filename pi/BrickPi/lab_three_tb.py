import lab_three as l3

total =0
for i in range (250):
    total += l3.lab_three()
    currAvg = total/(i+1)
    print  str(i) + "th Average: " + str(currAvg)

