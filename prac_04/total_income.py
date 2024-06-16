"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display monthly_income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        monthly_income = float(input(f"Enter income for a month {month}:"))
        incomes.append(monthly_income)

    report(number_of_months, incomes)


#This function will print report
def report(number_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        monthly_income = incomes[month - 1]
        total += monthly_income
        print("Month {:2} - Income: ${:,.2f} Total: ${:,.2f}".format(month, monthly_income, total))


main()
