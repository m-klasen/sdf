import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import  GridSpec
from functions import *


ncols = 6
nrows = 4
grid = GridSpec(nrows, ncols,
                left=0.1, bottom=0.15, right=0.94, top=0.94, wspace=1, hspace=1)
'''
#Figure 0
fig = plt.figure(0)

axesPosition = fig.add_subplot(grid[0:2, 0:2])
axesPositionArrow = fig.add_subplot(grid[2:4, 0:2])
axesVelocity = fig.add_subplot(grid[0:2, 2:4])
axesVelocityArrow = fig.add_subplot(grid[2:4, 2:4])
axesAcceleration = fig.add_subplot(grid[0:2, 4:6])
axesAccelerationArrow = fig.add_subplot(grid[2:4, 4:6])

#Figure 1
ax = plt.figure(1)

plottangent = ax.add_subplot(grid[0:2, 0:2])
plotnormal = ax.add_subplot(grid[0:2, 2:4])
plot_absvelo = ax.add_subplot(grid[0:2,4:6])
plot_absaccel = ax.add_subplot(grid[2:4,0:2])
plot_acceltangent = ax.add_subplot(grid[2:4,2:4])
plot_accelnormal = ax.add_subplot(grid[2:4,4:6])

#Figure 2
radar = plt.figure(2)
plot_cartesian = radar.add_subplot(grid[0:6, 0:6])
'''
#Figure 3
kal = plt.figure(3)
plot_vergleich = kal.add_subplot(grid[0:6, 0:6])


def main():
    #setAxesSize()
    #ani = animation.FuncAnimation(fig, update_plot, interval=1, frames=300)
    #ani2 = animation.FuncAnimation(ax, update_plot2, interval=1, frames=300)
    #ani3 = animation.FuncAnimation(radar, update_plot_radar, interval=1, frames=300)
    drawKalman()
    plt.show()

def setAxesSize():
    axesPosition.set_ylim(-12000, 12000)
    axesPosition.set_xlim(-12000, 12000)
    axesPosition.set_title('Position')

    axesVelocity.set_ylim(-400, 400)
    axesVelocity.set_xlim(-300, 300)
    axesVelocity.set_title('Velocity')

    axesAcceleration.set_ylim(-10, 10)
    axesAcceleration.set_xlim(-5, 5)
    axesAcceleration.set_title('Acceleration')

    axesPositionArrow.set_ylim(-5000, 5000)
    axesPositionArrow.set_xlim(-2000, 2000)


    axesVelocityArrow.set_ylim(-120, 120)
    axesVelocityArrow.set_xlim(-100, 100)

    axesAccelerationArrow.set_ylim(-5, 5)
    axesAccelerationArrow.set_xlim(-1, 1)


def update_plot(i):
    multi = 10
    dotSizePosition = 10 * multi
    dotSizeVelocity = multi
    dotSizeAcceleration = multi
    i = i * multi

    vecPosition = calcPosition(i)
    xPosition = vecPosition[0]
    yPosition = vecPosition[1]

    vecPositionOld = calcPosition(i-multi)
    xPositionOld = vecPositionOld[0]
    yPositionOld = vecPositionOld[1]

    vecVelocity = calcVelocity(i)
    xVelocity = vecVelocity[0]
    yVelocity = vecVelocity[1]

    vecVelocityOld = calcVelocity(i-multi)
    xVelocityOld = vecVelocityOld[0]
    yVelocityOld = vecVelocityOld[1]

    vecAcceleration = calcAcceleration(i)
    xAcceleration = vecAcceleration[0]
    yAcceleration = vecAcceleration[1]

    vecAccelerationOld = calcAcceleration(i-multi)
    xAccelerationOld = vecAccelerationOld[0]
    yAccelerationOld = vecAccelerationOld[1]



    if i == 0:
        arrow(xPosition, yPosition, xVelocity, yVelocity, xAcceleration, yAcceleration)
    else:
        xDifPos = xPosition - xPositionOld
        yDifPos = yPosition - yPositionOld

        xDifVel = xVelocity - xVelocityOld
        yDifVel = yVelocity - yVelocityOld

        xDifAcc = xAcceleration - xAccelerationOld
        yDifAcc = yAcceleration - yAccelerationOld



        arrow(xDifPos, yDifPos, xDifVel, yDifVel, xDifAcc, yDifAcc)

    clear(xPosition,yPosition, xPositionOld, yPositionOld)
    axesPosition.scatter([xPosition], [yPosition], c=[1], s = dotSizePosition)
    axesVelocity.scatter([xVelocity], [yVelocity], c=[1], s = dotSizeVelocity)
    axesAcceleration.scatter([xAcceleration], [yAcceleration], c=[1], s = dotSizeAcceleration)


