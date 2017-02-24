initial_deposit = int(input('Enter your initial deposit: ' ))
total_cost = 1000000
epsilon = 100
portion_down_payment = 0.25 * total_cost
number_of_years=3
steps=0

def current_savings_guess(r):
    current_savings = initial_deposit*(1+r/12)**(number_of_years*12)
    return float(format(current_savings, '.2f'))
maximun_savings = current_savings_guess(1)
if maximun_savings > portion_down_payment:
    if initial_deposit < portion_down_payment: 
        low = 0
        high = 10000
        guess = int((high + low)/2.0)
        while abs(current_savings_guess(guess/10000) - portion_down_payment) > epsilon:
            if current_savings_guess(guess/10000) < portion_down_payment:
                low = guess
            else:
                high = guess
            guess = int((high + low)/2.0)
            steps += 1
        best_r = guess
    else:
        best_r = 0
       
    print('Best savings rate: ', best_r/10000)
    print('steps in bisection search: ',steps)
else:
    best_r = 'no r possible'
    steps = 'no r possible'
    print('It is not possible to pay the down payment in three years.')
    print('Best savings rate: ', best_r)
    print('steps in bisection search: ',steps)
