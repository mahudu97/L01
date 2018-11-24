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
            f.close()
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
        ls.sig[i] = 0
    # 3 runs
    for k in range(1,4):
        print "Place the robot at the waypoint."
        ans = "n"
        while ans != "y":
            ans = input("Ready? y/n\n")
        for i in range(len(ls.sig)):
            # read
            ls.sig[i] += read_sonar()
            L01.left_90(0.05555555555) # rotate 5 deg for next reading
            time.sleep(0.3)
    # avg
    for i in range(len(ls.sig)):
        ls.sig[i] /= 3



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


# Prior to starting learning the locations, it should delete files from previous
# learning either manually or by calling signatures.delete_loc_files(). 
# Then, either learn a location, until all the locations are learned, or try to
# recognize one of them, if locations have already been learned.

signatures = SignatureContainer(5)
signatures.delete_loc_files()

for i in range(5):
   print "Place the robot at the waypoint."
   ans = "n"
   while ans != "y":
      ans = input("Ready? y/n\n")

   learn_location()



