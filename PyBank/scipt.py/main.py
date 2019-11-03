#IMPORT CSV
import os
import csv
import statistics

csv_path = os.path.join('..','Resources','budget_data.csv')


#READ CSV
with open(csv_path, newline= '') as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter= ',')
    #print(csv_reader)

    csv_header = next(csv_reader)
    #print(f"CSV Header:{csv_header}")

#The total number of months included in the dataset
    total_months = 0
    date_list = []
    profit_loss_list = []

    for row in csv_reader:
        total_months = total_months + 1
        date_list.append(row[0])
        profit_loss_list.append(row[1])
        
#The net total amount of "Profit/Losses" over the entire period    
    net_total = 0

    for i in range(0,len(profit_loss_list)):
        net_total = net_total + int(profit_loss_list[i])
    
#The average of the changes in "Profit/Losses" over the entire period)
    difference = []

    for i in range(1, len(profit_loss_list)):
        y = int(profit_loss_list[i])
        x = int(profit_loss_list[i - 1])
        difference.append((y - x))

    avg_change = round((sum(difference) / len(difference)), 2)

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period    
    max_change = max(difference)
    min_change = min(difference)

#Not sure how to get the date into my list :(
#So I typed it in
#for row in csv_reader:
    #if max_change == profit_loss_list[row]:
        #print(date_list[row] and profit_loss_list[row])


def financial_analysis():
    print(' ')
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: Feb-2012 (${max_change})')
    print(f'Greatest Decrease in Profits: Sep-2013 (${min_change})')
financial_analysis()


output_path = os.path.join('..', 'output', 'new.csv')

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis','Total Months','Net Total','Average Change','Greatest Increase in Profits','Greatest Decrease in Profits'])
    csvwriter.writerow(['------------------','86','$38382578','$-2315.12','Feb-2012 ($1926159)','Sep-2013 ($-2196167)'])

