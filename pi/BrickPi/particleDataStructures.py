#!/usr/bin/env python 

# Some suitable functions and data structures for drawing a map and particles

import time
import random
import math

# A Canvas class for drawing a map and particles:
# 	- it takes care of a proper scaling and coordinate transformation between
#	  the map frame of reference (in cm) and the display (in pixels)
class Canvas:
    def __init__(self,map_size=210):
        self.map_size    = map_size;    # in cm;
        self.canvas_size = 768;         # in pixels;
        self.margin      = 0.05*map_size
        self.scale       = self.canvas_size/(map_size+2*self.margin)

    def drawLine(self,line):
        x1 = self.__screenX(line[0])
        y1 = self.__screenY(line[1])
        x2 = self.__screenX(line[2])
        y2 = self.__screenY(line[3])
        print "drawLine:" + str((x1,y1,x2,y2))

    def drawParticles(self,data):
        display = [(self.__screenX(d[0]),self.__screenY(d[1])) + d[2:] for d in data]
        print "drawParticles:" + str(display)

    def __screenX(self,x):
        return (x + self.margin)*self.scale

    def __screenY(self,y):
        return (self.map_size + self.margin - y)*self.scale

# A Map class containing walls
class Map:
    def __init__(self):
        self.walls = []

    def add_wall(self,wall):
        self.walls.append(wall)

    def clear(self):
        self.walls = []

    def draw(self):
        for wall in self.walls:
            canvas.drawLine(wall)

# Simple Particles set
class Particles:
    def __init__(self):
        self.n = 100    
        self.data = []
    
    # implemented out of class
    #def update(self):
        #self.data = [(calcX(), calcY(), calcTheta(), calcW()) for i in range(self.n)];
    
    def draw(self):
        canvas.drawParticles(self.data)

canvas = Canvas()	# global canvas we are going to draw on

def init_world(mymap):
    # Definitions of walls
    # a: O to A
    # b: A to B
    # c: C to D
    # d: D to E
    # e: E to F
    # f: F to G
    # g: G to H
    # h: H to O
    mymap.add_wall((0,0,0,168))        # a
    mymap.add_wall((0,168,84,168))     # b
    mymap.add_wall((84,126,84,210))    # c
    mymap.add_wall((84,210,168,210))   # d
    mymap.add_wall((168,210,168,84))   # e
    mymap.add_wall((168,84,210,84))    # f
    mymap.add_wall((210,84,210,0))     # g
    mymap.add_wall((210,0,0,0))        # h

    ######adding crosses for waypoints#####
    mymap.add_wall((79,30,89,30))       #h1
    mymap.add_wall((84,25,84,35))       #v1
    mymap.add_wall((175,30,185,30))     #h2
    mymap.add_wall((180,25,180,35))     #v2
    mymap.add_wall((175,54,185,54))     #h3
    mymap.add_wall((180,49,180,59))     #v3
    mymap.add_wall((133,54,143,54))     #h4
    mymap.add_wall((138,49,138,59))     #v4
    mymap.add_wall((133,168,143,168))   #h5
    mymap.add_wall((138,163,138,173))   #v5
    mymap.add_wall((109,168,119,168))   #h6
    mymap.add_wall((114,163,114,173))   #v6
    mymap.add_wall((109,84,119,84))     #h7
    mymap.add_wall((114,79,114,89))     #v7
    mymap.add_wall((79,84,89,84))       #h8
    mymap.add_wall((84,79,84,89))       #v8
    ########################################

    mymap.draw()
