#Import the csv library to read the .csv file
#Import Counter object from collections class
import csv
import os
from collections import Counter

#Defnie relative path of .csv file
csvpath = os.path.join('Resources','election_data.csv')

#Array to store total list of votes
votes = []

#Open file and read contents
with open(csvpath) as csvfile:
    
    #Create csv reader object
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Read each row of the file and store in respective lists
    for row in csvreader:
        votes.append(row[2])
        
#Remove headers of list
votes.remove('Candidate')

#Calculate Total Number of votes
T_votes = len(votes)

#Count unique occurrences in the votes list
results = Counter(votes)

#Get key of max value in the 'results' dictionary
winner = max(results,key=results.get)

#Assemble the string for the text report
text = ("Election Results\n" +
  "-------------------------\n" +
  f"Total Votes: {T_votes}\n" +
  f"-------------------------\n" +
  f"Khan: {results.get('Khan')/T_votes*100:.2f}% ({results.get('Khan')})\n" +
  f"Correy: {results.get('Correy')/T_votes*100:.2f}% ({results.get('Correy')})\n" +
  f"Li: {results.get('Li')/T_votes*100:.2f}% ({results.get('Li')})\n" +
  f"O'Tooley: {results.get('''O'Tooley''')/T_votes*100:.2f}% ({results.get('''O'Tooley''')})\n" +
  "-------------------------\n" +
  f"Winner: {winner}\n" +
  "-------------------------")
print(text)

#Defnie relative path to store text file
txtpath = os.path.join('Analysis','PyPollReport.txt')

#Write string to text file
report = open(txtpath, "w")
report.write(text)
report.close()