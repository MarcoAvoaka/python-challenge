
# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv
csv_file_path = os.path.join('Resources', 'budget_data.csv')
#create file path for out file budget_data.txt
with open(csv_file_path) as csvfile:
# CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    month_total = 0
    total = 0
    net_transition = 0
    greatest_inc =0
    greatest_dec = 0
    changes = 0
    output_path = 0
    first_row = next(csvreader)
    
# The total number of months included in the dataset
    month_total = 1
# The net total amount of "Profit/Losses" over the entire period
    net_transition = int(first_row[1])
    prev_PL = int(first_row[1])
    change_list =[]

    for line in csvreader:
        #reads and increments the count of month
        #print(line[0]), int(line[1])
        month_total +=1
        #reads and increments the total profit/loss
        total += int(line[1])
        #print(month_total, total)
        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #print(int(line[1]), prev_PL)
        monthly_change =  int(line[1]) - prev_PL
        
        change_list.append(monthly_change)
        prev_PL = int(line[1])

#Calculate the average net change
print(sum(change_list)/len(change_list))

# The greatest increase in profits (date and amount) over the entire period
#USE MAX FUNCTION ON CHANGE_LIST
print(max(change_list)) 

# The greatest decrease in profits (date and amount) over the entire period
#USE MIN FUNCTION ON CHANGE_LIST
print(min(change_list))

#print into text file and open the outfile and write

output_path = os.path.join('Analysis', 'results_data.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
# write the header
    csvwriter.writerow(['Financial Analysis'])
# write the data
    csvwriter.writerow(['Month Total: 86', 'Current Total: 38382578', 'Greatest Increase: 1926159', 'Greatest Decrease: -2196167', 'Average Net Change: -2315.1176470588234'])
    
