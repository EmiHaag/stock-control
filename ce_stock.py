import requests

from bs4 import BeautifulSoup


def current_ce_stock(ce_id):
    stock = []
    url = "[your-url]"
    try:
        response = requests.get(url)

        #here we have the html data, we need to grab the custom data using Beautiful soup lib.
       
        soup = BeautifulSoup(response.text, 'lxml')
        tables = soup.findChildren('table')
     
        my_table = tables[0]
        rows = my_table.findChildren(['tr'])

        for index in range(2, len(rows)):
            celdas_no_deseadas = ["Part Number", "Non Reworkable Parts", "Reworkable Parts", None, "Part Number", "Description", "Bin Loc","On Hand", "Last Receipt Date", "Cost" ,"Rework", "Min", "Max", "Roq", "Rop", "Comment"]
            cells = rows[index].findChildren('td')
            cell_array = []
            for cell in cells:
                value = cell.string
                if value not in celdas_no_deseadas:
                    cell_array.append(value)
            
            stock.append(cell_array)    
       
       
        return stock

    except requests.exceptions.RequestException as e:
    
        print("No esta conectado a la VPN. Conéctese a la misma y vuelva a ejecutar este archivo")
        input("presione ENTER para cerrar..")
        raise SystemExit(e)


#print(current_ce_stock("AR903E46"))
