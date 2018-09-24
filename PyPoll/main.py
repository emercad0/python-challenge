import os
import csv

data_file = os.path.join("Resources","election_data_2.csv")
r_analysis = os.path.join("Resources","results.txt")


# retrive csv for analyst 
def file_check(path):
    with open(path) as data:
        csvReader = csv.DictReader(data, delimiter=',')
        for row in csvReader:
            yield row
        return csvReader
            
# function to help group the votes by candidates 
# Return data of candidates who received votes base on index (0,1,2,3,...)
def candidates_with_votes(data,who='Candidate'):
    candidatesVotes = {}
    for row in file_check(data_file):
        # Our Candidates
        candidates = row[who]
        #list to add voter ID values for each dictionary keys 
        candidatesList = []
        
        #if name of candidate is a member of dictionary candidatesVotes 
        if candidates in candidatesVotes:
        # fill in members in the list
            candidatesList = candidatesVotes[candidates]
        # add ID 
        candidatesList.append(row['Voter ID'])
         # fill in group voter id keys by member
        candidatesVotes[candidates] = candidatesList         
    return candidatesVotes


# The total number of votes each candidate won
def numberOfVotesPer(candidate):
    votesData  = candidates_with_votes(file_check(data_file))
    candidates = votesData[candidate]
    total = 0
    for n in candidates:
        total = total + 1
    return total

#The total number of votes cast 
def totalVotes():
    #Count all the rows
    countV = 0
    for row in file_check(data_file):
        countV = countV + 1
    return(countV)

#print(type(candidates_with_votes(file_check(data_file))))
#print(V)

#The percentage of votes each candidate won    - divide the sum of each candidates votes by the total amount of votes
def percentage_of_votes(index):
    total = 0
    voteCounts = {}
    percentofVotes = {}
    votePercentage = 0 
    results = []
    # assign the data of the group candidates  
    data = candidates_with_votes(file_check(data_file))
    for v in data.items():
        #list of candidates votes 
        votes = v[1]  
        # total for all votes
        total = total + len(votes) 
        if v[0] not in voteCounts:
        # assign value to key of candidates in votecounts
            voteCounts[v[0]]= 0        
    #gather the total amount of votes for each candidates 
    #and assign to voteCounts variables
            voteCounts[v[0]] = voteCounts[v[0]] + len(votes)
    # Calculate percentage by dividing
    for values in voteCounts:
        counts = voteCounts.get(values)
        votePercentage = counts / total * 100
        percentofVotes[values] = 0
        percentofVotes[values] = percentofVotes[values] +  votePercentage
    #return list with name and percentage
    #results = list(percentofVotes.items())
    # return only values***
    results = list(percentofVotes.values())
    return results[index]

# copy of function above but this will only return a string
def percentageOfVotesCandidate(value):
    total = 0
    voteCounts = {}
    percentofVotes = {}
    votePercentage = 0 
    results = []
    # assign the data of the group candidates  
    data = candidates_with_votes(file_check(data_file))
    for v in data.items():
        #list of candidates votes 
        votes = v[1]  
        # total for all votes
        total = total + len(votes) 
        if v[0] not in voteCounts:
        # assign value to key of candidates in votecounts
            voteCounts[v[0]]= 0        
    #gather the total amount of votes for each candidates 
    #and assign to voteCounts variables
            voteCounts[v[0]] = voteCounts[v[0]] + len(votes)
    # Calculate percentage by dividing
    for values in voteCounts:
        counts = voteCounts.get(values)
        votePercentage = float(counts / total) * 100
        percentofVotes[values] = 0
        percentofVotes[values] = percentofVotes[values] +  votePercentage
    results = list(percentofVotes)
    return str(results[value])


#The winner of the election based on popular vote. 
#- Who received the most votes
def winnerOfElection():
    votesData  = candidates_with_votes(file_check(data_file))
    mPopular = 0 
    winner = ''
    for person in votesData:
        votes = votesData.get(person)
        #popularV = len(votesData[person])
        #print(person)
        if(len(votes) > mPopular):
            mPopular = len(votes)
            return(person)     
def main():
    
    print(
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {totalVotes()}\n"
          f"-------------------------\n"
          f" {percentageOfVotesCandidate(0)}  {percentage_of_votes(0)}  {numberOfVotesPer(percentageOfVotesCandidate(0))}\n"
          f" {percentageOfVotesCandidate(1)}  {percentage_of_votes(1)}  {numberOfVotesPer(percentageOfVotesCandidate(1))}\n"
          f" {percentageOfVotesCandidate(2)}  {percentage_of_votes(2)}  {numberOfVotesPer(percentageOfVotesCandidate(2))}\n"
          f" {percentageOfVotesCandidate(3)}  {percentage_of_votes(3)}  {numberOfVotesPer(percentageOfVotesCandidate(3))}\n"
          f"-------------------------\n"
          f" Winner:: {winnerOfElection()}\n"
          f"-------------------------\n")

    writeout = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {totalVotes()}\n"
          f"-------------------------\n"
          f" {percentageOfVotesCandidate(0)}  {percentage_of_votes(0)}  {numberOfVotesPer(percentageOfVotesCandidate(0))}\n"
          f" {percentageOfVotesCandidate(1)}  {percentage_of_votes(1)}  {numberOfVotesPer(percentageOfVotesCandidate(1))}\n"
          f" {percentageOfVotesCandidate(2)}  {percentage_of_votes(2)}  {numberOfVotesPer(percentageOfVotesCandidate(2))}\n"
          f" {percentageOfVotesCandidate(3)}  {percentage_of_votes(3)}  {numberOfVotesPer(percentageOfVotesCandidate(3))}\n"
          f"-------------------------\n"
          f" Winner:: {winnerOfElection()}\n"
          f"-------------------------\n")
    with open(r_analysis, "w") as file:
        file.write(writeout)

if __name__ == '__main__':
    main()