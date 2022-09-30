
import os
import constants

def retorna_ultimos_dos_nombres_de_reportes():
    #get list of all files in dir files stock
    file_names = os.listdir(constants.DIR_FILES_STOCK)

    temp= []
    for file_name in file_names:
    
        temp.append(os.path.splitext(file_name)[0])
    temp.sort(key=int, reverse=True)
    if len(temp)>1:
        return[ temp[0], temp[1]]
    else:
        return []

def retorna_ultimo_reporte_added():
    
    file_names = os.listdir(constants.DIR_DIF_REPORTES+"added/")

    temp= []
    for file_name in file_names:  
        #extrae el str fecha del nombre del archivo ej 220906 
      
        temp.append(os.path.splitext(file_name)[0].split("-")[1])  
    
    #ordena lista dejando a la fecha mas alta en la primera posicion
    temp.sort(key=int, reverse=True)
    
    if len(temp)>0:
        return[ temp[0]]
    else:
        return []


def retorna_ultimo_reporte_removed():
    
    file_names = os.listdir(constants.DIR_DIF_REPORTES+"removed/")
    temp= []
    for file_name in file_names:  
        #extrae el str fecha del nombre del archivo ej 220906 
     
        temp.append(os.path.splitext(file_name)[0].split("-")[1])    
    #ordena lista dejando a la fecha mas alta en la primera posicion
    temp.sort(key=int, reverse=True)
    if len(temp)>0:
        return[temp[0]]
    else:
        return []

#print(retorna_ultimo_reporte_added())