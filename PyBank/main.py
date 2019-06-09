# Import the file
import csv
file = ('03-Python_homework_PyBank_Resources_budget_data.csv')

#Set an empty list for 2 set of data(columns) in opened file
with open (file, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header_row = next(csvreader)
    profit_loss = []
    total_months = []
   # Loop to add items to an empty list from column 1 and 2
    for row in csvreader:
        profit_loss.append (row[1]) 
        total_months.append (row[0])     
    # Count total months
    total_months_1 =  len(total_months) 
    # Convert text to number
    total = [int(i) for i in profit_loss]
    # Find total of Profit/Loss column
    total_profit_loss = sum (total)
    #Find average
    average = total_profit_loss / len(total)
    #Find max amount 
    max_increase = max(total)
    #Find min amount
    min_decrease = min(total)
    #Search for max and min amount index to find a month
    max_index = total.index(max_increase)
    min_index = total.index(min_decrease)
    max_month = total_months[max_index]
    min_month = total_months[min_index]
#Prin all outputs
print ("Total months: " + str(total_months_1))   
print("Total: " + "$" + str(total_profit_loss))
print("Average change: " + "$" + str(average))
print("Greatest increase in Profits: " + max_month + " $" + str(max_increase))
print("Greatest decrease in Profits: " + min_month + " $" + str(min_decrease))

file1 = open("file.txt", "w")
save_file = ["str1\n",
    "'Total months: ' + str(total_months_1)\n",
    "'Total: ' + '$' + str(total_profit_loss)\n",
    "'Average change: ' + '$' + str(average)\n",
    "'Greatest increase in Profits: ' + max_month + ' $' + str(max_increase)\n",
    "'Greatest decrease in Profits: ' + min_month + ' $'+ str(min_decrease)"]
file1.writelines(save_file)
file1.close()