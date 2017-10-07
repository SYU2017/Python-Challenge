import os
import csv

newbudgetdata2 = os.path.join('..','Resources', "budget_data2.csv")
    
    total_months = 0
    total_revenue = 0
    avg_rev_change = 0
    current_month_rev = 0
    period_month_rev = 0
    
    change_in_rev = []

with open(newbudgetdata2, "r" ) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    headerline = csvfile.next()
    
for row in csvreader:

    total_months = sum(map(int, row))-1
    #print( "Total Months : " + str(total_months))
    total_revenue += int(row[1])
    #print( "Total Revenue : " +"$"+ str(total_revenue)
    if total_months > 1:
          change = current_month_rev - period_month_rev
          change_in_rev.append(change)
          
total_change = 0
for i in range(len(change_in_rev)):
    total_change = total_change + change_in_rev[i]

    avg_rev_change = total_change / len(change_in_rev)
 
    print("Total Months: " + str(total_months))
    print( "Total Revenue : " +"$"+ str(total_revenue)
    print("Average Revenue Change:" +"$"+  str(round(avg_rev_change,2)))
output_file = os.path.join('../Resources','Pybank' + ".txt") 
with open(output_file, 'w') as textfile:
    textfile.write("Total Months: " + str(total_months)+ "\n")
    textfile.write("Total Revenue: "+" $" + str(total_revenue) + "\n")
    textfile.write("Average Revenue Change: "+" $" + str(round(avg_rev_change, 2))+ "\n")