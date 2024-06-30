def calculate_savings():
    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return

    savings_goal = 10000
    current_savings = 0
    months = 0

    while current_savings < savings_goal:
        current_savings += (monthly_income - monthly_expenses)
        months += 1

    print(f"You'll reach $10,000 in savings after {months} months.")

if __name__ == "__main__":
    calculate_savings()
