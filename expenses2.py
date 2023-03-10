import tkinter as tk

root = tk.Tk() # This creates the main window of the tkinter application
total_expenses_label = tk.Label(root, text="Total Expenses: $0.00")
total_expenses_label.pack()

root.mainloop() # This runs the Tkinter event loop which handles user input and updates the GUI

# create a Tkinter window
window = tk.Tk()
window.title("Budget Tracker")

# create input fields for income, expenses, and savings
income_label = tk.Label(window, text="Income:")
income_label.grid(row=0, column=0)
income_entry = tk.Entry(window)
income_entry.grid(row=0, column=1)

cash_label = tk.Label(window, text="Cash (Pocket cash):")
cash_label.grid(row=1, column=0)
cash_entry = tk.Entry(window)
cash_entry.grid(row=1, column=1)

car_payment1_label = tk.Label(window, text="Car payment 1:")
car_payment1_label.grid(row=2, column=0)
car_payment1_entry = tk.Entry(window)
car_payment1_entry.grid(row=2, column=1)

car_payment2_label = tk.Label(window, text="Car payment 2:")
car_payment2_label.grid(row=3, column=0)
car_payment2_entry = tk.Entry(window)
car_payment2_entry.grid(row=3, column=1)

car_insurance_label = tk.Label(window, text="Car insurance:")
car_insurance_label.grid(row=4, column=0)
car_insurance_entry = tk.Entry(window)
car_insurance_entry.grid(row=4, column=1)

electricity_heating_label = tk.Label(window, text="Electricity/Heating:")
electricity_heating_label.grid(row=5, column=0)
electricity_heating_entry = tk.Entry(window)
electricity_heating_entry.grid(row=5, column=1)

mortgage_label = tk.Label(window, text="Mortgage:")
mortgage_label.grid(row=6, column=0)
mortgage_entry = tk.Entry(window)
mortgage_entry.grid(row=6, column=1)

medical_insurance_label = tk.Label(window, text="Medical insurance:")
medical_insurance_label.grid(row=7, column=0)
medical_insurance_entry = tk.Entry(window)
medical_insurance_entry.grid(row=7, column=1)

water_label = tk.Label(window, text="Water:")
water_label.grid(row=8, column=0)
water_entry = tk.Entry(window)
water_entry.grid(row=8, column=1)

landscaping_label = tk.Label(window, text="Landscaping:")
landscaping_label.grid(row=9, column=0)
landscaping_entry = tk.Entry(window)
landscaping_entry.grid(row=9, column=1)

gas_label = tk.Label(window, text="Gas:")
gas_label.grid(row=10, column=0)
gas_entry = tk.Entry(window)
gas_entry.grid(row=10, column=1)

groceries_label = tk.Label(window, text="Groceries:")
groceries_label.grid(row=11, column=0)
groceries_entry = tk.Entry(window)
groceries_entry.grid(row=11, column=1)

# create buttons to add and remove items
add_button = tk.Button(window, text="Add")
add_button.grid(row=12, column=0)

remove_button = tk.Button(window, text="Remove")
remove_button.grid(row=12, column=1)

# create a label to display the budget information
budget_label = tk.Label(window, text="")
budget_label.grid(row=13, column=0, columnspan=2)

# create a function to update the budget information
def update_budget():
    # Get the current values from the input fields
    income = float(income_entry.get())
    cash = float(cash_entry.get())
    car_payment1 = float(car_payment1_entry.get())
    car_payment2 = float(car_payment2_entry.get())
    car_insurance = float(car_insurance_entry.get())
    electricity_heating = float(electricity_heating_entry.get())
    mortgage = float(mortgage_entry.get())
    medical_insurance = float(medical_insurance_entry.get())
    water = float(water_entry.get())
    landscaping = float(landscaping_entry.get())
    gas = float(gas_entry.get())
    groceries = float(groceries_entry.get())
    
    # Calculate total expenses
    total_expenses = cash + car_payment1 + car_payment2 + car_insurance + electricity_heating + mortgage + medical_insurance + water + landscaping + gas + groceries
    

    calculation_var = tk.StringVar()
    calculation = calculation_var.get()


    # Calculate net income
    if calculation_var.get() == "Monthly":
        net_income = income - total_expenses
    elif calculation_var.get() == "Yearly":
        net_income = (income - total_expenses) * 12
        
    # Update the labels with the new information
    total_expenses_label.config(text="Total Expenses: $%.2f" % total_expenses)
    net_income_label.config(text="Net Income: $%.2f" % net_income)

    # Create the labels to display the total expenses and net income
total_expenses_label = tk.Label(root, text="Total Expenses: $0.00")
total_expenses_label.pack()

# Create the labels to display the total expenses and net income
net_income_label = tk.Label(root, text="Total Expenses: $0.00")
net_income_label.pack()