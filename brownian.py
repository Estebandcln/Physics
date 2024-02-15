import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


n_steps = 1000
dt = 0.01
D = 1.0
"""
x = 0.0
y = 0.0
a = 0.0
b = 0.0
a1 = 0.0
b1 = 0.0

fig, ax = plt.subplots(facecolor='black')
line, = ax.plot([], [], lw=2, c='#fcfce8')
line2, = ax.plot([], [], lw=2, c='#ededaf')
line3, = ax.plot([], [], lw=2, c='#ffff00')

def update(i):
    global x, y, a, b, a1, b1
    dx = np.sqrt(2*D*dt)*np.random.randn()
    dy = np.sqrt(2*D*dt)*np.random.randn()
    da = np.sqrt(2*D*dt)*np.random.randn()
    db = np.sqrt(2*D*dt)*np.random.randn()
    da1 = np.sqrt(2*D*dt)*np.random.randn()
    db1 = np.sqrt(2*D*dt)*np.random.randn()
    x += dx
    y += dy
    a += da
    b += db
    a1 += da1
    b1 += db1
    line.set_data(np.append(line.get_xdata(), x), np.append(line.get_ydata(), y))
    line2.set_data(np.append(line2.get_xdata(), a), np.append(line2.get_ydata(), b))
    line3.set_data(np.append(line3.get_xdata(), a1), np.append(line3.get_ydata(), b1))
    ax.relim()
    ax.autoscale_view(True,True,True)
    return line, line2, line3,

ax.set_axis_off()
ani = animation.FuncAnimation(fig, update, frames=30, interval=25, blit=True)
#ani.save('brownian.gif', writer='imagemagick', fps=60)
plt.show()
"""

"""

a = 0.0
b = 0.0
a1 = 0.0
b1 = 0.0

fig, ax = plt.subplots(facecolor='black')
line, = ax.plot([], [], lw=2, c='#c9843a')

def update(i):
    global a, b, a1, b1

    da = np.sqrt(2*D*dt)*np.random.randn()
    db = np.sqrt(2*D*dt)*np.random.randn()
    da1 = np.sqrt(2*D*dt)*np.random.randn()
    db1 = np.sqrt(2*D*dt)*np.random.randn()

    a += da
    b += db
    a1 += da1
    b1 += db1
    line.set_data(np.append(line.get_xdata(), a), np.append(line.get_ydata(), b))
    line.set_data(np.append(line.get_xdata(), a1), np.append(line.get_ydata(), b1))
    ax.relim()
    ax.autoscale_view(True,True,True)
    return line,

ax.set_axis_off()
ani = animation.FuncAnimation(fig, update, frames=int(n_steps/100), interval=25, blit=True)
#ani.save('b1.gif', writer='imagemagick', fps=60, savefig_kwargs={'facecolor': 'black'})
#ani.save('brownian.gif', writer='imagemagick', fps=60)
plt.show()

"""

a = 0.0
b = 0.0

fig, ax = plt.subplots(facecolor='black')
line, = ax.plot([], [], lw=2, c='#c9843a')

def update(i):
    global a, b, a1, b1

    da = np.sqrt(2*D*dt)*np.random.randn()
    db = np.sqrt(2*D*dt)*np.random.randn()

    a += da
    b += db
    line.set_data(np.append(line.get_xdata(), a), np.append(line.get_ydata(), b))
    ax.relim()
    ax.autoscale_view(True,True,True)
    return line,

ax.set_axis_off()
ani = animation.FuncAnimation(fig, update, frames=int(n_steps/100), interval=25, blit=True)
#ani.save('b1.gif', writer='imagemagick', fps=60, savefig_kwargs={'facecolor': 'black'})
#ani.save('brownian.gif', writer='imagemagick', fps=60)
plt.show()

