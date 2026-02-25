import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Moving Circle Animation")

# Create circle
circle = plt.Circle((1, 5), 0.5, color='red')
ax.add_patch(circle)

# Update function (moves circle to the right)
def move(frame):
    circle.center = (1 + frame * 0.1, 5)
    return circle,

# Animate
animation = FuncAnimation(fig, move, frames=80, interval=50)

plt.grid(True)  # Show grid with axes
plt.show()
