import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import  GridSpec
from functions import *


ncols = 6
nrows = 4
grid = GridSpec(nrows, ncols,
                left=0.1, bottom=0.15, right=0.94, top=0.94, wspace=1, hspace=1)

fig = plt.figure(0)
fig.clf()

# Add axes which can span multiple grid boxes
axesPosition = fig.add_subplot(grid[0:2, 0:2])
axesPositionArrow = fig.add_subplot(grid[2:4, 0:2])

axesVelocity = fig.add_subplot(grid[0:2, 2:4])
axesVelocityArrow = fig.add_subplot(grid[2:4, 2:4])

axesAcceleration = fig.add_subplot(grid[0:2, 4:6])
axesAccelerationArrow = fig.add_subplot(grid[2:4, 4:6])

ax = plt.figure(1)

plottangent = ax.add_subplot(grid[0:2, 0:2])
plotnormal = ax.add_subplot(grid[0:2, 2:4])

plot_absvelo = ax.add_subplot(grid[0:2,4:6])
plot_absaccel = ax.add_subplot(grid[2:4,0:2])
plot_acceltangent = ax.add_subplot(grid[2:4,2:4])
plot_accelnormal = ax.add_subplot(grid[2:4,4:6])

def main():
    ani = animation.FuncAnimation(fig, update_plot, interval=1, frames=300)

    ani2 = animation.FuncAnimation(ax, update_plot2, interval=1, frames=300)

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



setAxesSize()
main()