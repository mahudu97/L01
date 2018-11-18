import math


def make_histogram(x): #take a LocationSignature in distance/angle space, and returns a LocationSignature in frequency/distance space
	# distance will be discretised into chunks of 8cm
	hist = [0]*32 # going to count how many occurences of each distance
	for i in range(len(x.sig)):
		value = math.floor(x.sig[i]/8)
		hist[value]+=1
	return hist