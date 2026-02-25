4
import matplotlib.pyplot as plt

# Take user input for data
data_input = input("Enter numbers separated by commas: ")

# Convert string input to list of floats
data = list(map(float, data_input.split(",")))

# Take user input for number of bins
bins = int(input("Enter number of bins: "))

# Create histogram
plt.hist(data, bins=bins, color='orange', edgecolor='black')

# Add title and labels
plt.title("Dynamic Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display histogram
plt.show()
