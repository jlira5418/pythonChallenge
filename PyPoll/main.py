import csv
import os

csv_to_use = os.path.join("Resources","election_data.csv")
file_to_output = os.path.join("analysis","output_file.txt")

if not os.path.exists(csv_to_use):
    print("File does not exists: ", csv_to_use)
    exit()


with open(csv_to_use) as mydata:
    my_reader = csv.reader(mydata)
    next(my_reader)

    number_of_votes = 0
    list_of_candidates = []
    list_number_of_votes_per_candidate = {}


    
    for row in my_reader:
        number_of_votes += 1
        if row[2] not in list_of_candidates :
            list_of_candidates.append(row[2])
            list_number_of_votes_per_candidate[row[2]] = 1   
        else:
            list_number_of_votes_per_candidate[row[2]] += 1
        
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {number_of_votes}")
    print("-------------------------")

    percent_votes = 0
    candidate_votes = 0
    winner_votes = 0
    winner_name = ""

    for candidate_name in list_of_candidates:
        candidate_votes = list_number_of_votes_per_candidate[candidate_name]
        percent_votes = candidate_votes/number_of_votes
        if candidate_votes > winner_votes :
            winner_votes = candidate_votes
            winner_name = candidate_name
        print(f"{candidate_name}: {percent_votes:.3%} ({candidate_votes})")
    
    print("-------------------------")
    print(f"Winner: {winner_name}")
    print("-------------------------")

    with open(file_to_output, 'w') as FAExport:
        FAExport.write("Election Results\n")
        FAExport.write("-------------------------\n")
        print(f"Total Votes: {number_of_votes}\n")
        FAExport.write("-------------------------\n")
        for candidate_name in list_of_candidates:
            candidate_votes = list_number_of_votes_per_candidate[candidate_name]
            percent_votes = candidate_votes/number_of_votes
            if candidate_votes > winner_votes :
                winner_votes = candidate_votes
                winner_name = candidate_name
            FAExport.write(f"{candidate_name}: {percent_votes:.3%} ({candidate_votes})\n")
        FAExport.write("-------------------------\n")
        FAExport.write(f"Winner: {winner_name}\n")
        FAExport.write("-------------------------\n")

