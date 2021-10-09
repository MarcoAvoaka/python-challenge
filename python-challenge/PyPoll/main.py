# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv
csvpath = os.path.joint('Resources', 'election_data.csv.icloud')

# Initializing variables
Khanvotes = 0
Correyvotes =0
Livotes =0
Otooleyvotes =0

# Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
# Next header
    csv_header = next(csvreader)
# Loop
    for row in csvreader:
        TotalVotes = TotalVotes + 1
# Candidate Name and Total
        if (row[2] == "Khan"):
            Khanvotes = Khanvotes + 1
        elif (row[2] == "Coreey"):
            Correyvotes = Correyvotes + 1
        elif (row[2] == "Li"):
            Livotes = Livotes + 1
        elif (row[2] == "OTooley"):
            Otooleyvotes = Otooleyvotes + 1

# Percentage of each Candidate
Khanpercentage = Khanvotes/TotalVotes
Correypercentage = Correyvotes/TotalVotes
Lipercentage = Livotes/TotalVotes
Otooleypercentage = Otooleyvotes/TotalVotes

# Finding the winner
if Khanvotes > Correyvotes and Khanvotes > Livotes and Khanvotes > Otooleyvotes:
    Winner = "Khan"
elif Correyvotes >Khanvotes and Correyvotes > Livotes and Correyvotes > Otooleyvotes:
    Winner = "Correy"
elif Livotes > Khanvotes and Livotes > Correyvotes and Livotes > Otooleyvotes:
    Winner = "Li"
elif Otooleyvotes > Khanvotes and Otooleyvotes > Correyvotes and Otooleyvotes >Livotes:
    Winner = "Otooley"

# Printing results
print("Election Results")
print(".........................")
print(TotalVotes + str(TotalVotes))
print(".........................")
print("Khan: "+ str(round(Khanpercentage*100,2)) + "% ("+str(Khanvotes) +")")
print("Correy: "+ str(round(Correypercentage*100,2)) + "% ("+str(Correyvotes) +")")
print("Li "+ str(round(Lipercentage*100,2)) + "% ("+str(Livotes) +")")
print("Otooley: "+ str(round(Otooleypercentage*100,2)) + "% ("+str(Otooleyvotes) +")")
print(".........................")
print("Winner: " + Winner)
print(".........................")

Textfile = open(r".\Pypoll\Pypoll_Output.txt", "w")

Textfile.write("Election Results")
Textfile.write("\n")
Textfile.write(".................")
Textfile.write("\n")
Textfile.write("Total Votes: " + str(TotalVotes))
Textfile.write("\n")
Textfile.write(".................")
Textfile.write("\n")
Textfile.write("Khan : " +str(round(Khanpercentage*100,2)) +"% (str(Khanvotes) +")
Textfile.write("\n")
Textfile.write("Correy : " +str(round(Correypercentage*100,2)) +"% (str(Correyvotes) +")
Textfile.write("\n")
Textfile.write("Li : " +str(round(Lipercentage*100,2)) +"% (str(Livotes) +")
Textfile.write("\n")
Textfile.write("Otooley : " +str(round(Otooleypercentage*100,2)) +"% (str(Otooleyotes) +")
Textfile.write("\n")
Textfile.write(".................")
Textfile.write("\n")
Textfile.write("Winner: " + Winner)
Textfile.write("\n")
Textfile.write(".................")
Textfile.close()








        

