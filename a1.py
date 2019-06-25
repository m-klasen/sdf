import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.gridspec import  GridSpec
from functions import *

pos_list= []
vel_list= []
acc_list= []
ncols = 6
nrows = 4
grid = GridSpec(nrows, ncols,left=0.1, bottom=0.15, right=0.94, top=0.94, wspace=1, hspace=1)

#Figure 0
fig = plt.figure(0)
axesPosition = fig.add_subplot(grid[0:2, 0:2])
axesPositionArrow = fig.add_subplot(grid[2:4, 0:2])
axesVelocity = fig.add_subplot(grid[0:2, 2:4])
axesVelocityArrow = fig.add_subplot(grid[2:4, 2:4])
axesAcceleration = fig.add_subplot(grid[0:2, 4:6])
axesAccelerationArrow = fig.add_subplot(grid[2:4, 4:6])

pos = axesPosition.scatter([], [], c="r")
ground_pos = axesPosition.plot([calcPosition(i)[0] for i in range(0,1000)],[calcPosition(i)[1] for i in range(0,1000)],c="b")

veloc = axesVelocity.scatter([], [], c="r")
ground_vel = axesVelocity.plot([calcVelocity(i)[0] for i in range(0,1000)],[calcVelocity(i)[1] for i in range(0,1000)],c="b")

accel = axesAcceleration.scatter([], [], c="r")
ground_vel = axesAcceleration.plot([calcAcceleration(i)[0] for i in range(0,1000)],[calcAcceleration(i)[1] for i in range(0,1000)],c="b")

#Figure 1
ax = plt.figure(1)
plottangent = ax.add_subplot(grid[0:2, 0:2])
plotnormal = ax.add_subplot(grid[0:2, 2:4])
plot_absvelo = ax.add_subplot(grid[0:2,4:6])
plot_absaccel = ax.add_subplot(grid[2:4,0:2])
plot_acceltangent = ax.add_subplot(grid[2:4,2:4])
plot_accelnormal = ax.add_subplot(grid[2:4,4:6])

tang=plottangent.scatter([],[])
norm=plotnormal.scatter([],[])

absvel=plot_absvelo.scatter([],[])
absacc=plot_absaccel.scatter([],[])
acctang=plot_acceltangent.scatter([],[])
accnorm=plot_accelnormal.scatter([],[])
def main():
    setAxesSize()
    ani2 = animation.FuncAnimation(ax, update_plot2, interval=25,blit=True)
    ani = animation.FuncAnimation(fig, update_plot, interval=25,blit=True)
    plt.show()

def setAxesSize():
    axesPosition.set_ylim(-1500, 1500)
    axesPosition.set_xlim(-1500, 1500)
    axesPosition.set_title('Position')

    axesVelocity.set_ylim(-40, 40)
    axesVelocity.set_xlim(-30, 30)
    axesVelocity.set_title('Velocity')

    axesAcceleration.set_ylim(-1, 1)
    axesAcceleration.set_xlim(-0.5, 0.5)
    axesAcceleration.set_title('Acceleration')

    axesPositionArrow.set_ylim(-25, 25)
    axesPositionArrow.set_xlim(-25, 25)


    axesVelocityArrow.set_ylim(-1.2, 1.2)
    axesVelocityArrow.set_xlim(-1.0, 1.0)

    axesAccelerationArrow.set_ylim(-0.5, 0.5)
    axesAccelerationArrow.set_xlim(-0.5, 0.5)

    plottangent.axis([-1.5, 1.5, -1.5, 1.5])
    plottangent.set_title('Tangent')
    plotnormal.axis([-1.5, 1.5, -1.5, 1.5])
    plotnormal.set_title('Normale')
    plot_absvelo.axis([0,30, 0, 30])
    plot_absvelo.set_title('Abs. Velocity')
    plot_absaccel.axis([0,1, 0, 1])
    plot_absaccel.set_title('Abs. Accel.')
    plot_acceltangent.axis([-0.3, 0.3, -1, 1])
    plot_acceltangent.set_title('Accel. Tangent')
    plot_accelnormal.axis([-0.3, 0.3, -1, 1])
    plot_accelnormal.set_title('Accel. Normale')

def update_plot(i):

    pos_list.append(calcPosition(i))
    vel_list.append(calcVelocity(i))
    acc_list.append(calcAcceleration(i))

    if i == 0:
        patch1 = plt.Arrow(0, 0, pos_list[-1][0], pos_list[-1][1])
        patch2 = plt.Arrow(0, 0, vel_list[-1][0], vel_list[-1][0])
        patch3 = plt.Arrow(0, 0, acc_list[-1][0], acc_list[-1][1])
        axesPositionArrow.add_patch(patch1)
        axesVelocityArrow.add_patch(patch2)
        axesAccelerationArrow.add_patch(patch3)
    else:
        xDifPos = pos_list[-1][0] - pos_list[-2][0]
        yDifPos = pos_list[-1][1] - pos_list[-2][1]

        xDifVel =  vel_list[-1][0] - vel_list[-2][0]
        yDifVel =  vel_list[-1][1] - vel_list[-2][1] 

        xDifAcc = acc_list[-1][0] - acc_list[-2][0]
        yDifAcc = acc_list[-1][1] - acc_list[-2][1]

        patch1 = plt.Arrow(0, 0, xDifPos,yDifPos)
        patch2 = plt.Arrow(0, 0, xDifVel,yDifVel)
        patch3 = plt.Arrow(0, 0, xDifAcc,yDifAcc)
        axesPositionArrow.add_patch(patch1)
        axesVelocityArrow.add_patch(patch2)
        axesAccelerationArrow.add_patch(patch3)

    temp = np.c_[np.array(calcPosition(i)).T[0], np.array(calcPosition(i)).T[1]]
    temp2 = np.c_[np.array(calcVelocity(i)).T[0], np.array(calcVelocity(i)).T[1]]
    temp3 = np.c_[np.array(calcAcceleration(i)).T[0], np.array(calcAcceleration(i)).T[1]]
    pos.set_offsets(temp)
    veloc.set_offsets(temp2)
    accel.set_offsets(temp3)
    return pos,veloc,accel,patch1,patch2,patch3

def update_plot2(i):
    tang.set_offsets(np.c_[np.array(calc_tangent(i)).T[0], np.array(calc_tangent(i)).T[1]])
    norm.set_offsets(np.c_[np.array(calc_normal(i)).T[0], np.array(calc_normal(i)).T[1]])
    absvel.set_offsets(np.c_[abs_velo(i), np.array(i)])
    plot_absvelo.set_ylim(i-20,i+20)
    absacc.set_offsets(np.c_[np.array(abs_accel(i)), np.array(i)])
    plot_absaccel.set_ylim(i-20,i+20)
    acctang.set_offsets(np.c_[np.array(accel_tangent(i)).T[0], np.array(accel_tangent(i)).T[1]])
    accnorm.set_offsets(np.c_[np.array(accel_normal(i)).T[0], np.array(accel_normal(i)).T[1]])
    return tang,norm,absvel,absacc,acctang,accnorm

main()