def update_plot2(i):
    multi = 10
    dotSizePosition = 10 * multi
    dotSizeVelocity = multi
    dotSizeAcceleration = multi
    i = i * multi

    plottangent.scatter(calc_tangent(i)[0],calc_tangent(i)[1])
    plotnormal.scatter(calc_normal(i)[0], calc_normal(i)[1])

    plot_absvelo.scatter(abs_velo(i),i)
    plot_absaccel.scatter(abs_accel(i),i)
    plot_acceltangent.scatter(accel_tangent(i)[0],accel_tangent(i)[1])
    plot_accelnormal.scatter(accel_normal(i)[0],accel_normal(i)[1])

def update_plot_radar(i):
    multi = 5
    dotSizePosition = 10 * multi
    i = i * multi
    
    vecPosition = calcPosition(i)
    xPosition = vecPosition[0]
    yPosition = vecPosition[1]
    plot_cartesian.scatter([xPosition], [yPosition], c='red', s = dotSizePosition)

    vecRadarPosition = cart_coord(i)
    xRadarPosition = vecRadarPosition[0]
    yRadarPosition = vecRadarPosition[1]
    plot_cartesian.scatter([xRadarPosition], [yRadarPosition], c='blue', s = dotSizePosition)
    
    radarX = 0
    radarY = 0
    vecRadarPosition = polar_coord(i, radarX, radarY)
    xRadarPosition = vecRadarPosition[0] * math.cos(vecRadarPosition[1]) 
    yRadarPosition = vecRadarPosition[0] * math.sin(vecRadarPosition[1])
    plot_cartesian.scatter([xRadarPosition], [yRadarPosition], c='green', s = dotSizePosition)

def drawKalman():
    start = 1   #min 1 wegen kalman prediction
    end = 50
    x1 = [start, end]
    y1 = [0, 0]
    x2 = []
    gTruth =[]
    radar =[]
    radarY =[]
    kFilter =[]
    kFilterY =[]
    for x in range(start, end): #startet bei 1 wegen kalman prediction
        x2.append(x)
        gTruth.append(calcPosition(x))
        radar.append(polar_RadarPunkt(x, 0, 0))
        kFilter.append(constAccKalman(x-1, 1, 1, 0, 0))
        radarY.append(coord_Distanz(radar[x-1], gTruth[x-1])) #x-1 da ich ja auch bei 1 starte
        kFilterY.append(coord_Distanz(kFilter[x-1], gTruth[x-1]))
    plot_vergleich.plot(x1, y1, x2, radarY, x2 , kFilterY)
    plot_vergleich.legend(["GroundTruth", "Radar Abweichung", "Kalman Prediction Abweichung"])

def constAccKalman(i, t, radaType, x, y):
    if radaType == 0:
        position = cart_coord(i)
    else:
        position = polar_RadarPunkt(i, x, y)
    velocity = calcVelocity(i)
    accerleration = calcAcceleration(i)
    nextPosX = position[0] + (t*velocity[0]) + (0.5 * t**2 * accerleration[0])
    nextPosY = position[1] + (t*velocity[1]) + (0.5 * t * accerleration[1])
    nextVelX = velocity[0] + (t* accerleration[0])
    nextVelY = velocity[1] + (t* accerleration[1])
    #geben nur die zukünftige Position aus, also i+t
    return[nextPosX, nextPosY]
    

def clear(x, y, xOld, yOld):
    if x > 0 and y > 0 and xOld < 0 and yOld < 0 :
        axesPosition.cla()
        axesVelocity.cla()
        axesAcceleration.cla()
        plottangent.cla()
        plotnormal.cla()

        setAxesSize()


def arrow(xPosition, yPosition, xVelocity, yVelocity, xAcceleration, yAcceleration):
    # P.arrow( x, y, dx, dy, **kwargs )
    axesAccelerationArrow.cla()
    axesPositionArrow.cla()
    axesVelocityArrow.cla()
    setAxesSize()
    axesPositionArrow.arrow( 0, 0, xPosition, yPosition, fc="k", ec="k",
    head_width=200, head_length=300 )
    axesVelocityArrow.arrow( 0, 0, xVelocity, yVelocity, fc="k", ec="k",
    head_width=5, head_length=15 )
    axesAccelerationArrow.arrow( 0, 0, xAcceleration, yAcceleration, fc="k", ec="k",
    head_width=0.2, head_length=0.6 )


main()