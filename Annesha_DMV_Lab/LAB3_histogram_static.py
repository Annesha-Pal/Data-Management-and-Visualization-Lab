import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 13, 17, 19, 21, 22, 25, 27, 30, 14, 16, 18, 20, 24]

# Create histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

# Add title and labels
plt.title("Static Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
