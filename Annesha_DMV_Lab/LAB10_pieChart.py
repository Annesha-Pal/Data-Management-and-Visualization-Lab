import matplotlib.pyplot as plt

# Sample data
labels = ['Apples', 'Bananas', 'Cherries', 'Guava']
sizes = [25, 30, 20, 25]  # Percentages or values
colors = ['red', 'yellow', 'pink', 'green']

# Draw pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Make the pie chart a circle
plt.axis('equal')

plt.title("Fruit Distribution")
plt.show()
