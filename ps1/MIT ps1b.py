"""
Created on Thu Jan 27 00:34:04 2022

@author: tythetasmaniantiger
"""
 
## PS1 Part B: Semi-Annual Raise


# Variables

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))
portion_down_payment = 0.25
r = 0.04    #Annual rate of return
current_savings = 0


# Calculations

down_payment_cost = total_cost * portion_down_payment
monthly_savings = (annual_salary / 12) * portion_saved

months = 0
while current_savings < down_payment_cost:
    salary_adjustment = (1 + semi_annual_raise) ** (months//6)
    current_savings += current_savings * r/12 + monthly_savings * salary_adjustment
    months += 1
    
print("Total Months:",months)