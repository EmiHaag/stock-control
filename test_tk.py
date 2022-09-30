from cmath import exp
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
with Image.open("img/favicon.ico") as _img:
    pic_img = ImageTk.PhotoImage(_img)
column_names = ("details", "price")

treeview_food = ttk.Treeview(root, columns=column_names)

treeview_food.heading("#0", text="Product")
treeview_food.heading("details", text="Details")
treeview_food.heading("price", text="Price")
treeview_food.pack(fill=tk.BOTH, expand=True)


treeview_food.insert(parent="", index=tk.END, values=("pizz1", "1.22"), image=pic_img)
root.mainloop()