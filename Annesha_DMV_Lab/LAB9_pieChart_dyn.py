import matplotlib.pyplot as plt

# Get user input for labels
labels_input = input("Enter labels separated by commas: ")
labels = [label.strip() for label in labels_input.split(",")]

# Get user input for values
values_input = input("Enter values separated by commas: ")
values = [float(val.strip()) for val in values_input.split(",")]

# Optional: check if lengths match
if len(labels) != len(values):
    print("Error: Number of labels and values must be the same.")
else:
    # Draw pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Make it circular
    plt.title("Dynamic Pie Chart")
    plt.show()
