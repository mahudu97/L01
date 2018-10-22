#Covariance Matrix
import numpy as np

#X values
x = []
#Y values
y = []

#Open File
file = open('square_test/results.txt', 'r')

#Read file into array
for line in file:
	fields = line.split(" ")
	x.append(float(fields[0]))
	y.append(float(fields[1]))

#Calculate the mean values
x_bar = float(sum(x))/len(x)
y_bar = float(sum(y))/len(y)

L1 = 0.0
L2 = 0.0
R1 = 0.0
R2 = 0.0
counter = 0

#Calculate the Matrix
for i in x:
	L1 = L1 + (( i - x_bar)**2)
	L2 = L2 + (( i - x_bar)*( y[counter] - y_bar))
	R1 = R1 + (( i - x_bar)*( y[counter] - y_bar))
	R2 = R2 + (( y[counter] - y_bar)**2)
	counter= counter +1
	
#Print the matrix
print L1/10 , R1/10 
print L2/10 , R2/10 
