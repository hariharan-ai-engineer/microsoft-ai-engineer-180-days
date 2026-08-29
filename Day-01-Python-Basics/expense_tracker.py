# Day 1 - Real World Python Project
# Simple Expense Tracker

monthly_budget = float(input("Enter your monthly budget: "))

food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))

total_expense = food + travel + shopping
remaining_balance = monthly_budget - total_expense

print("\n----- EXPENSE REPORT -----")
print("Monthly Budget:", monthly_budget)
print("Total Expense:", total_expense)
print("Remaining Balance:", remaining_balance)
