from datetime import datetime
import constants

today = datetime.now()
todayformated = today.strftime("%y%m%d")
def make_current_stock_ce_file(stock_list):
    with open("{}{}.txt".format(constants.DIR_FILES_STOCK, todayformated), "w") as file:
        for row in stock_list:
        
        
            str_cell =""
            for cell in row:
                str_cell += cell + "***"
            
            file.write(str_cell + "\n")
    return

    

def make_differences_report(added_parts, removed_parts):
    with open("{}added/added-{}.txt".format(constants.DIR_DIF_REPORTES,todayformated), "w") as file:
        for row in added_parts:        
            str_cell =""
            for cell in row:
                str_cell += cell + "***"
            
            file.write(str_cell + "\n")
    with open("{}removed/removed-{}.txt".format(constants.DIR_DIF_REPORTES, todayformated), "w") as file:
        for row in removed_parts:    
        
            str_cell =""
            for cell in row:
                str_cell += cell + "***"
            
            file.write(str_cell + "\n")
    
    return

def get_list_from_file_report_added(file_name):
    return_list = []
    with open("{}added/added-{}.txt".format(constants.DIR_DIF_REPORTES,file_name[0])) as file:
        
        for line in file:
            if line != "\n":
                formatted_line = line.strip(",\n").split("***")

                return_list.append(formatted_line)
    return return_list

def get_list_from_file_report_removed(file_name):
    return_list = []
    with open("{}removed/removed-{}.txt".format(constants.DIR_DIF_REPORTES,file_name[0])) as file:
        
        for line in file:
            if line != "\n":
                formatted_line = line.strip(",\n").split("***")

                return_list.append(formatted_line)
    return return_list