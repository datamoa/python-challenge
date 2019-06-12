import csv
from collections import Counter

# Path to collect data from the file
file = ('03-Python_homework_PyPoll_Resources_election_data.csv')

# Give a title to all outputs
print("Election Results")

#Path to atore results as a txt file
result_file = open("result.txt","w")

# open the CSV
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header_row = next(csvreader)
   #set an empty list for Voter total and Candidate list
    voters = []
    candidate = []
    #Loop to add items to an empty list
    for row in csvreader:
        voters.append(row[0])
        candidate.append(row[2])
    #Find and print total voters
    total_voters = len(voters)
    print("Total voters: " + str(total_voters))

    #Use counter function to find candidate occurancies and set dictionary 
    candidate_list = Counter(candidate)
    results = candidate_list.items()
    #Set a string for winner and start winner count as O
    winner_name = ""
    winner_count = 0
    #Use loop to find pecentage in dic
    for item in results:
        percent = round((item[1] / total_voters) * 100)
        line = item[0] + ': ' + str(percent) + '%' + ', ' + str(item[1]) +"\n"
        result_file.write(line)
        print(line)
        if item[1] > winner_count:
            winner_name = item[0]
            winner_count = item[1]
            
    print('Winner is ' + winner_name)
    
#  py_poll = open("file.txt", "w")
# save_py_poll = ["str1\n",
#     "Election Results" + "\n",
#     "Total voters: " + str(total_voters) + "\n",
#     item[0] + ': ' + str(percent) + '%' + ', ' + str(item[1]) + "\n",
#     "Winner is " + winner_name + "\n",]
result_file.write("Winner is " + winner_name + "\n")
# py_poll.writelines(save_py_poll)
# py_poll.close()
result_file.close()