import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 18]

# Create the line chart
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add title and labels
plt.title("Simple Static Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show grid
plt.grid(True)

# Display the chart
plt.show()
