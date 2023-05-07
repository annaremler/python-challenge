# Import modules os and csv
import os
import csv

# Part 1: PyBank
## Pull CSV file "budget_data.csv" and set path
pybank_csv = os.path.join("Resources", "budget_data.csv")
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

## Create variables and lists
    profit = []
    difference = []
    dates = []

    count = 0
    total_profit = 0
    revenue_change = 0
    initial_profit = 0

    for row in csvreader:
        count = count + 1
        dates.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        difference_profit = int(row[1])
        monthly_difference = difference_profit - initial_profit
        difference.append(monthly_difference)

        revenue_change = revenue_change + monthly_difference
        initial_profit = difference_profit
        average_profits = monthly_difference / count

        greatest_increase = max(difference)
        increase_month = dates[difference.index(greatest_increase)]
        greatest_decrease = min(difference)
        decrease_month = dates[difference.index(greatest_decrease)]


## Check that data Financial Analysis checks out
    print(f'PyBank Analysis')

    print(f'Total Months: {len(dates)}')
    print(f'Total: ' + "$" + str(total_profit))
    print(f'Average Change: ' + "$" + str(int(average_profits)))
    print(f'Greatest Increase in Profits: ' + str(increase_month) + " ($" + str(greatest_increase) + ")")
    print(f'Greatest Decrease in Profits: ' + str(decrease_month) + " ($" + str(greatest_decrease) + ")")


## Open into text file
    with open("Financial_analysis.txt", "w") as text:
        text.write(f'PyBank Analysis' + "\n")

        text.write(f'Total Months: {len(dates)}' + "\n")
        text.write(f'Total: ' + "$" + str(total_profit) + "\n")
        text.write(f'Average Change: ' + "$" + str(int(average_profits)) + "\n")
        text.write(f'Greatest Increase in Profits: ' + str(increase_month) + " ($" + str(greatest_increase) + ")\n")
        text.write(f'Greatest Decrease in Profits: ' + str(decrease_month) + " ($" + str(greatest_decrease) + ")\n")