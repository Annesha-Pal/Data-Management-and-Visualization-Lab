import matplotlib.pyplot as plt

# --- User input for categories ---
categories_input = input("Enter categories separated by commas: ")
categories = [cat.strip() for cat in categories_input.split(",")]

# --- User input for values ---
values_input = input(f"Enter values for {len(categories)} categories separated by commas: ")
values = [float(val.strip()) for val in values_input.split(",")]

# --- Check if lengths match ---
if len(categories) != len(values):
    print("Error: Number of categories and values must be the same.")
else:
    # --- Draw bar chart ---
    plt.bar(categories, values, color='skyblue')
    plt.title("Dynamic Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
