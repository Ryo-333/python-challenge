import os
import csv

# Read data from CSV file
file_path = '/Users/ryojousin/Downloads/Starter_Code 3/PyBank/Resources/budget_data.csv'
file = open(file_path, 'r')
reader = csv.reader(file)
next(reader)  # Skip header row
data = list(reader)
file.close()

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = int(data[0][1])
total_changes = 0
greatest_increase = 0
greatest_decrease = 0
greatest_inc_date = ""
greatest_dec_date = ""

# Iterate through the data to perform calculations
for row in data:
    total_months += 1
    net_total += int(row[1])
    profit_loss = int(row[1])
    change = profit_loss - previous_profit_loss
    total_changes += change
    
    if change > greatest_increase:
        greatest_increase = change
        greatest_inc_date = row[0]
    
    if change < greatest_decrease:
        greatest_decrease = change
        greatest_dec_date = row[0]
    
    previous_profit_loss = profit_loss

# Calculate average change
average_change = total_changes / (total_months - 1)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease})")

# Export the analysis to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_decrease})\n")
