import math

table2 = open("loc_01_hist.dat", 'w')
table3 = open("loc_02_hist.dat", 'w')

way02 = open("loc_01.dat", 'r')
way03 = open("loc_02.dat", 'r')

way2 = way02.read().split()
way3 = way03.read().split()

# distance will be discretised into chunks of 8cm
hist2 = [0]*64 # going to count how many occurences of each distance
wa_2 = 0
for i in range(len(way2)):
    value = math.floor(int(way2[i])/4)
    wa_2 += value**(i*8)
    hist2[int(value)]+=1

hist3 = [0]*64 # going to count how many occurences of each distance
wa_3 = 0
for i in range(len(way3)):
    value = math.floor(int(way3[i])/4)
    wa_3 += value**(i*8)
    hist3[int(value)]+=1

for i in range(len(hist2)):

    table2.write(str(hist2[i])+'\n')
    table3.write(str(hist3[i])+'\n')

table2.write("\nWeighted Avg for 2: "+str(wa_2)+'\n')
table3.write("\nWeighted Avg for 3: "+str(wa_3)+'\n')


table2.close()
table3.close()
