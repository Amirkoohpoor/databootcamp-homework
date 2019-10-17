import os
import csv
#import pandas as pd
#import numpy as np


PyPoll_csv = os.path.join("PyPoll", "Resources","election_data.csv")
with open(PyPoll_csv, newline="") as csvfile:
    #for line in csvfile:
        #print (line)
    csv_reader = csv.reader(csvfile, delimiter=",") 
    #df = pd.read_csv(PyPoll_csv)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    total_votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    Otooley = 0
    for row in csv_reader:
        candidate = row[2]
        if candidate == "Khan" or candidate == "Correy" or candidate == "Li" or candidate == "O'Tooley":
            total_votes = total_votes + 1

        if candidate == "Khan":
            Khan = Khan + 1
        elif candidate == "Correy":
                Correy = Correy +1
        elif candidate == "Li":
                Li = Li +1
        else:
            Otooley = Otooley +1


    print ("--------------------------------")
    print ("Election Results")
    print ("--------------------------------")
    print ("Total votes :        " + str(total_votes))
    print ("--------------------------------")
    print ("Khan : " + "         " + str(Khan) + " ||||||  " + str((Khan/total_votes)*100) + "%")
    print ("Correy : " + "       " + str(Correy) + "  ||||||  " + str((Correy/total_votes)*100) + "%")
    print ("Li : " + "           " + str(Li) + "  ||||||  " + str((Li/total_votes)*100) + "%")
    print ("O'Tooley : " + "     " + str(Otooley) + "  ||||||  " + str((Otooley/total_votes)*100) + "%")
    print ("--------------------------------")

    if Khan > Correy and Khan > Li and Khan > Otooley:
        print ("Winner:        " + "Khan")
    elif Correy> Khan and Correy > Li and Correy > Otooley :
        print ("Winner:        " + "Correy")
    elif Li> Khan and Li > Correy and Li > Otooley :
        print ("Winner:        " + "Li")
    else:
        print ("Winner:        " + "O'Tooley")

#---------------------------------------------------------------
#This is also how I used Panda To solve it----------------------
    # print(df)

    # The total number of votes cast
    #total_votes = df["Voter ID"].count()
    #print ("--------------------------------")
    #print ("Election Results")
    #print ("--------------------------------")
    #print ("Total Votes = " + str(total_votes))

    # A complete list of candidates who received votes

    #print ("--------------------------------")
    #print (df["Candidate"].value_counts(normalize = True).mul(100).round(1).astype(str) + "%")
    #print ("--------------------------------")
    #print (df["Candidate"].value_counts())
    #print ("--------------------------------")

    # The winner of the election based on popular vote.

    #print ("Winner = " + str(df["Candidate"].value_counts().max()))
    #print ("--------------------------------")

    #In addition, your final script should both print the analysis to the terminal and export a text file with the results.

    #df2.to_csv("output.csv")
    #df2 = df.groupby(["Candidate"]).max()
    #print (df2)