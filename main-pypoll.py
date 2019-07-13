#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:27:09 2019

@author: badz
"""

import os
import csv

csvpath = os.path.join('/Users/badz/', 'Desktop', 'election_data.csv')

count = 0
candidate_list = []
unique_candidate= []
vote_count = []
vote_percent = []

with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvfile)
        
        for row in csvreader:
            count = count + 1
            candidate_list.append(row[2])
        for x in set(candidate_list):
            unique_candidate.append(x)
            y = candidate_list.count(x)
            vote_count.append(y)
            z = (y/count)*100
            vote_percent.append(z)
            
        winning_vote_count = max(vote_count)
        losing_vote_count = min(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]
        loser = unique_candidate[vote_count.index(losing_vote_count)]

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("The loser is: " +loser)
print("-------------------------")
print("That's fucking crazy dude")
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")

  
       
