# Import modules os and csv
import os
import csv

# Part 1: PyBank
## Pull CSV file "budget_data.csv" and set path
pybank_csv = os.path.join ("Resources", "budget_data.csv")

## Open CSV as reader
with open(pybank_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    ## Create lists
    profit = []
    difference = []
    date = []

    ## Insert variables
    count = 0
    total_profit = 0
    revenue_change = 0
    initial_profit = 0

    ## Coding the chart
    for row in csvreader:    
        # Use count to count the number months in this dataset
        count += 1 

        # Append onto "date"
        date.append(row[0])

        # Append profit and calculate total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        #Calculate average change in profits monthly
        final_profit = int(row[1])
        difference_profits = final_profit - initial_profit

        #Store monthly changes in a list
        difference.append(difference_profits)

        revenue_change = revenue_change + difference_profits
        initial_profit = final_profit

        ##Calculate average change in profits
        average_revenue_change = (revenue_change/count)
        
        ##Find max and min change in profits + the dates that changes occured
        greatest_increase_profits = max(difference)
        greatest_decrease_profits = min(difference)

        increase_date = date[difference.index(greatest_increase_profits)]
        decrease_date = date[difference.index(greatest_decrease_profits)]

    ## Check that data Financial Analysis checks out
    print(f"Financial Analysis")
    print(f"----------------------------------------------------------")
    print(f"Total Months: " + str(count))
    print(f"Total Profits: " + "$" + str(total_profit))
    print(f"Average Change: " + "$" + str(int(average_revenue_change)))
    print(f"Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print(f"Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    
    ##Open into text file
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(totalProfit) +"\n")
    text.write("    Average Change: " + '$' + str(int(averagechangeProfits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(grtstincreaseProfits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(grtstdecreaseProfits) + ")\n")
    text.write("----------------------------------------------------------\n")
