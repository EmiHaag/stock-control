from genericpath import isfile
import constants
import os
import re

"""
return a list of reports by dates, with the option of select and open by one

"""

#define an empty list
report_list = []


#get the dir of the filename and return every item added / removed
def getItemsFromFiles(dir_path):
    list = []
    try:
        with open(dir_path, 'r') as file:
            for line in file:
                if line != "\n":
                    list.append(line.strip(",\n").split("***"))
            return list        
    except FileNotFoundError:
        print("{} ERROR: File not found".format(dir_path))
    
#return => 
#report date : 08/09/2022 
#           added 1 
#               8770321277 DOCUMENT PROOF OF TECHNICAL VI***4***
#           removed 1
#               8770321277 DOCUMENT PROOF OF TECHNICAL VI***4***
#return a list of all reports ordered by date 
def get_report_list():

    #get list of dates removed and added 'added-220906.txt' and 'removed-220913.txt'
    added_dates = os.listdir("{}/added".format(constants.DIR_DIF_REPORTES))
    

    #iterate over dates, for every date added has a removed 
    for fileName in added_dates:
        #get the date from the file name with format dd/mm/yyyy
        date_pattern = r"\w+-(\d\d)(\d\d)(\d\d)"
        date = re.search(date_pattern, fileName)
        # return > 'report date: 22/09/2022'
        #print("report date: {}/{}/20{}".format(date[3],date[2],date[1]))
        added = getItemsFromFiles("{}added/{}".format(constants.DIR_DIF_REPORTES, fileName))
        #print("ADDED++ ({})".format(len(added)))
        removed = getItemsFromFiles("{}removed/removed-{}{}{}.txt".format(constants.DIR_DIF_REPORTES, date[1],date[2],date[3]))
        #print("REMOVED++ ({})".format(len(removed)))
        item = {}
        item["date"] = "{}/{}/20{}".format(date[3],date[2],date[1])
        item["added"] = added
        item["removed"]=removed
        report_list.append(item)
       
    return report_list



print(get_report_list())