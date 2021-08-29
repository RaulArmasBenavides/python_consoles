import calendar
import datetime
from tkinter import *
import tkinter as tk

# Obtenemos los valores del año y mes a mostrar
year = datetime.date.today().year
month = datetime.date.today().month
 
def writeCalendar(year,month):
	# Asignamos el año y mes al calendario
	str1 = calendar.month(year, month)
 
	label1.configure(text=str1)
 
def mesAnterior():
	global month,year
	month-=1
	if month==0:
		month=12
		year-=1
 
	writeCalendar(year,month)

def mesSiguiente():
	global month,year
	month+=1
	if month==13:
		month=1
		year+=1
 
	writeCalendar(year,month)
 
root = tk.Tk()
root.title("Calendario")
 
# Lo posicionamos en un label
label1 = tk.Label(root, text="", font=('courier', 14, 'bold'), bg='white', justify=tk.LEFT)
label1.grid(row=1,column=1)

# ponemos los botones dentro un Frame
frame=tk.Frame(root,bd=5)
anterior = tk.Button(frame,text="Anterior", command=mesAnterior)
anterior.grid(row=1, column=1, sticky=tk.W)
siguiente = tk.Button(frame,text="Siguiente", command=mesSiguiente)
siguiente.grid(row=1, column=2)
frame.grid(row=2,column=1)
 
writeCalendar(year,month)
 
# ejecutamos el evento loop
root.mainloop()