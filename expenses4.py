import tkinter as tk

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

# create a drop-down menu to choose monthly or yearly calculations
calculation_label = tk.Label(window, text="Calculation:")
calculation_label.grid(row=12, column=0)
calculation_var = tk.StringVar()
calculation_dropdown = tk.OptionMenu(window, calculation_var, "Monthly", "Yearly")
calculation_dropdown.grid(row=12, column=1)

# create buttons to add and remove items
def add_item():
    pass

add_button = tk.Button(window, text="Add", command=add_item)
add_button.grid(row=13, column=0)

def remove_item():
    pass

remove_button = tk.Button(window, text="Remove", command=remove_item)
remove_button.grid(row=13, column
# create table for budget items and total
budget_table = tk.LabelFrame(window, text="Budget Table")
budget_table.grid(row=14, column=0, columnspan=2)
budget_items = tk.Label(budget_table, text="Budget Items")
budget_items.grid(row=0, column=0)
budget_amounts = tk.Label(budget_table, text="Amounts")
budget_amounts.grid(row=0, column=1)
income_label = tk.Label(budget_table, text="Income:")
income_label.grid(row=1, column=0)
income_amount = tk.Label(budget_table, text="0")
income_amount.grid(row=1, column=1)
cash_label = tk.Label(budget_table, text="Cash (Pocket cash):")
cash_label.grid(row=2, column=0)
cash_amount = tk.Label(budget_table, text="0")
cash_amount.grid(row=2, column=1)
car_payment1_label = tk.Label(budget_table, text="Car payment 1:")
car_payment1_label.grid(row=3, column=0)
car_payment1_amount = tk.Label(budget_table, text="0")
car_payment1_amount.grid(row=3, column=1)
car_payment2_label = tk.Label(budget_table, text="Car payment 2:")
car_payment2_label.grid(row=4, column=0)
car_payment2_amount = tk.Label(budget_table, text="0")
car_payment2_amount.grid(row=4, column=1)
car_insurance_label = tk.Label(budget_table, text="Car insurance:")
car_insurance_label.grid(row=5, column=0)
car_insurance_amount = tk.Label(budget_table, text="0")
car_insurance_amount.grid(row=5, column=1)
electricity_heating_label = tk.Label(budget_table, text="Electricity/Heating:")
electricity_heating_label.grid(row=6, column=0)
electricity_heating_amount = tk.Label(budget_table, text="0")
electricity_heating_amount.grid(row=6, column=1)
mortgage_label = tk.Label(budget_table, text="Mortgage:")
mortgage_label.grid(row=7, column=0)
mortgage_amount = tk.Label(budget_table, text="0")
mortgage_amount.grid(row=7, column=1)
medical_insurance_label = tk.Label(budget_table, text="Medical insurance:")
medical_insurance_label.grid(row=8, column=0)
medical_insurance_amount = tk.Label(budget_table, text="0")
medical_insurance_amount.grid(row=8, column=1)
water_label = tk.Label(budget_table, text="Water:")
water_label.grid(row=9, column=0)
water_amount = tk.Label(budget_table, text="0")
water_amount.grid(row=9, column=1)
landscaping_label = tk.Label(budget_table, text="Landscaping:")
landscaping_label.grid(row=10, column=0)
landscaping_amount = tk.Label(budget_table, text="0")
landscaping_amount.grid(row=10, column=1)
gas_label = tk.Label(budget_table, text="Gas:")
gas_label.grid(row=11, column=0)
gas_amount = tk.Label(budget_table, text="0")
gas_amount.grid(row=11, column=1)
groceries_label = tk.Label(budget_table, text="Groceries:")
groceries_label.grid(row=12, column=0)
groceries_amount = tk.Label(budget_table, text="0")
groceries_amount.grid(row=12, column=1)
total_label = tk.Label
