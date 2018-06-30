import os
import csv

budget_data = 'budget_data.csv'

with open(budget_data, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    months = []
    revenue = []
    revenue_change = []

    print("Financial Analysis")
    print("----------------------------")

    for row in csvreader:
        months.append(row[0])
        total_months = len(months)
        revenue.append(int(row[1]))
        total_revenue = sum(revenue)

    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_revenue))

    for x in range(1, total_months):
        revenue_change.append(revenue[x] - revenue[x-1])
        average_change = round(sum(revenue_change)/len(revenue_change), 2)
        
    print("Average Change: $" + str(average_change))

    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
    greatest_increase_month = months[revenue_change.index(greatest_increase) + 1]
    greatest_decrease_month = months[revenue_change.index(greatest_decrease) + 1]
 
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")

import sys
sys.stdout = open("output.txt", "w")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")