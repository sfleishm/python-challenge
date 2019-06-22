import os
import csv


csvData = os.path.join('..', 'HW3_boot', 'budget-data.csv')

countMonths = []
totals = []


with open(csvData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        countMonths.append(row[0])
        totals.append(row[1])
        
#turns the totals list from strings into integers       
totals = [int(i) for i in totals]

#https://stackoverflow.com/questions/2400840/finding-differences-between-elements-of-a-list
v = [totals[i+1] - totals[i] for i in range(len(totals)-1)]

#average change of the differences 
change = (sum(v)/len(v))
#print(change)

#prints the highest value of list v
#print(max(v))

#prints the lowest value of list v 
#print(min(v))
    
#print(sum(totals)) works

#+1 since the difference list has one less
indexHigh = v.index(max(v))
greatestIncrease = countMonths[indexHigh+1]

indexLow = v.index(min(v))
lowestDate = countMonths[indexLow+1]


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(countMonths)}') 
print(f'Total: ${sum(totals)}') 
print(f'Average Change: ${round(change,2)}')
print(f'Greatest Increase in Profits: {greatestIncrease} ${max(v)}')
print(f'Greatest Decrease in Profits: {lowestDate} ${min(v)}')

file = "..\HW3_boot\hw3TestBudget.txt"
writing = open(file, "w")
writing.write("Financial Analysis\n")
writing.write("----------------------------\n")
writing.write(f'Total Months: {len(countMonths)}\n')
writing.write(f'Total: ${sum(totals)}\n')
writing.write(f'Average Change: ${round(change,2)}\n')
writing.write(f'Greatest Increase in Profits: {greatestIncrease} ${max(v)}\n')
writing.write(f'Greatest Decrease in Profits: {lowestDate} ${min(v)}\n')
writing.close()
    
#o The total number of months included in the dataset  86
#o The net total amount of "Profit/Losses" over the entire period $38382578
#o The average of the changes in "Profit/Losses" over the entire period $-2315.12
#o The greatest increase in profits (date and amount) over the entire period Feb-2012 ($1926159)

    #print(max(totals)) # this is giving me the max of the highest in the list, i need the highest rate of change 
#o The greatest decrease in losses (date and amount) over the entire period Sep-2013 ($-2196167)

#print(countMonths[index+1])
#print(index)
