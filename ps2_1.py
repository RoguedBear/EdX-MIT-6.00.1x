balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 10

def debt_calculator(months):
    global balance
    if months == 1:
        paid_amount = monthlyPaymentRate * balance
        unpaid_balance = balance - paid_amount
        print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)

    else:
        balance = debt_calculator(months-1)
        unpaid_balance = balance - (monthlyPaymentRate * balance)
        print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)

print(debt_calculator(12))
