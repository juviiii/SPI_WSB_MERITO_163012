import matplotlib.pyplot as plt

def calculate_savings():
    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return

    savings_goal = 10000
    current_savings = 0
    months = []
    savings_history = []

    while current_savings < savings_goal:
        current_savings += (monthly_income - monthly_expenses)
        months.append(len(months) + 1)  # Track the month number
        savings_history.append(current_savings)

    print(f"You'll reach $10,000 in savings after {len(months)} months.")

    # Plot the savings history
    plt.plot(months, savings_history, marker='o')
    plt.xlabel("Months")
    plt.ylabel("Savings ($)")
    plt.title("Monthly Savings Progress")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    calculate_savings()
