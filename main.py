#########################################################################
#Title: Project Scenario - Data Analysis
#Description: This program allows user to read content from the file and identity the top 3 countries of visitors to Singapore from a specific region over a span of 10 years. 
#Name: Jovan Lim
#Class: PN2004L
#Date: 15/2/2021
#Version: 3.8.2
#########################################################################

#########################################################################
#Class - calculate Utility
#Read content from the file and identity the top 3 countries of visitors to Singapore from a specific region over a span of 10 years.
#########################################################################
import csv
#creates table-like custom objects from the items in CSV files

class top3countries:
  def __init__(self):
    #Function to calculate total visitors in each countries over a span of 10 years and list the top 3
    CalculateTotalVisitors()

#########################################################################
#Functon - CalculateTotalVisitors
#Read content from the file and calculate total visitors in each countries over a span of 10 years and list the top 3
#########################################################################
def CalculateTotalVisitors():

  path = 'MonthyVisitors.csv'
  #open file and universal newlines mode is enabled, but line endings are returned to the caller untranslated.
  file = open(path, newline='')
  #Return a reader object which will iterate over lines in the given csvfile
  reader = csv.reader(file)
  #skip the header
  header = next(reader)
  #initialise lists and variables
  data = []
  each_countries_total_visitors = []
  BruneiDarussalam _visitors = []
  Indonesia  _visitors = []
  Malaysia  _visitors = []
  Philippines  _visitors = []
  Thailand _visitors = []
  VietNam _visitors = []  
  Myanmar _visitors = []

  #Parse (remove irrelevant data regions) the data based on requirement
  for row in reader:
    # row = [Year,Month," Japan "," Hong Kong "," China "," Taiwan "," Korea, Republic Of "]
    year = int(row[0])
    month = str(row[1])
    BruneiDarussalam = int(row[2])
    Indonesia = int(row[3])
    Malaysia = int(row[4])
    Philippines = int(row[5])
    Thailand = int(row[6])
    VietNam = int(row[7])
    Myanmar = int(row[8])
  
    data.append([year, month, japan, hk, china, taiwan, korea])
  #close the file
  file.close()
  #parse the required range of data into lists
  for i in range(348, len(data)):
    dataR = data[i]
    BruneiDarussalam_visitors.append(dataR[2])
    Indonesia_visitors.append(dataR[3])
    Malaysia_visitors.append(dataR[4])
    Philippines_visitors.append(dataR[5])
    Thailand_visitors.append(dataR[6])
    VietNam_visitors.append(dataR[7])
    Myanmar_visitors.append(data[8])
  #sum of visitors from each countries over a span of 10 years
  total_Brunei_visitors = sum(BruneiDarussalam_visitors)
  total_Indonseia_visitors = sum(Indonesia_visitors)
  total_Malaysia_visitors = sum(Malaysia_visitors)
  total_Philippines_visitors = sum(Philippines_visitors)
  total_Thailand_visitors = sum(Thailand_visitors)
  total_VietNam_visitors = sum(VietNam_visitors)
  total_Myanmar_visitors = sum(Myanmar_visitors)
  #add each countries total visitors together to form a list
  each_countries_total_visitors.append(total_Brunei_visitors)
  each_countries_total_visitors.append(total_Indonseia_visitors)
  each_countries_total_visitors.append(total_Malaysia_visitors)
  each_countries_total_visitors.append(total_Philippines_visitors)
  each_countries_total_visitors.append(total_Thailand_visitors)
  each_countries_total_visitors.append(total_VietNam_visitors)
  each_countries_total_visitors.append(total_Myanmar_visitors)
  #sort the values from smallest to highest
  each_countries_total_visitors.sort()
  #removes the items one by one from the lists starting from the highest and assigned a variable to the return value
  first = each_countries_total_visitors.pop()
  second = each_countries_total_visitors.pop()
  third = each_countries_total_visitors.pop()
  fouth = each_countries_total_visitors.pop()
  fifth = each_countries_total_visitors.pop()
  sixth = each_countries_total_visitors.pop()
  seventh = each_countries_total_visitors.pop()
  #Find out which countries have the most visitors count
  if first == total_Brunei_visitors:
    print("1st: " + header[2] + " - " + str(first))
  else:
    if first == total_Indonseia_visitors:
      print("1st: " + header[3] + " - " + str(first))
    else:
      if first == total_Malaysia_visitors:
        print("1st: " + header[4] + " - " + str(first))
      else:
        if first == total_Philippines_visitors:
          print("1st: " + header[5] + " - " + str(first))
        else:
          if first == total_Thailand_visitors:
            print("1st: " + header[6] + " - " + str(first))
        else:
          if first == total_VietNam_visitors:
            print("1st: " + header[7] + " - " + str(first)

  if second == total_japan_visitors:
    print("2nd: " + header[9] + " - " + str(second))
  else:
    if second == total_hk_visitors:
      print("2nd: " + header[10] + " - " + str(second))
    else:
      if second == total_china_visitors:
        print("2nd: " + header[11] + " - " + str(second))
      else:
        if second == total_taiwan_visitors:
          print("2nd: " + header[12] + " - " + str(second))
        else:
          if fifth == total_korea_visitors:
            print("2nd: " + header[13] + " - " + str(second))

  if third == total_japan_visitors:
    print("3rd: " + header[9] + " - " + str(third))
  else:
    if third == total_hk_visitors:
      print("3rd: " + header[10] + " - " + str(third))
    else:
      if third == total_china_visitors:
        print("3rd: " + header[11] + " - " + str(third))
      else:
        if third == total_taiwan_visitors:
          print("3rd: " + header[12] + " - " + str(third))
        else:
          if third == total_korea_visitors:
            print("3rd: " + header[13] + " - " + str(third))

  if fouth == total_japan_visitors:
    print("Other: " + header[9] + " - " + str(fouth))
  else:
    if fouth == total_hk_visitors:
      print("Other: " + header[10] + " - " + str(fouth))
    else:
      if fouth == total_china_visitors:
        print("Other: " + header[11] + " - " + str(fouth))
      else:
        if fouth == total_taiwan_visitors:
          print("Other: " + header[12] + " - " + str(fouth))
        else:
          if fouth == total_korea_visitors:
            print("Other: " + header[13] + " - " + str(fouth))

  if fifth == total_japan_visitors:
    print("Other: " + header[9] + " - " + str(fifth))
  else:
    if fifth == total_hk_visitors:
      print("Other: " + header[10] + " - " + str(fifth))
    else:
      if fifth == total_china_visitors:
        print("Other: " + header[11] + " - " + str(fifth))
      else:
        if fifth == total_taiwan_visitors:
          print("Other: " + header[12] + " - " + str(fifth))
        else:
          if fifth == total_korea_visitors:
            print("Other: " + header[13] + " - " + str(fifth))

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  #program Title
  print("####################################################")
  print("data analyses - top 3 countries of visitors to Singapore over a span of 10 years")
  print("####################################################")
  #identify top 3
  top3countries()