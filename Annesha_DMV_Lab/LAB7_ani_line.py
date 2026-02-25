import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Animated Line")

# Empty line
line, = ax.plot([], [], color='blue')

# Data lists
x_data = []
y_data = []

# Update function
def update(frame):
    x_data.append(frame)
    y_data.append(frame)   # Line y = x (diagonal line)
    line.set_data(x_data, y_data)
    return line,

# Animate
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)

plt.grid(True)
plt.show()
