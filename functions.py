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


def normrand(deviation):
    sigma = deviation
    x = np.random.normal(0,sigma,1)
    y = np.random.normal(0,sigma,1)
    return [x,y]

def cart_coord(i):
    x = calcPosition(i)[0]+normrand(50)[0]
    y = calcPosition(i)[1]+normrand(50)[1]
    return [x,y]

def polar_coord(i, radarX, radarY):
    deviation = 20
    winkel = 0.2
    plainPosition = calcPosition(i)
    xk = plainPosition[0]
    yk = plainPosition[1]
    xs = radarX
    ys = radarY
    range = math.sqrt(math.pow((xk-xs), 2) + math.pow((yk-ys), 2)) + normrand(deviation)[0]
    winkel = math.atan((yk-ys)/(xk-xs)) #+ normrand(winkel)[1]
    while True:
        if (xk-xs) < 0:
            if (yk-ys) < 0:
                winkel -= math.pi
                break
            winkel += math.pi
            break
        break
    return [range, winkel]