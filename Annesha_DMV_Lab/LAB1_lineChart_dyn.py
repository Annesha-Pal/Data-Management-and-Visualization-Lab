import matplotlib.pyplot as plt

# Take user input
x_input = input("Enter X values separated by commas: ")
y_input = input("Enter Y values separated by commas: ")

# Convert input strings to lists of numbers
x = list(map(float, x_input.split(",")))
y = list(map(float, y_input.split(",")))

# Check if lengths match
if len(x) != len(y):
    print("Error: X and Y must have the same number of values.")
else:
    # Plot the line chart
    plt.plot(x, y, marker='o', linestyle='-', color='green')
    plt.title("Dynamic Line Chart (User Input)")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()
