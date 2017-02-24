annual_salary = int(input('Enter your annual_salary: ' ))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ' ))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the sei-annual raise, as a decimal: '))
portion_down_payment = 0.20 * total_cost
r=0.05
current_savings=0
tmp_money=0
months=0
raise_period=6

while current_savings < portion_down_payment:
    if months > 0 and months % 6 == 0:
        annual_salary = annual_salary * (1+semi_annual_raise)
    monthly_salary = annual_salary / 12 + tmp_money*r /12
    current_savings += monthly_salary * portion_saved
    tmp_money += monthly_salary
    months += 1
print('Number of months: ', months)
