#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#Add Our Dependencies
import csv
import os

csvfile=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("Analysis","election_results.txt")  

#Set Total vote counter
Total_votes=0

#Candidate Sort
candidate_options=[]

# Candidate Votes
candidate_votes={}

#Winning Candidate
winning_candidate=""
winning_count = 0
winning_percentage = 0 

with open(csvfile) as election_data:
    csvreader = csv.reader(election_data, delimiter=",")

 
    headers = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
        # Total Votes Counter
        Total_votes += 1

        #print Candidate Name
        candidate_name=row[2]

        if candidate_name not in candidate_options:

        #Add candidate name to list
            candidate_options.append(candidate_name)
        #tracking candidates vote count
            candidate_votes[candidate_name]=0
        #Add Candidate votes
        candidate_votes[candidate_name] +=1
    
    #Iterate through list
    for candidate_name in candidate_votes:

        #get Vote count for candidate
        votes=candidate_votes[candidate_name]

        #Calculate percentage 
        vote_percentage=float(votes) / float(Total_votes)*100

    #    print(f'{candidate_name}: received {round(vote_percentage,1)} % of the vote')
    #Determine winning vote and candidate
    #Determine winning vote is greater than winning count

        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:})\n ')

        if (votes>winning_count) and (vote_percentage>winning_percentage):

        #setting winning value
            winning_count = votes
            winning_percentage = vote_percentage
        
        #identify winning candidate
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Vote Percentage: {winning_percentage:,.1f}\n'
    f'-------------------------\n'
    )
        

    print(winning_candidate_summary)        


 


