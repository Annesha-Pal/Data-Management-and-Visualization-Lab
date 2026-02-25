import matplotlib.pyplot as plt

# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Create scatter plot
plt.scatter(x, y, color='green', marker='o', s=100)  # s = size of points

# Add title and labels
plt.title("Static Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)
plt.show()
