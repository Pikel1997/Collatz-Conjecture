import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)


def animation_frame(i):
	x_data.append(i * 10)
	y_data.append(i)

	line.set_xdata(x_data)
	line.set_ydata(y_data)
	return line,


animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.1), interval=10)
animation_frame()
plt.show()
