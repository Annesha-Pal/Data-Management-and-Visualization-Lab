import matplotlib.pyplot as plt

# Take number of points
n = int(input("How many data points? "))

x = []
y = []

# Take input for each point
for i in range(n):
    x_val = float(input(f"Enter X value {i+1}: "))
    y_val = float(input(f"Enter Y value {i+1}: "))
    x.append(x_val)
    y.append(y_val)

# Plot the line graph
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add labels and title
plt.title("Line Graph (User Input)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)
plt.show()
