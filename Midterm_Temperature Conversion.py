from tkinter import *

class TemperatureWindow:
    def __init__ (self, temp):
        self.lbl1=Label(temp, text='Enter Temperature')
        self.lbl1.place(x=30, y=25)
        self.lbl2 = Label(temp, text='Result')
        self.lbl2.place(x=50, y=150)
        self.t1 = Entry(bd=3)
        self.t1.place(x=160, y=25)
        self.t2 = Entry(bd=3)
        self.t2.place(x=160, y=150)
        self.btn1 = Button(temp, text='Fahrenheit to Celsius')
        self.btn1 = Button(temp, text='Fahrenheit to Celsius', command=self.Temp1)
        self.btn1.place(x=50, y=80)
        self.btn2 = Button(temp, text='Kelvin to Celsius')
        self.btn2 = Button(temp, text='Kelvin to Celsius', command=self.Temp2)
        self.btn2.place(x=230, y=80)

    def Temp1(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=(num1-32)*5/9
        self.t2.insert(END, str(result))

    def Temp2(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=(num1-273.15)
        self.t2.insert(END, str(result))

window=Tk()
mywin=TemperatureWindow(window)
window.title('TEMPERATURE UNIT CONVERSION')
window.geometry("400x200+10+10")
window.mainloop()
