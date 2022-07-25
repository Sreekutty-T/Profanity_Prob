#importing libraries
from profanity_check import predict, predict_prob
from itertools import zip_longest
import csv


#Reading input file
with open('tweets.txt') as f:
    lines = [line.rstrip() for line in f]
  
#Calculating probability of profanity
Probability_of_Profanity = []
In_Percentage = []
for i in lines:
    l = [i]
    prob = predict_prob(l)
    num = float(prob)
    val = num * 100
    rou = round(val,3)
    In_Percentage.append(rou)
    Probability_of_Profanity.append(num)
    

#writing output to a csv file
d = [lines, Probability_of_Profanity, In_Percentage]
export_data = zip_longest(*d, fillvalue = '')
with open('output.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("lines", "Probability_of_Profanity","In_Percentage"))
      wr.writerows(export_data)
myfile.close()
