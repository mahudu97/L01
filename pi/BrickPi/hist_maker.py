import math

table2 = open("loc_01_hist.dat", 'w')
table3 = open("loc_02_hist.dat", 'w')

way02 = open("loc_01.dat", 'r')
way03 = open("loc_02.dat", 'r')

way2 = way02.read().split()
way3 = way03.read().split()

# distance will be discretised into chunks of 8cm
hist2 = [0]*64 # going to count how many occurences of each distance
for i in range(len(way2)):
    value = math.floor(int(way2[i])/4)
    hist2[int(value)]+=1

hist3 = [0]*64 # going to count how many occurences of each distance
for i in range(len(way3)):
    value = math.floor(int(way3[i])/4)
    hist3[int(value)]+=1

for i in range(len(hist2)):
    table2.write(str(hist2[i]))
for i in range(len(hist3)):
    table3.write(str(hist3[i]))


table2.close()
table3.close()
