balance = 3926
annualInterestRate = 0.2

paid_amount = 10


def debt_calculator(months):

    if months == 1:

        unpaid_balance = balance - paid_amount
        #print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)

    else:
        new_balance = debt_calculator(months-1)
        unpaid_balance = new_balance - paid_amount
        #print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)


unpaid_balance = debt_calculator(12)

while not unpaid_balance <= 0:
    paid_amount += 10
    unpaid_balance = debt_calculator(12)

print(f"Lowest Payment: ", paid_amount)
