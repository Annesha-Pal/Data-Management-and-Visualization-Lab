import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
bar_values = [10, 15, 7, 12]

scatter_x = [1, 2, 3, 4, 5]
scatter_y = [5, 10, 7, 12, 9]

# Create figure with 2 subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# --- Bar chart subplot ---
ax1.bar(categories, bar_values, color='skyblue')
ax1.set_title("Bar Chart")
ax1.set_ylabel("Values")
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# --- Scatter plot subplot ---
ax2.scatter(scatter_x, scatter_y, color='red', s=100)
ax2.set_title("Scatter Plot")
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y Axis")
ax2.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
