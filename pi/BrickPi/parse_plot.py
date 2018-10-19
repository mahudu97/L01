#!/usr/bin/python



class Record:
    def __init__(self, time, ref_rm, actual_rm, ref_lm, actual_lm):
        self.time      = time
        self.ref_rm    = ref_rm
        self.actual_rm = actual_rm
        self.ref_lm    = ref_lm
        self.actual_lm = actual_lm

    def __str__(self):
        return self.time + "::" + self.ref_rm + "::" + self.actual_rm + "::" + \
                self.ref_lm + "::" + self.actual_lm + "::\n"


if __name__ == "__main__":
    lines = open("ATL.txt").read().splitlines()

    records = []

    for l in lines:
        tmp = l.split()
        r = Record(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
        print r