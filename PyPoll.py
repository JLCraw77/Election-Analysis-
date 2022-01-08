#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import csv
import os

csvfile=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("Analysis","election_results.txt")  
 # CSV reader specifies delimiter and variable that holds contents
csvreader = csv.reader(csvfile, delimiter=',')
#     # CSV reader specifies delimiter and variable that holds contentscsvreader = csv.reader(csvfile, delimiter=',')
print(csvreader)

# with open(file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election")
#     txt_file.write("\n---------------")


#     txt_file.write("\nArapahoe\nDenver\nJefferson")
 

with open(csvfile) as election_data:
        csvreader = csv.reader(election_data, delimiter=",")

# Read and print the header row.
        headers = next(csvreader)
        print(headers)
    
# for row in csvreader:
#          print(row)

    # Read and print the header row.
    # headers = next(file_reader)
    # print(headers) 
    
#     # Read the header row first (skip this step if there is now header)
# csv_header = next(csvreader)
# print(f"CSV Header: {csv_header}")
    
# #     # Read each row of data after the header
# for row in csvreader:
#     print(row)
