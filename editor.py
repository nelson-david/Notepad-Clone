import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import *
import os
from tkinter.messagebox import *


def font_select():
	global win1
	win1 = Toplevel()
	win1.geometry("400x520")
	win1.resizable(width=False, height=False)
	win1.title("Font Style Setting")

	frame1 = Frame(win1, bg="white", width=200, height=200)
	frame1.grid(row=0, column=0)


	f_style_box = tk.Scrollbar(frame1)
	f_style_box.grid(row=0, column=0)

def close():
	answer = askquestion(title='Quit?', message="Are you sure you want to exit?")
	if answer=='yes':
		root.destroy()
	else:
		pass

def new_file():
	text_box.delete(1.0,END)

	root.title("Untitled - David Notes")


def open_file():
	global open_name
	open_name = askopenfilename(initialdir='c:\\python31\\',filetypes=[('Code files','.txt .py .dav')])
	if open_name != "":
		with open(f"{open_name}", "r") as r:
			data = r.read()
		
		text_box.insert(1.0, f"{data}")
		root.title(f"{open_name} - David Notes")

def re_save():
	global savings
	savings = 0
	re_file = text_box.get(1.0, END)
	try:
		with open(f"{general_name}", "w") as a:
			a.write(re_file)
			a.close()
			savings += 1
	except:
		with open(f"{open_name}", "w") as a:
			a.write(re_file)
			a.close()


	showinfo(title='Message', message='File Saved Successfuly')

def save_file():
	global general_name
	file = text_box.get(1.0, END)
	filename = asksaveasfilename(initialdir='c:\\python31\\',filetypes=[('Text files','.txt')])
	with open(f"{filename}.txt", "w") as f:
		f.write(file)
		f.close()
	root.title(f"{filename} - David Notes")

	general_name = f"{filename}.txt"






def main_menu():
	global file_menu
	global edit_menu
	global format_menu
	global help_menu
	global page_menu
	global menu


	menu = Menu()

	root.config(menu=menu)
	file_menu = Menu(menu, tearoff=0)
	file_menu.add_command(label='New     Ctrl+N', command=new_file)
	file_menu.add_command(label='Open    Ctrl+O', command=open_file)
	file_menu.add_command(label='Save     Ctrl+S', command=re_save)
	file_menu.add_command(label='Save As...', command=save_file)
	file_menu.add_separator()
	file_menu.add_command(label='Print...  Ctrl+P')
	file_menu.add_separator()
	file_menu.add_command(label='Exit', command=close)

	edit_menu = Menu(menu, tearoff=0)
	edit_menu.add_command(label='Undo    Ctrl+Z')
	edit_menu.add_command(label='Cut    Ctrl+X')
	edit_menu.add_command(label='Copy    Ctrl+C')
	edit_menu.add_command(label='Paste  Ctrl+V')
	edit_menu.add_separator()
	edit_menu.add_command(label='Find   Ctrl+F')
	edit_menu.add_command(label='Select All  Ctrl+A')

	format_menu = Menu(menu, tearoff=0)
	format_menu.add_command(label='Font Styles', command=font_select)
	format_menu.add_separator()
	format_menu.add_command(label='Font Color')

	help_menu = Menu(menu, tearoff=0)
	help_menu.add_command(label='View Help')
	help_menu.add_separator()
	help_menu.add_command(label='About Davnotes')

	page_menu = Menu(menu, tearoff=0)
	page_menu.add_command(label='Background Settings')
	page_menu.add_separator()
	page_menu.add_command(label='Zoom')

	menu.add_cascade(label='File', menu=file_menu)
	menu.add_cascade(label='Edit', menu=edit_menu)
	menu.add_cascade(label='Format', menu=format_menu)
	menu.add_cascade(label='Page Layout', menu=page_menu)
	menu.add_cascade(label='Help', menu=help_menu)






root = tk.Tk()
root.title("Untitled - David Notes")
root.geometry("1100x570")
root.resizable(width=False, height=False)
root.protocol('WM_DELETE_WINDOW', close)

main_menu()

text_box = ScrolledText(font=("Comic Sans MS", 11), width=120, height=27)
text_box.grid(row=0, column=0, padx=5)



mainloop()