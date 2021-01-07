
#Import supporting Python modules
import csv
import os

#Defnie relative path of .csv file
csvpath = os.path.join('Resources','budget_data.csv')

#Initialize lists to store contents of .csv
Date=[]
Profit_Loss=[]

#Open file and read contents
with open(csvpath) as csvfile:
    
    #Create csv reader object
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Read each row of the file and store in respective lists
    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(row[1])
        
#Remove headers of lists
Date.remove('Date')
Profit_Loss.remove('Profit/Losses')

#Calculate number of periods, each row represents a month
T_Months = len(Date)

#Transform 'Profit_Loss' list into integers
for x in range(0,len(Profit_Loss)):
  Profit_Loss[x] = int(Profit_Loss[x])
  
#Calculate Total amount of Profit/Losses over the period
T_Profit_Loss = sum(Profit_Loss)

#Create new 'Change' list to store period changes
Change=[]
for x in range(1,len(Profit_Loss)):  
  Change.append(Profit_Loss[x]-Profit_Loss[x-1])
  
#Calculate Average Change across periods
Avg_Change = sum(Change)/len(Change)

#Calculate Greates Increase and Date of that increase
max_value = max(Change)
max_date = Date[Change.index(max_value)+1]

#Calculate Greates Decrease and Date of that decrease
min_value = min(Change)
min_date = Date[Change.index(min_value)+1]

#Build analysis string to save on text file
text = ("Financial Analysis\n"
"----------------------------\n"
f"Total Months: {T_Months}\n"
f"Total: ${T_Profit_Loss}\n"
f"Average  Change: ${Avg_Change:.2f}\n"
f"Greatest Increase in Profits: {max_date} (${max_value})\n"
f"Greatest Decrease in Profits: {min_date} (${min_value})")
print(text)

#Defnie relative path to store text file
txtpath = os.path.join('Analysis','PyBankReport.txt')

#Write string to text file
report = open(txtpath, "w")
report.write(text)
report.close()