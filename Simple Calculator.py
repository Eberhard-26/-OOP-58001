from tkinter import *
window = Tk()
window.title('Simple Calculator')
window.geometry("450x300+20+10")


class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.place(relx=0.50, y=50, anchor= "center")
        self.lbl2 = Label(window, text="Input 1st Number:")
        self.lbl2.place(x=50, y=80 )
        self.txtfld2 = Entry(window, bd=3)
        self.txtfld2.place(x= 180, y=80)
        self.lbl3 = Label(window, text= "Input 2nd Number:")
        self.lbl3.place(x=50, y=120, )
        self.txtfld3 = Entry(window, bd=3)
        self.txtfld3.place(x=180, y=120)

        self.lbl4=Label(window, text="Choose among the Operators", bg = "Yellow")
        self.lbl4.place(x=50, y=150)
        self.btn1=Button(window,text= "Add(+)",command=self.add)
        self.btn1.place(x=50,y=200)
        self.btn2 = Button(window, text="Subtract(-)",command=self.subtract)
        self.btn2.place(x=125, y=200)
        self.btn1 = Button(window, text="Multiply(*)",command=self.multiply)
        self.btn1.place(x=225, y=200)
        self.btn2 = Button(window, text="Divide(/)",command=self.div)
        self.btn2.place(x=322, y=200)

        self.lbl5=Label(window, text= "Answer")
        self.lbl5.place(x=50,y=250)

        self.txtfld4=Entry(window,bd=4)
        self.txtfld4.place(x=120, y=250)


    def add(self):
        self.txtfld4.delete(0, 'end')
        number1=int(self.txtfld2.get())
        number2=int(self.txtfld3.get())
        answer=number1+number2
        self.txtfld4.insert(END,str(answer))

    def subtract(self):
        self.txtfld4.delete(0, 'end')
        number1=int(self.txtfld2.get())
        number2=int(self.txtfld3.get())
        answer=number1-number2
        self.txtfld4.insert(END,str(answer))

    def multiply(self):
        self.txtfld4.delete(0, 'end')
        number1=int(self.txtfld2.get())
        number2=int(self.txtfld3.get())
        answer=number1*number2
        self.txtfld4.insert(END,str(answer))

    def div(self):
        self.txtfld4.delete(0, 'end')
        number1=int(self.txtfld2.get())
        number2=int(self.txtfld3.get())
        answer=number1/number2
        self.txtfld4.insert(END,str(answer))





mywin =MyWindow(window)

window.mainloop()