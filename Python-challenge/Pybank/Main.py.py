import os
import csv
#import pandas as pd

Pybank_csv = os.path.join("PyBank", "Resources","budget_data.csv")
with open(Pybank_csv, newline="") as file:
    #for line in csvfile:
        #print (line)
    csv_reader = csv.reader(file, delimiter=",") 
    csv_header = next(file)
    #print(f"Header: {csv_header}")
    total_month = 0
    total = 0
    i = 1
    for row in csv_reader:
        Profit_Losses = row[1]
        Date = row[0]
        if Date != "":
            total_month = total_month + 1
        if float(row[1])!= "":
            total = total + int(row[1])
    print ("--------------------------------")
    print ("Financial Analysis")
    print ("--------------------------------")
    print ("Total month = " + str(total_month))
    print ("--------------------------------")
    print("Total = " + str(total))
    print ("--------------------------------")
    print ("Average = " + str(total/total_month))
    print ("--------------------------------")

#---------------------------------------------------------------
#This is also how I used Panda To solve it----------------------

    #df = pd.read_csv(Pybank_csv)
    #print(df)
    #print ("--------------------------------")
    #print ("Financial Analysis")
    #print ("--------------------------------")
    #The total number of months included in the dataset
    #print ("Total Month = " + str(df["Date"].count()))
    #print ("--------------------------------")
    #The net total amount of "Profit/Losses" over the entire period
    #print ("Total = " + str(df["Profit/Losses"].sum()))
    #print ("--------------------------------")
    #The average of the changes in "Profit/Losses" over the entire period
    #print ("Average Change = " + str(df["Profit/Losses"].mean()))
    #print ("--------------------------------")
    #The greatest decrease in losses (date and amount) over the entire period
    #df2 = df.sort_values("Profit/Losses", ascending = True)
    #sorted_df = df2.reset_index(drop=True)
    #print("Greatest Decrease in Profits = " + str(sorted_df.loc[0,:]))
    #print ("--------------------------------")
    #The greatest increase in profits (date and amount) over the entire period
    #df3 = df.sort_values("Profit/Losses", ascending = False)
    #sorted_df2 = df3.reset_index(drop=True)
    #print("Greatest Increase in Profits = " + str(sorted_df2.loc[0,:]))
    #print ("--------------------------------")
    #In addition, your final script should both print the analysis to the terminal and export a text 
    #file with the results.
    #df3.to_csv("output.csv")
