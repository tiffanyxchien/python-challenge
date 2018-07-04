import os
import csv

budget_data = 'budget_data.csv'

with open(budget_data, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    months = []
    revenue = []
    revenue_change = []

    print("Financial Analysis \n----------------------------")

    for row in csvreader:
        months.append(row[0])
        total_months = len(months)
        revenue.append(int(row[1]))
        total_revenue = sum(revenue)

    print(f"Total Months: {total_months} \nTotal: ${total_revenue}")

    for x in range(1, total_months):
        revenue_change.append(revenue[x] - revenue[x-1])
        average_change = round(sum(revenue_change)/len(revenue_change), 2)
        
    print(f"Average Change: ${average_change}")

    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
    greatest_increase_month = months[revenue_change.index(greatest_increase) + 1]
    greatest_decrease_month = months[revenue_change.index(greatest_decrease) + 1]
 
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

with open("output.txt", "w") as txtfile:
    txtfile.write(f"Total Months: {total_months} \nTotal: ${total_revenue} \nAverage Change: ${average_change} \nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase} \nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")