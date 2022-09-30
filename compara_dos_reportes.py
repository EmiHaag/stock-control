import constants
from stock_file import make_differences_report 
# retorna un array con una parte x, las veces que aparezca en la lista


def get_item_en_lista(item, lista):
    res = []
    for i in lista:
        if i[0] == item[0] and i[2] == item[2]:
            res = i

    return res


def comparar_reportes(last_rep, penultimate_rep):
    added_parts = []
    removed_parts = []
    last_rep_list = []
    penultimate_rep_list = []

    with open(constants.DIR_FILES_STOCK + last_rep) as file:
        for line in file:
            if line != "\n":
                formatted_line = line.strip(",\n").split("***")

                last_rep_list.append(formatted_line)

    with open(constants.DIR_FILES_STOCK + penultimate_rep) as file:
        for line in file:
            if line != "\n":
                formatted_line = line.strip(",\n").split("***")
                penultimate_rep_list.append(formatted_line)

    # se recorre cada item en last rep list
    for item in last_rep_list:
        # si cambio la fila o se removio
        # if item not in penultimate_rep_list:
        # o la fila ya no existe mas o se modifico una fila y tiene mas stock o menos stock
        # chequea si item actual esta en reporte anterior retorna [item=>good,item=>bad] si no lo encuentra
        item_en_anteultima_lista = get_item_en_lista(
            item, penultimate_rep_list)

        # el item no figuraba en la lista anterior ni good ni bad
        if len(item_en_anteultima_lista) == 0:
            # parte no estaba en lista anterior, se incrementa directamente
            added_parts.append(
                [item[0], item[1], item[3]])
        elif int(item[3]) > int(item_en_anteultima_lista[3]):
            added_parts.append([item[0], item[1] 
                               ,  str(int(item[3]) - int(item_en_anteultima_lista[3]))])
        elif int(item[3]) < int(item_en_anteultima_lista[3]):
            removed_parts.append([item[0], item[1]
                                 ,  str(int(item_en_anteultima_lista[3]) - int(item[3]))])
        # situacion 2:  existe en reporte anterior y se incremento su stock
        # a su vez no se incremento bad
        # situacion 3: el item esta en reporte anterior y se decremento con respecto al nuevo reporte
        # Si la suma de la parte en estado good + bad == al good + bad de reporte anterior no se debe incrementar

    # se recorre cada item en anteultimo reporte si fila no existe en el ultimo reporte se incrementa removed parts[]
    for item in penultimate_rep_list:

        item_en_ultima_lista = get_item_en_lista(item, last_rep_list)

        if len(item_en_ultima_lista) == 0:
            # parte no estaba en la ultima lista
            removed_parts.append(
                [item[0], item[1] ,  item[3]])

    added_temp = []
    removed_temp =[]
    #busca elementos que hayan sido agregados y eliminados en la misma cantidad added+1 == removed+1 y los remueve
    for index, added in enumerate(added_parts):
        for index2, removed in enumerate(removed_parts):
            if removed[0] == added[0]:
                if removed[2] == added[2]:
                    #index_to_remove.append(index)
                    #index2_to_remove.append(index2)
                    #del added_parts[index]
                    #del removed_parts[index2]
                    added_temp.append(added)
                    removed_temp.append(removed)
                    break
  
    
    for tmp in added_temp:        
        try:
            added_parts.remove(tmp)
        except ValueError:
            print("Se intento remover un valor inexistente: {}".format(tmp))

    for tmp in removed_temp:
        try:
            removed_parts.remove(tmp)
        except ValueError:
            print("Se intento remover un valor inexistente: {}".format(tmp))


    print("COMPARA_DOS_REPORITES: added parts: {}, removed parts: {}".format(added_parts, removed_parts))
    make_differences_report(added_parts, removed_parts)

#comparar_reportes("220910.txt", "220907.txt")
