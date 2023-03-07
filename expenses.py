import tkinter as tk

# create a Tkinter window
window = tk.Tk()
window.title("Budget Tracker")

# create input fields for income, expenses, and savings
income_label = tk.Label(window, text="Income:")
income_label.grid(row=0, column=0)
income_entry = tk.Entry(window)
income_entry.grid(row=0, column=1)

expenses_label = tk.Label(window, text="Expenses:")
expenses_label.grid(row=1, column=0)
expenses_entry = tk.Entry(window)
expenses_entry.grid(row=1, column=1)

savings_label = tk.Label(window, text="Savings:")
savings_label.grid(row=2, column=0)
savings_entry = tk.Entry(window)
savings_entry.grid(row=2, column=1)

# create buttons to add and remove items
add_button = tk.Button(window, text="Add")
add_button.grid(row=3, column=0)

remove_button = tk.Button(window, text="Remove")
remove_button.grid(row=3, column=1)

# create a label to display the budget information
budget_label = tk.Label(window, text="")
budget_label.grid(row=4, column=0, columnspan=2)

# create a function to update the budget information
def update_budget():
    # retrieve data from input fields
    income = float(income_entry.get())
    expenses = float(expenses_entry.get())
    savings = float(savings_entry.get())

    # calculate total income, expenses, and savings
    total_income = income
    total_expenses = expenses
    total_savings = savings

    # update the budget label with the new data
    budget_label.config(text="Total Income: $%.2f\nTotal Expenses: $%.2f\nTotal Savings: $%.2f" % (total_income, total_expenses, total_savings))

# assign the update_budget function to the add button
add_button.config(command=update_budget)

# run the Tkinter event loop
window.mainloop()
