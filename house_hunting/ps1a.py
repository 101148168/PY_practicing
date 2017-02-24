annual_salary = int(input('Enter your annual_salary: ' ))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ' ))
total_cost = int(input('Enter the cost of your dream home: '))
portion_down_payment = 0.20 * total_cost
r=0.05
current_savings = 0
tmp_money=0
months=0

while current_savings < portion_down_payment:
    monthly_salary = annual_salary / 12 + tmp_money*r /12
    current_savings += monthly_salary * portion_saved
    tmp_money += monthly_salary
    months += 1
print('Number of months: ', months)
