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
    profit_loss_list = []

    for row in csv_reader:
        total_months = total_months + 1
        profit_loss_list.append(row[1])
        
#The net total amount of "Profit/Losses" over the entire period    
    net_total = 0

    for i in range(0,len(profit_loss_list)):
        net_total = net_total + int(profit_loss_list[i])
    

#The average of the changes in "Profit/Losses" over the entire period
#MOVING AVERAGE NOT WORKING
    averages = []

    for i in range(0,len(profit_loss_list)):
        x = int(profit_loss_list[i-1])
        y = int(profit_loss_list[i])
        avg = x + y / 2.0
        averages.append(avg)

    avg_change = statistics.mean(int(str(averages)))
    
    print(avg_change)

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period



def financial_analysis(): 
    print('')
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    
    print(f"Total: ${net_total}")
    

#financial_analysis()