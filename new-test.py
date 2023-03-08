# Import the necessary modules
import tkinter as tk

# Create a function to calculate the total expenses and net income
def calculate_net_income():
    # Get the values from the input fields
    income = float(income_entry.get())
    expenses = float(expenses_entry.get())

    # Calculate the total expenses and net income
    total_expenses = expenses
    net_income = income - total_expenses

    # Update the labels with the new information
    total_expenses_label.config(text="Total Expenses: $%.2f" % total_expenses)
    net_income_label.config(text="Net Income: $%.2f" % net_income)

# Create the main window
root = tk.Tk()

# Create the input fields
income_entry_label = tk.Label(root, text="Income:")
income_entry_label.pack()
income_entry = tk.Entry(root)
income_entry.pack()

expenses_entry_label = tk.Label(root, text="Expenses:")
expenses_entry_label.pack()
expenses_entry = tk.Entry(root)
expenses_entry.pack()

# Create the button to calculate the net income
calculate_button = tk.Button(root, text="Calculate", command=calculate_net_income)
calculate_button.pack()

# Create the labels to display the total expenses and net income
total_expenses_label = tk.Label(root, text="Total Expenses: $0.00")
total_expenses_label.pack()

net_income_label = tk.Label(root, text="Net Income: $0.00")
net_income_label.pack()

# Run the main loop
root.mainloop()
