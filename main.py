import tkinter
from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("300x400+10+20")
window.title("Python")

label=Label(window,text = "Welcome to PyCharm CE!", fg = "white", bg = "black")
label.place(x=70, y=40)

entry=Entry(window, bd = 2)
entry.place(x=55, y=70)

button=Button(window, text = "Start", fg = "black", font = ("Verdana", 16))
button.place(x=110, y=100)

v1=IntVar()
radiobutton1 = Radiobutton(window, text= "Admin", variable = v1 ,value = 1)
radiobutton2 = Radiobutton(window, text= "Guest", variable = v1 ,value = 2)
radiobutton1.place(x=115, y=150)
radiobutton2.place(x=115, y=180)

v2=StringVar()
v2.set('User 1')
data1 = "User 1", "User 2", "User 3"
combo = ttk.Combobox(window, values=data1)
combo.place(x=48, y = 230)

data = "Info", "Details", "Description"
lb = Listbox(window, height=3, selectmode="multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=61, y=280)

window.mainloop()
