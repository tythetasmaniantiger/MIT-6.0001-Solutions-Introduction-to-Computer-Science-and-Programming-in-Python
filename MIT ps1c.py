"""
Created on Thu Jan 27 02:10:31 2022

@author: tythetasmaniantiger
"""
## PS1 Part C: Finding the right amount to save away

import statistics as stat


# Variables

starting_salary = float(input("Enter Starting Salary:"))
semi_annual_raise = .07
total_cost = 1000000
portion_down_payment = 0.25
r = 0.04   #Annual rate of return
months = 36


# Savings Function

down_payment_cost = total_cost * portion_down_payment

def remaining_cost(portion_saved):
    '''
    Parameters
    ----------
    portion_saved : float, the ratio of annual salary saved towards down payment,
                between 0 and 1

    Returns
    -------
    difference: float, the difference between down_payment_cost and current_savings
    after 36 months
    '''
    monthly_savings = (starting_salary/12) * portion_saved
    current_savings = 0
    for k in range(months):
        salary_adjustment = (1 + semi_annual_raise) ** (k//6)
        current_savings += current_savings * r/12 + monthly_savings * salary_adjustment
        
    difference = down_payment_cost - current_savings
    return(difference)


# Bisection Search

a = 1; b = 10000  #starting_bounds
for n in range(a,b):
    guess = (stat.mean([a,b]))/10000
    if abs(remaining_cost(guess))<100 or n > 100:
        break
    elif remaining_cost(guess) > 0:
        a = (a+b) / 2
    else: 
        b = (a+b) / 2

if n >= 100:
    print("It is not possible to pay the down payment in three years.")
else:
    guess = round(guess,4)
    print("Best savings ate:",guess)
    print("Steps in bisection search:",n)



