from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import os
from varibles import *




root = Tk()
root.title(TITLE)
root.geometry(RESOLUTION)


text = Text(width=TEXT_WIDTH, height = TEXT_HEIGHT)
text.pack()



def new_file():
    global file_name
    file_name = "empty"
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode = 'w', defaultextension='.py')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("ERROR", 'Error by cannot save file!')

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def open_source():
    inp = open('akmascode.py', 'r')
    text.delete('1.0', END)
    text.insert('1.0', inp.read())
    inp.close()




menu_bar = Menu(root)
file_menu = Menu(menu_bar)
plugins_menu = Menu(root)
menu_bar.add_cascade(label = "File", menu =file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save as", command=save_as)
menu_bar.add_cascade(label = "Write plugins", menu = plugins_menu)
plugins_menu.add_command(label= "Open source", command = open_source)
  

root.config(menu=menu_bar)
root.mainloop()