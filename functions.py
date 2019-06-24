import numpy as np
import math
import cmath

v = 30
q = 0.9
w = q/(2*v)
A = (v*v)/q

def calcPosition(i):
    x = A * np.sin(w*i)
    y = A * np.sin(2*w*i)
    return [x,y]

def calcVelocity(i):
    t = i
    x = v * (np.cos(w*t)/2)
    y = v * np.cos(2*w*t)
    return [x,y]

def calcAcceleration(t):
    x = (-q) * (np.sin(w*t)/4)
    y = (-q) * np.sin(2*w*t)
    return [x,y]

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


def normrand(deviation):
    sigma = deviation
    x = np.random.normal(0,sigma,1)
    y = np.random.normal(0,sigma,1)
    return [x,y]

def cart_coord(i,dev):
    x_dev = normrand(dev)[0]
    y_dev = normrand(dev)[1]
    x = calcPosition(i)[0]+x_dev
    y = calcPosition(i)[1]+y_dev
    return [x,y],x_dev,y_dev

def cart_coord1(i,dev):
    x_dev = normrand(dev)[0]
    y_dev = normrand(dev)[1]
    x = calcPosition(i)[0]+x_dev
    y = calcPosition(i)[1]+y_dev
    return [x,y],x_dev,y_dev

def polar_coord(i, radarX, radarY):
    range_dev = normrand(20)[0]
    winkel_dev = normrand(0.15)[0]
    plainPosition = calcPosition(i)
    xk = plainPosition[0]
    yk = plainPosition[1]
    xs = radarX
    ys = radarY
    pos_r = np.array([xs,ys])
    range = np.linalg.norm(plainPosition-pos_r)
    winkel = np.arctan2((yk-ys),(xk-xs))
    return [range+range_dev, winkel+winkel_dev], range_dev,winkel_dev

def polar_RadarPunkt(i, radarX, radarY):
    vec,range_dev,winkel_dev = polar_coord(i, radarX, radarY)
    x = vec[0] * math.cos(vec[1]) + radarX
    y = vec[0] * math.sin(vec[1]) + radarY
    return[x, y],range_dev,winkel_dev

def coord_Distanz(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[0]-p1[0])
