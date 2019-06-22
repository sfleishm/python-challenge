import os
import csv

csvData = os.path.join('..', 'HW3_boot', 'election_data (1).csv')

candidates = []
voters = []
khanVotes = []
correyVotes = []
liVotes = []
tooleyVotes = []

with open(csvData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        voters.append(row[0])

        # if the name appears in row 2 append it to a list 
        if 'Khan' == row[2]:
            khanVotes.append(row[2])

        elif 'Correy' == row[2]:
            correyVotes.append(row[2])

        elif 'Li' == row[2]:
            liVotes.append(row[2])

        elif 'O\'Tooley' == row[2]:
            tooleyVotes.append(row[2])


# Percentage of votes
countKhan = ((len(khanVotes)/len(voters))*100.00)
countCorrey = ((len(correyVotes)/len(voters))*100.00)
countLi = ((len(liVotes)/len(voters))*100.00)
countTooley = ((len(tooleyVotes)/len(voters))*100.00)

# Dictionary to put name and votes together
dict = {
    'Khan': len(khanVotes),
    "Correy": len(correyVotes),
    "Li": len(liVotes),
    "O\'Tooley": len(tooleyVotes)
    }

max_value = max(dict.values())  # maximum value
max_keys = [k for k, v in dict.items() if v == max_value] # getting all keys containing the `maximum`


print('Election Results')
print('-------------------------')
print(f'Total Votes: {len(voters)}')
print('-------------------------')
print(f'Khan: {round(countKhan,3)}% ({len(khanVotes)})')
print(f'Correy: {round(countCorrey,3)}% ({len(correyVotes)})')
print(f'Li: {round(countLi,3)}% ({len(liVotes)})')
print(f'O\'Tooley: {round(countTooley,3)}% ({len(tooleyVotes)})')
print('-------------------------')
print(f'Winner: {max_keys}')

file = "..\HW3_boot\hw3Election.txt"
writing = open(file, "w")
writing.write("Election Results\n")
writing.write("----------------------------\n")
writing.write(f'Total Votes: {len(voters)}\n')
writing.write("----------------------------\n")
writing.write(f'Khan: {round(countKhan,3)}% ({len(khanVotes)})\n')
writing.write(f'Correy: {round(countCorrey,3)}% ({len(correyVotes)})\n')
writing.write(f'Li: {round(countLi,3)}% ({len(liVotes)})\n')
writing.write(f'O\'Tooley: {round(countTooley,3)}% ({len(tooleyVotes)})\n')
writing.write(f'-------------------------\n')
writing.write(f'Winner: {max_keys}\n')
writing.close()

