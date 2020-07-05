def debt_calculator(paid_amount, months):

    if months == 1:

        unpaid_balance = balance - paid_amount
        #print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)

    else:
        new_balance = debt_calculator(paid_amount, months-1)
        unpaid_balance = new_balance - paid_amount
        #print(f"Month {months} Remaining balance: {unpaid_balance + (annualInterestRate / 12 * unpaid_balance):.2f}")
        return unpaid_balance + (annualInterestRate / 12 * unpaid_balance)

balance = 320000
annualInterestRate = 0.2

lower_bound = balance / 12
upper_bound = (balance * (1+ (annualInterestRate / 12))**12)/12
paid_amount = round((lower_bound + upper_bound) / 2, 2)

print(f"Lower Bound: {lower_bound:.2f}, {debt_calculator(lower_bound, 12):.2f}\tUpper Bound: {upper_bound:.2f}, {debt_calculator(upper_bound, 12):.2f}\nMid: {paid_amount:.2f}, {debt_calculator(paid_amount, 12):.2f}")
