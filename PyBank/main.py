import csv
import os

csv_to_use = os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("analysis","output_file.txt")

if os.path.exists(csv_to_use) :
    number_of_months = 0
    net_Profits = 0
    avg_Change_per_Month = 0.0
    previous_profit = 0
    greatest_increase_in_profits = 0
    greatest_decrease_in_profits = 0
    sum_change_profit = 0 
    list_change_profit = []
    list_Change_date = []
    with open(csv_to_use) as mydata:
        my_reader = csv.reader(mydata)
        next(my_reader)

        for row in my_reader:
            number_of_months += 1
            net_Profits += int(row[1])

            if number_of_months > 1:
                avg_Change_per_Month += int(row[1]) - previous_profit
                sum_change_profit =  int(row[1]) - previous_profit
                list_change_profit.append(sum_change_profit)
                list_Change_date.append(row[0])
                 
            previous_profit = int(row[1])

            
        avg_Change_per_Month = avg_Change_per_Month / (number_of_months-1)

        #print(list_change_profit[0])
    
        #print("")
        #print(list_Change_date)
        maxprofit = max(list_change_profit)
        maxindex = list_change_profit.index(maxprofit)
        maxdate = list_Change_date[maxindex]
        #print(maxprofit,maxindex,maxdate)


        minprofit = min(list_change_profit)
        minindex = list_change_profit.index(minprofit)
        mindate = list_Change_date[minindex]
        #print(minprofit,minindex,mindate)

        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {number_of_months}")
        print(f"Total: ${net_Profits}")
        print(f"Average Change: ${avg_Change_per_Month:.2f}")
        print(f"Greatest Increase in Profits: {maxdate} (${maxprofit})")
        print(f"Greatest Decrease in Profits: {mindate} (${minprofit})")

        with open(file_to_output, 'w') as FAExport:
            FAExport.write("Financial Analysis\n")
            FAExport.write("----------------------------\n")
            FAExport.write(f"Total Months: {number_of_months}\n")
            FAExport.write(f"Total: ${net_Profits}\n")
            FAExport.write(f"Average Change: ${avg_Change_per_Month:.2f}\n")
            FAExport.write(f"Greatest Increase in Profits: {maxdate} (${maxprofit})\n")
            FAExport.write(f"Greatest Decrease in Profits: {mindate} (${minprofit})\n")
        

else:
    print("File does not exists: ", csv_to_use)
            
