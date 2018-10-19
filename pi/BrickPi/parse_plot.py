#!/usr/bin/python

# to use - install pip, matplotlib, tk
    # file "ATL.txt" should be in same dir

# Plotting library
from matplotlib import pyplot as plt
import pylab
import sys


class Record:
    def __init__(self):
        self.time      = []
        self.ref_rm    = []
        self.actual_rm = []
        self.diff_rm   = []
        self.ref_lm    = []
        self.actual_lm = []
        self.diff_lm   = []

    # add a data points into the lists
    def append(self, time, ref_rm, actual_rm, ref_lm, actual_lm):
        self.time.append(float(time))
        self.ref_rm.append(float(ref_rm))
        self.actual_rm.append(float(actual_rm))
        self.diff_rm.append(abs(float(ref_rm) - float(actual_rm)) )
        self.ref_lm.append(float(ref_lm))
        self.actual_lm.append(float(actual_lm))
        self.diff_lm.append(abs(float(ref_lm) - float(actual_lm)) )

    #Use to test
    #def __str__(self):
    #    return str(self.time) + "::" + str(self.ref_rm) + "::" + str(self.actual_rm) + "::" + \
    #            str(self.ref_lm) + "::" + str(self.actual_lm) + "::\n"


if __name__ == "__main__":
    # split file by new line
    lines = open(sys.argv[1]).read().splitlines()
    k = sys.argv[1].split("_")
    k_p = k[1]
    k_i = k[2]
    k_d = k[3][:-4]

    # Instantiate Record obj
    records = Record()

    for l in lines:
        # split line by whitespace
        tmp = l.split()
        # build record
        records.append(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

    # plot rm
    plt.figure(1)
    plt.title("Right motor reference and actual angle: Kp="+k_p+", Ki="+k_i+", Kd="+k_d)
    plt.xlabel("time (ns)")
    plt.ylabel("angle (radians)")
    plt.plot(records.time, records.ref_rm, label = "ref")
    plt.plot(records.time, records.actual_rm, label = "actual")
    plt.legend()
    pylab.savefig("rm_raa_"+k_p+"_"+k_i+"_"+k_d+".png", bbox_inches = "tight")
    plt.figure(2)
    plt.title("Right motor absolute error: Kp="+k_p+", Ki="+k_i+", Kd="+k_d)
    plt.xlabel("time (ns)")
    plt.ylabel("angle (radians)")
    plt.plot(records.time, records.diff_rm)
    pylab.savefig("rm_err_"+k_p+"_"+k_i+"_"+k_d+".png", bbox_inches = "tight")

    # plot lm
    plt.figure(3)
    plt.title("Left motor reference and actual angle: Kp="+k_p+", Ki="+k_i+", Kd="+k_d)
    plt.xlabel("time (ns)")
    plt.ylabel("angle (radians)")
    plt.plot(records.time, records.ref_lm, label = "ref")
    plt.plot(records.time, records.actual_lm, label = "actual")
    plt.legend()
    pylab.savefig("lm_raa_"+k_p+"_"+k_i+"_"+k_d+".png", bbox_inches = "tight")
    plt.figure(4)
    plt.title("Left motor absolute error: Kp="+k_p+", Ki="+k_i+", Kd="+k_d)
    plt.xlabel("time (ns)")
    plt.ylabel("angle (radians)")
    plt.plot(records.time, records.diff_lm)
    pylab.savefig("lm_err_"+k_p+"_"+k_i+"_"+k_d+".png", bbox_inches = "tight")
    plt.show()
