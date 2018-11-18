#!/usr/bin/env python
# By Jacek Zienkiewicz and Andrew Davison, Imperial College London, 2014
# Based on original C code by Adrien Angeli, 2009

import batmobile as L01
import time
import math
import random
import os

# Location signature class: stores a signature characterizing one location
class LocationSignature:
    # 5 degrees rotation
    def __init__(self, no_bins = 72):
        self.sig = [0] * no_bins
        
    def print_signature(self):
        for i in range(len(self.sig)):
            print self.sig[i]

# --------------------- File management class ---------------
class SignatureContainer():
    def __init__(self, size = 5):
        self.size      = size; # max number of signatures that can be stored
        self.filenames = [];
        
        # Fills the filenames variable with names like loc_%%.dat 
        # where %% are 2 digits (00, 01, 02...) indicating the location number. 
        for i in range(self.size):
            self.filenames.append('loc_{0:02d}.dat'.format(i))

    # Get the index of a filename for the new signature. If all filenames are 
    # used, it returns -1;
    def get_free_index(self):
        n = 0
        while n < self.size:
            if (os.path.isfile(self.filenames[n]) == False):
                break
            n += 1
            
        if (n >= self.size):
            return -1;
        else:    
            return n;
 
    # Delete all loc_%%.dat files
    def delete_loc_files(self):
        print "STATUS:  All signature files removed."
        for n in range(self.size):
            if os.path.isfile(self.filenames[n]):
                os.remove(self.filenames[n])
            
    # Writes the signature to the file identified by index (e.g, if index is 1
    # it will be file loc_01.dat). If file already exists, it will be replaced.
    def save(self, signature, index):
        filename = self.filenames[index]
        if os.path.isfile(filename):
            os.remove(filename)
            
        f = open(filename, 'w')

        for i in range(len(signature.sig)):
            s = str(signature.sig[i]) + "\n"
            f.write(s)
        f.close();

    # Read signature file identified by index. If the file doesn't exist
    # it returns an empty signature.
    def read(self, index):
        ls = LocationSignature()
        filename = self.filenames[index]
        if os.path.isfile(filename):
            f = open(filename, 'r')
            for i in range(len(ls.sig)):
                s = f.readline()
                if (s != ''):
                    ls.sig[i] = int(s)
            f.close();
        else:
            print "WARNING: Signature does not exist."
        
        return ls


# getting a sonar reading
def read_sonar():
    usReadings = []
    for i in range(11):
        usReadings.append(L01.interface.getSensorValue(L01.us_port))
        time.sleep(0.0045)
    usReadings.sort()
    if usReadings[5] :
        return usReadings[5][0]
    else:
        print "Failed US reading"
        return read_sonar()

def characterize_location(ls):
    for i in range(len(ls.sig)):
        # read
        ls.sig[i] = read_sonar()
        L01.left_90(5/90) # rotate 5 deg for next reading

def make_histogram(x): #take a LocationSignature in distance/angle space, and returns a LocationSignature in frequency/distance space
	# distance will be discretised into chunks of 8cm
	hist = [0]*32 # going to count how many occurences of each distance
	for i in range(len(x.sig)):
		value = math.floor(x.sig[i]/8)
		hist[value]+=1
	return hist

# angle invariant
def compare_signatures(ls1, ls2):
    dist = 0
    a1 = make_histogram(ls1)
    a2 = make_histogram(ls2)
    # sum of differences squared
    for i in range(len(a1)):
        dist += (a1[i]-a2[i])**2
    return dist

# angle variant - pass in arrays
def compare_signatures_simple(ls1, ls2):
    dist = 0
    # sum of differences squared
    for i in range(len(ls1.sig)):
        dist += (ls1.sig[i]-ls2.sig[i])**2
    return dist

def find_rotation(obs, pred):
    # array to shift by 1 at end of each iteration
    shifted = []
    for i in range(len(obs.sig)):
        shifted.append( obs.sig[i] )

    matching_angle = 0
    best_dist = 99999999999999999999

    for i in range(len(obs.sig)):
        dist = compare_signatures_simple(shifted, pred.sig)
        if dist < best_dist:
            best_dist = dist
            matching_angle = i*5
        # now left rotat shifted
        shifted = shifted[1:] + shifted [0]

    if matching_angle > 180:
        matching_angle -= 360

    return matching_angle


# This function characterizes the current location, and stores the obtained 
# signature into the next available file.
def learn_location():
    ls = LocationSignature()
    # gets sonar readings
    characterize_location(ls)
    idx = signatures.get_free_index()
    if (idx == -1): # run out of signature files
        print "\nWARNING:"
        print "No signature file is available. NOTHING NEW will be learned and stored."
        print "Please remove some loc_%%.dat files.\n"
        return
    
    signatures.save(ls,idx)
    print "STATUS:  Location " + str(idx) + " learned and saved."

# This function tries to recognize the current location.
# 1.   Characterize current location
# 2.   For every learned locations
# 2.1. Read signature of learned location from file
# 2.2. Compare signature to signature coming from actual characterization
# 3.   Retain the learned location whose minimum distance with
#      actual characterization is the smallest.
# 4.   Display the index of the recognized location on the screen
def recognize_location():
    ls_obs = LocationSignature()
    characterize_location(ls_obs)

    best_match = 0
    smallest_dist = 9999999999999999999
    for idx in range(signatures.size):
        print "STATUS:  Comparing signature " + str(idx) + " with the observed signature."
        ls_read = signatures.read(idx)
        dist    = compare_signatures(ls_obs, ls_read)
        if dist < smallest_dist:
            smallest_dist = dist
            best_match = idx
    # at this location
    print "We are at location " + str(best_match)
    # now rotation
    ls_pred = signatures.read(best_match)
    rot = find_rotation(ls_obs, ls_pred)
    print "We are " + str(rot) + "degrees from x-axis at this position"

# Prior to starting learning the locations, it should delete files from previous
# learning either manually or by calling signatures.delete_loc_files(). 
# Then, either learn a location, until all the locations are learned, or try to
# recognize one of them, if locations have already been learned.

signatures = SignatureContainer(5)
#signatures.delete_loc_files()

for i in range(5):
    print "Place the robot at the waypoint."
    ans = "N"
    while ans != "Y":
        print "Ready? Y/N"
        ans = input()

    learn_location()

print "Now place robot in position for matching"
ans = "N"
while ans != "Y":
        print "Ready? Y/N"
        ans = input()

recognize_location()


