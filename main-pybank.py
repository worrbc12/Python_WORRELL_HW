# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import csv

csvpath = os.path.join('/Users/badz/', 'Desktop', 'budget_data.csv')

PL = []
months = []
revenue_change = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
  
    for rows in csvreader:
        PL.append(int(rows[1]))
        months.append(rows[0])
    
    for x in range(1, len(PL)):
        revenue_change.append((int(PL[x] - int(PL[x-1]))))
        revenue_average = sum(revenue_change) / len(revenue_change)
        total_months = len(months)
        
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    print("Financial Analysis")
    print("................................................................") 
    print("Total Months: " + str(total_months))
    print(" ")
    print("Total: " + "$" + str(sum(PL)))
    print(" ")
    print("Average change: " + "$" + str(revenue_average))
    print(" ")
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print(" ")
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease)) 
    print("............................................................... ")
    
file = open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("...................................................................................." + "\n")
file.write("total months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(sum(PL)) + "\n")
file.write("Average change: " + "$" + str(revenue_average) + "\n")
file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
file.close()
    
    
    

  
      
         
        
        
   
    
    
    

        

   
    
        
        
    
        


        
        
        
    
    

       
        
       
      
        
        
            
        
            
            
    
    
        
        
        
        
        
       
        
      
        
       
       
            
        
        
    

        
        
    
    
    

   