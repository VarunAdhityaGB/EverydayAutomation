from tkinter import *
from tkinter import ttk
import pyautogui as pyg, time

root = Tk()
root.tk.call("source", "sv.tcl")
root.tk.call("set_theme", 'dark')
root.geometry('585x480')
root.title("Writer")
root.resizable(0,0)
    
def write(content):
    time.sleep(5)
    pyg.typewrite(content)
    txtb.delete(0, "end-1c")

txtb = Text(root)
txtb.grid(row=0, column=0, padx=10, pady=10)
btn = ttk.Button(root, text='WRITE', width=50, command=lambda: write(txtb.get(1.0, "end-1c")))
btn.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()