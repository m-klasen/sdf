import numpy as np
import math

v = 300
q = 9
w = q/(2*v)
A = (v*v)/q

def calcPosition(i):
    x = A * np.sin(w*i)
    y = A * np.sin(2*w*i)
    i = [x,y]
    return i

def calcVelocity(i):
    t = i
    x = v * (np.cos(w*t)/2)
    y = v * np.cos(2*w*t)
    vec = [x,y]
    return vec

def calcAcceleration(t):
    x = (-q) * (np.sin(w*t)/4)
    y = (-q) * np.sin(2*w*t)
    vec = [x,y]
    return vec

def calc_tangent(t):
    x= v*math.cos(w*t)/2
    y= v*math.cos(2*w*t)
    return [x/math.sqrt(x*x+y*y),y/math.sqrt(x*x+y*y)]

def calc_normal(t):
    x= -(v*math.cos(2*w*t))
    y= v*math.cos(w*t)/2
    return [x/math.sqrt(x*x+y*y),y/math.sqrt(x*x+y*y)]

def abs_velo(t):
    [x,y] = calcVelocity(t)
    return math.sqrt(x*x+y*y)

def abs_accel(t):
    [x,y] = calcAcceleration(t)
    return math.sqrt(x*x+y*y)

def accel_tangent(t):
    [x,y] = calcAcceleration(t)
    return [x*calc_tangent(t)[0],y*calc_tangent(t)[1]]

def accel_normal(t):    
    [x,y] = calcAcceleration(t)
    return [x*calc_normal(t)[0],y*calc_normal(t)[1]]


def normrand(i):
    sigma = 50
    x = np.random.normal(0,sigma,1)
    y = np.random.normal(0,sigma,1)
    print([x,y])
    return [x,y]

def cart_coord(i):
    x = calcPosition(i)[0]+calcVelocity(i)[0]+calcAcceleration(i)[0]+normrand(i)[0]
    y = calcPosition(i)[1]+calcVelocity(i)[1]+calcAcceleration(i)[1]+normrand(i)[1]
    return [x,y]