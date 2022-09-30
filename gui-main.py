
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from main import *

stringLabel = "starting.."


def call_tree(list_last_added, list_last_removed):
    root = Tk()
    root.state("zoomed")
    style = ttk.Style()
    style.configure("Treeview", rowheight=45)
    root.iconbitmap("img/favicon.ico")
    root.title('Control de stock')

    global stringLabel

    label = Label(root, text=stringLabel)
    label.config(text=stringLabel)
    label.pack(side="bottom")

    column_names = ('part_number', 'nombre', 'cantidad')
    my_tree = ttk.Treeview(root, columns=column_names)

    my_tree.heading("#0")
    my_tree.heading("part_number", text="Part Number")
    my_tree.heading("nombre", text="Nombre")
    my_tree.heading("cantidad", text="Cantidad")

    my_tree.pack(fill=tk.BOTH, expand=True)
    stringLabel = stringLabel + "Starting.. 2"
    label.config(text=stringLabel)
    with Image.open("img/arrow_top.png") as _img_up, \
            Image.open("img/arrow_bottom.png") as _img_down,\
            Image.open("img/cloud_off.png") as _cloud_off,\
            Image.open("img/cloud_ok.png") as _cloud_ok:
        arrow_up = ImageTk.PhotoImage(_img_up)
        arrow_down = ImageTk.PhotoImage(_img_down)
        cloud_on = ImageTk.PhotoImage(_cloud_ok)
        #cloud_on = cloud_on.zoom(25)       
        #cloud_off = ImageTk.PhotoImage(_cloud_off)

    for added in list_last_added:

        my_tree.insert(parent="", index=tk.END, values=(
            added[0], added[1], added[2]), image=arrow_down)

    for removed in list_last_removed:
        my_tree.insert(parent="", index=tk.END, image=arrow_up,
                       values=(removed[0], removed[1], removed[2]))

    stringLabel = stringLabel + "Tabla actualizada"
  
    image = Image.open('img/cloud_ok.png')
    image = image.resize((20, 20), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image=image)

    label = tk.Label(root, image=img1)
    label.pack()
    root.mainloop()


def update_list():
    global stringLabel
    stringLabel = stringLabel + "Generando reporte"

    generar_stock_diario()
    list_last_added = get_ultimo_reporte_added()
    list_last_removed = get_ultimo_reporte_removed()
    stringLabel = stringLabel + "\nReporte generado"

    print("reporte generado..{}".format(list_last_added))
    stringLabel = stringLabel + "\nActualizando tabla.."

    call_tree(list_last_added, list_last_removed)


update_list()
