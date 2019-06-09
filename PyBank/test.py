import csv
file = ('03-Python_homework_PyBank_Resources_budget_data.csv')

with open (file, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header_row = next(csvreader)
    profit_loss = []
    total_months = []
    for row in csvreader:
        profit_loss.append (row[1]) 
        total_months.append (row[0])     
    total_months_1 =  len(total_months) 
    total = [int(i) for i in profit_loss]
    total_profit_loss = sum (total)
    average = total_profit_loss / len(total)
    max_increase = max(total)
    min_decrease = min(total)
    max_index = total.index(max_increase)
    min_index = total.index(min_decrease)
    max_month = total_months[max_index]
    min_month = total_months[min_index]

print ("Total months: " + str(total_months_1))   
print("Total: " + "$" + str(total_profit_loss))
print("Average change: " + "$" + str(average))
print("Greatest increase in Profits: " + max_month + " $" + str(max_increase))
print("Greatest decrease in Profits: " + min_month + " $" + str(min_decrease))

file1 = open("file.txt", "w")
save_file = ["str1\n",
    "'Total months: ' + str(total_months_1)\n",
    "'Total: ' + "$" + str(total_profit_loss)\n",
    "'Average change: ' + "$" + str(average)\n",
    "'Greatest increase in Profits: ' + max_month + " $" + str(max_increase)\n",
    "'Greatest decrease in Profits: ' + min_month + " $" + str(min_decrease)"]
file1.writelines(save_file)
file1.close()