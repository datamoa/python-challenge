# Import the file
import csv
file = ('03-Python_homework_PyBank_Resources_budget_data.csv')


with open (file, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header_row = next(csvreader)
   #Set an empty list for  set of datas
    profit_loss = []
    total_months = []
    # Set an empty list for profit/loss and start a count as 0 to find the incremental 
    profit_loss_raw = []
    prev_profit_loss = 0
   # Loop to add items to an empty list from column 1 and 2
    for row in csvreader:
    # Set a condition to skip the first row of incremental because it doesnt have a data
      if len(total_months) > 0:
          profit_loss.append ( int(row[1]) - int(prev_profit_loss) ) 
      total_months.append (row[0])
      profit_loss_raw.append(row[1])
      prev_profit_loss = row[1]
    # Count total months
    total_months_1 =  len(total_months) 
    # Convert profir/loss string to number 
    total = [int(i) for i in profit_loss_raw]
    # Find total of Profit/Loss
    total_profit_loss = sum (total)
    # Convert difference array to numbers
    diff_total = [int(i) for i in profit_loss]
    # Find difference total
    diff_total_sum = sum(diff_total)
    #Find average
    average = round(diff_total_sum / len(diff_total))
    #Find max amount 
    max_increase = max(diff_total)
    #Find min amount
    min_decrease = min(diff_total)
    #Search for max and min amount index in Month column to find a date
    max_index = diff_total.index(max_increase)
    min_index = diff_total.index(min_decrease)
    max_month = total_months[max_index + 1]
    min_month = total_months[min_index + 1]
#Print all outputs
print("Financial Analysis")
print ("Total months: " + str(total_months_1))   
print("Total: " + "$" + str(total_profit_loss))
print("Average change: " + "$" + str(average))
print("Greatest increase in Profits: " + max_month + " $" + str(max_increase))
print("Greatest decrease in Profits: " + min_month + " $" + str(min_decrease))
