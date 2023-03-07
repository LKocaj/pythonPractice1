# initialize empty dictionaries for income, expenses, and savings
income = {}
expenses = {}
savings = {}

# prompt user for income data
income['salary'] = float(input("Enter your salary: "))
income['bonus'] = float(input("Enter any bonuses you received: "))

# prompt user for expense data
expenses['rent'] = float(input("Enter your monthly rent: "))
expenses['utilities'] = float(input("Enter your monthly utilities: "))
expenses['groceries'] = float(input("Enter your monthly groceries: "))

# calculate total income, expenses, and savings
total_income = sum(income.values())
total_expenses = sum(expenses.values())
total_savings = total_income - total_expenses

# display budget information to user
print("Your Budget Information:")
print("------------------------")
print("Total Income: $%.2f" % total_income)
print("Total Expenses: $%.2f" % total_expenses)
print("Total Savings: $%.2f" % total_savings)
