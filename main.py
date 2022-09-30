from generar_reporte_stock_actual import generar_reporte_stock_actual
from busca_reporte_anterior import *
from compara_dos_reportes import comparar_reportes 
from stock_file import get_list_from_file_report_added, get_list_from_file_report_removed
#si la vpn esta abierta
#1- generar reporte diario
#2- chequear si hay un reporte anterior
def generar_stock_diario():
    if generar_reporte_stock_actual("AR903E46"):
        print("Se generó reporte del día de la fecha \nBuscando reporte anterior..")
        reportes_anteriores = retorna_ultimos_dos_nombres_de_reportes()

        if len(reportes_anteriores)>0:
            print(reportes_anteriores)
            comparar_reportes(reportes_anteriores[0]+".txt", reportes_anteriores[1]+".txt")
        else:
            print("no existen reportes anteriores..") 

    else:
        print("No se pudo generar reporte actual")

#retorna el ultimo reporte added en formato lista
def get_ultimo_reporte_added():
    last_added_list = get_list_from_file_report_added(retorna_ultimo_reporte_added())
    return last_added_list


#retorna el ultimo reporte removed en formato lista
def get_ultimo_reporte_removed():
    last_removed_list = get_list_from_file_report_removed(retorna_ultimo_reporte_removed())
    return last_removed_list
#print(get_ultimo_reporte_removed())
