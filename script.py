###Script to create a readily importable file into MedNet that lists access point names
#that have been exported from Cisco Prime.  This script was intended to make large, sweeping
#updates to the MedNet database.  In order to speed up this script the MAC addresses should be
#alphabetically sorted in each exported file.
#Last modified 12/4/2015 by Jordan Villarreal

#Opens and reads in the file exported by MedNet
hospiraFile = open ('C:\Python27\hospiralist.csv', 'r')
hospiraList = hospiraFile.readlines()
#Forces all text to upper case.  As of writing MedNet exports MAC addresses using upper case. 
#This is a saftey in the event Hospira changes their code
hospiraList = [element.upper() for element in hospiraList]

#Opens and reads in the file exported by Cisco Prime
primeFile = open ('C:\Python27\primelist.csv', 'r')
primeList = primeFile.readlines()
#Forces all text to upper case.  As of writing Prime exports MAC addresses using lower case.  
#This normalizes the data to match the MedNet standard
primeList = [element.upper() for element in primeList]

#Logic behind matching process.  
for i in range(len(hospiraList)): #For every item in the Hospira list
	for ii in range(len(primeList)): #Process every item in the Prime list
		if hospiraList[i][:16] == primeList[ii][:16]: #If the first 16 characters match : Example 1 below
			hospiraList[i] = hospiraList[i][:18] + primeList[ii][18:] #Slice the first 18 characters from the Hospira list to all characters after the 18th in the Prime list : Example 2 below
		
combinedList = open ('C:\Python27\combined-new-list.csv', 'w')
for item in hospiraList:
	combinedList.write("%s" % item)
combinedList.close()

#Example 1 12:34:56:78:90:A                          This purposefully leaves off the last hex digit because it changes depending on the SSID
#Example 2 12:34:56:78:90:AB,TCHMACCESSPOINTNAME     This output is a blend of the necessary information from both lists
