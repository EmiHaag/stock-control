
from check_pulse_login import check_pulse_conn
from ce_stock import current_ce_stock
from stock_file import make_current_stock_ce_file
from call_pulse import open_pulse
import os

clear = lambda:os.system('cls')
clear()

 #pasos
    #1. cuando se ejecuta el script:
    #       se traen todas las filas del stock actual del ce
    #       se almacenan en una lista
    #       se chequea si existe archivo con stock_ce_xx_yy.txt (xx = legajo , yy = date)
    #           si archivo no existe se crea uno nuevo con el stock actual de la fecha
    #               si existe archivo anterior se compara, si hay cambios se hace un append a archivo final con las filas affectadas



def generar_reporte_stock_actual(legajo_ce):
    #check if pulse secure is connected
    if check_pulse_conn():
        print("Pulse OK")
            
        #       se traen todas las filas del stock actual del ce
    
        stock = current_ce_stock(legajo_ce)

        if len(stock) > 0:
            #make file
            make_current_stock_ce_file(stock)
            print("Reporte generado.")
        return True
    else:
        print("Pulse no conectado. Abriendo pulse..")
        if open_pulse():
            print("se abrio pulse, ingrese datos")
        return False
    




   