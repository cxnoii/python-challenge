import csv
import os
import sys

from numpy import average


csvpath = r'\Users\Nickaruto\Desktop\python-challenge\PyBank\Resources\budget_data.csv'

with open(csvpath, newline='') as csvfile:
    budget_data = list(csv.reader(csvfile, delimiter=','))

    # making variables for total months & sum
    month_total = 0
    profit_loss_total = 0
    changes_list = []

    # incrementing rows for month total + adding profit/loss totals
    for row in budget_data[1:]:
        month_total += 1
        profit_loss_total = int(row[1]) + profit_loss_total

    for i in range(2, len(budget_data)):
        current_row = budget_data[i]
        previous_row = budget_data[i-1]
        change = int(current_row[1]) - int(previous_row[1])
        changes_list.append(change)


average_change = round((profit_loss_total/month_total), 2)

#print to terminal
print('Financial Analysis: ')
print(f'Total Months: {month_total}')
print(f'Total: $ {profit_loss_total}')
print(f'Average Change: {average(changes_list)}')
print(f'Greatest Increase in Profits: {max(changes_list)}')
print(f'Greatest Decrease in Profits: {min(changes_list)}')

#create and print to txt file
sys.stdout = open('Financial Analysis.txt', 'w')
print('Financial Analysis: ')
print(f'Total Months: {month_total}')
print(f'Total: $ {profit_loss_total}')
print(f'Average Change: {average(changes_list)}')
print(f'Greatest Increase in Profits: {max(changes_list)}')
print(f'Greatest Decrease in Profits: {min(changes_list)}')
sys.stdout.close()