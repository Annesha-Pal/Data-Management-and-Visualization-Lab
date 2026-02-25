import matplotlib.pyplot as plt

# Get user input for X values
x_input = input("Enter X values separated by commas: ")
x = [float(i.strip()) for i in x_input.split(",")]

# Get user input for Y values
y_input = input("Enter Y values separated by commas: ")
y = [float(i.strip()) for i in y_input.split(",")]

# Check if lengths match
if len(x) != len(y):
    print("Error: X and Y must have the same number of values.")
else:
    # Create scatter plot
    plt.scatter(x, y, color='blue', marker='o', s=100)
    plt.title("Dynamic Scatter Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()
