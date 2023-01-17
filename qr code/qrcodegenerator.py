import tkinter as tk
import pyautogui as pg
from tkinter import ttk
from pyqrcode import QRCode

root = tk.Tk()
root.title("QR CODE GENERATOR")
root.resizable(0,0)

reso = pg.size()
rx = reso[0]
ry = reso[1]
x = int((rx / 2) - (1000 / 2))
y = int((ry / 2) - (500 / 2))
root.geometry("320x100" + f"+{x}+{y}")

def generate(d):
    n = QRCode(d)
    n.png('image.png', scale=10)
    ent.delete(0,tk.END)

lbl = ttk.Label(root, text="Data: ", font=("", 14))
ent = ttk.Entry(root, font=("",14))
btn = ttk.Button(root, text="Generate", command=lambda: generate(ent.get()))

lbl.grid(row=0, column=0, padx=10, pady=10)
ent.grid(row=0, column=1, padx=10, pady=10)
btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()