import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title("Static Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display chart
plt.show()
