from tkinter import *
import functools

class main:
    def __init__(self):
        
        self.master = root
        self.master.title('Smart buttons')
        self.master.geometry('400x400')
        self.n = 1
        self.button = Button(self.master, text = 'Add button',
                             command = self.createbutton)
        self.button.pack(side = TOP)
        self.sp = []
        self.label = Label(self.master)
        self.label.configure(text = 'null')
        self.label.pack(side = BOTTOM)
        self.master.mainloop()

    def createbutton(self):
        global nomer
        nomer += 1
        n = nomer
        def callback(number):
            print ("button = ", number)
            self.label["text"] = str(number)
            global tek_nom
            tek_nom = number
        self.button = Button(root, text = str(nomer), command = lambda: callback(n)).pack(side =TOP)
        z = self.button
        self.sp.append(z)
tek_nom = 0
nomer = 0
root = Tk()
main()
