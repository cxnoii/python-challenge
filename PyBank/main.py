import csv, os
import math


csvpath = r'\Users\Nickaruto\Desktop\python-challenge\PyBank\Resources\budget_data.csv'

def financial_analysis(budget_data):
    date = str(budget_data[0])
    total = int(budget_data[1])
    print(f'wtf is going on + {total}')

with open(csvpath, newline = '') as csvfile:
    budget_data = csv.DictReader(csvfile, delimiter=',')
    next(budget_data)

 #making variables for total months & sum
    month_total = 1
    profit_loss_total = 0

 #incrementing rows for month total + adding profit/loss totals
    for row in budget_data:
     month_total += 1
     profit_loss_total = int(row['Profit/Losses']) + profit_loss_total

#this is not working yet.
    for row in budget_data:
        if float(row[1]) > 0:
            max_inc = row[0]
            value_max = float(row[1])

   
average_change = round((profit_loss_total/month_total),2)


print(f'Total Months: {month_total}')
print(f'Total: $ {profit_loss_total}')
print(f'Average Change: $ {average_change}')

#print(type(greatest_inc))



