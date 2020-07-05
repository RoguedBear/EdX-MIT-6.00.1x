cache = {}

def cache_manager(paying_amount):
    if paying_amount not in cache.keys():
        cache[paying_amount] = debt_calculator(paying_amount, 12)
        return cache[paying_amount]
    else:
        global cache_returned

        return cache[paying_amount]


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


balance = 99999999999
annualInterestRate = 0.18

epsilon = 0.1
lower_bound = balance / 12
upper_bound = (balance * (1+ (annualInterestRate / 12))**12)/12
unpaid_balance = 0


while  not upper_bound - lower_bound <= epsilon:
    paid_amount = round((lower_bound + upper_bound) / 2, 2)
    unpaid_balance = cache_manager(paid_amount)
    #print(f"Lower Bound and payment: {lower_bound:.2f}, {cache_manager(lower_bound):.2f} \t Upper Boune w/ payment: {upper_bound:.2f}, {debt_calculator(upper_bound, 12):.2f}")
    #print(f"Mid: {paid_amount}, {unpaid_balance:.2f}")

    if unpaid_balance > epsilon:
        lower_bound = paid_amount

    elif unpaid_balance < epsilon:
        upper_bound = paid_amount
    #print(paid_amount)
print("Lowest Payment: {}".format(round(paid_amount, 2)))
