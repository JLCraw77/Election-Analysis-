# Election-Analysis-
## Project Overview
A Colorado Board of elections employee has given me the task to analyze the election data for the local congressional election.
  1) Calcualte the total number of votes
  2) Complete list of candidates receiving votes
  3) Calculate total number of votes received by each candidate
  4) Calculate the percentage of the votes each candidate won
  5) Determine the winner based on popular vote

## Resources
  - Datafile: election_results.csv
  - Python 3.7.6 and VS Code 1.63.2

## Summary
  - There were 369,711 Votes cast in the Colorado congressional election.
  - The 3 candidates listed below:
    -   Charles Casper Stockham
    -   Diana DeGette
    -   Raymon Anthony Doane
  - The candidates Results were as follows:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
  - The winner of the congressional election was:
    - Diana DeGette receiving 73.8% of the votes and getting 272,892 cast votes
 
## Challenge Overview
   - The following 3 Counties listed below:
      - Jefferson: 10.5% (38,855)
      - Denver: 82.8% (306,055)
      - Arapahoe: 6.7% (24,801)
   - Specify which County had the largest turout of voters
    
## Challenge Summary
  -  The county voting results are as follows:
      - Jefferson County with 38,855 votes had 10.5% of the total votes 
      - Denver County with 306,055 votes had 82.8% of the total votes 
      - Arapahoe County with 24,801 votes had 6.7% of the total votes
  - The county that had the largest turout of voters is Denver.

## Recommendation on Future Elections:
  - This election analysis can be used on any future elections by changing the following 2 items and runng the code.
   
   1) Provide a new .csv file to be anaylzed and point in the proper location on Line 9 of the Code
      - file_to_load = os.path.join("Resources", "election_results.csv")

   2) The row location within new data for the candidate or county may need to be adjsuted to match the data file.
      - candidate_name = row[2]  and / or county = row[1]
  


