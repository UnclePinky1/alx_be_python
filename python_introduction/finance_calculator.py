monthly_income = float(input("enter your monthly income: $ "))
monthly_expenses = float(input("Enter your total monthly expenses: $ "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with interest are: ${annual_savings:.2f}")