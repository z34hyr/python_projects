# для установки модуля minimalmodbus (и вообще любого требуемого модуля)
# 1. открыть консоль виндувс (win+r) далее cmd
# 2. pip install minimalmodbus
import minimalmodbus
import serial
import time
from tkinter import *
import functools
mb = minimalmodbus
mb.BAUDRATE = 19200
mb.BYTESIZE = 8
mb.PARITY = "O"
mb.STOPBITS = 1
mb.TIMEOUT = 0.05
listbox_items = [9600, 19200, 115200]
curr_speed = 0
lbl = ""
#mb.Instrument("COM3", 1, "rtu")
class main:
    def __init__(self):
        self.master = root
        self.master.title("Modbus RTU - найди свою плату")
        self.master.geometry('500x220')
# группа 1 - задание скорости
##############################
        # заголовок окна задания скорости
        self.labl_speed = LabelFrame(self.master,
                               text = "задайте скорость ",
                               width = 40, height = 5,
                               )
        self.labl_speed.grid(row = 1, column = 1)
##############################
        # список со скоростями
        self.listbox = Listbox(self.labl_speed,
                               width = 30,
                               height = 4,)
        self.listbox.bind("<ButtonRelease-1>", self.select_item)
        for item in listbox_items:
            self.listbox.insert(END, item)
        self.listbox.grid(row = 2, column = 1)
##############################
        
##############################    
        # строка "выбранная сокрость" 
        self.label = Label(self.labl_speed,
                           text = "скорость по умолчанию: "+str(mb.BAUDRATE),)
        self.label.grid(row = 3, column = 1, sticky = "nw")

# группа 2 - звдвние номера COM-порта

        self.labl_COM = LabelFrame(self.master,
                                   text = "задайте номер порта ",
                                   width = 15, height = 5)
        self.labl_COM.grid(row = 1, column = 2, sticky = "nw")


        self.just_COM = Label(self.labl_COM,
                              text = "COM",
                              width = 5
                              )
        self.just_COM.grid(row = 2, column = 2, sticky = "e")
        self.curr_COM = Entry(self.labl_COM,
                              width = 5,)
        self.curr_COM.grid(row = 2, column = 3, sticky = "w")

        
        self.label_state = Label(self.labl_COM,
                                 text = "COM-порт: закрыт",
                                 )
        self.label_state.grid(row = 3, column = 2)

        
##############################
        # кнопка запуска поиска адреса
        self.label_empty = Label(self.master,
                                 text = "")
        self.label_empty.grid(row = 4, column = 2)
        self.button = Button(self.master,
                             text = "Начать поиск",
                             command = self.ret_number)
        self.button.grid(row = 5, column = 2, sticky = "we")
##############################
        self.label_result = Label(self.master,
                           text = "выберите номер порта\nи скорость")
        self.label_result.grid(row = 6, column = 2)
        

        
        
        self.master.mainloop()

        
        
    def select_item(self, event):
            value = (self.listbox.get(self.listbox.curselection()))
            self.label["text"] = "выбранная скорость: " + str(value)
            mb.BAUDRATE = value
            #print(mb.BAUDRATE)
    
    def ret_number(self):
        start_time = time.time()
        x = FALSE
        for i in range(1,248):
            try:
                COM = "COM" + self.curr_COM.get()
                plata = mb.Instrument(COM, i, "rtu")
                if x != TRUE:
                    print("идет поиск...")
                    
                x = TRUE
                self.label_state["text"] = "COM-порт: открыт"
                self.label_result["text"] = "не удалось открыть " 
                a = plata.read_register(3)
                print("answer is ", a)
                proc_time = time.time() - start_time 
                proc_time = str("{:.2f}".format(proc_time))
                self.label_result["text"] = "адрес платы = " + str(i) + "\nвремя на поиск - " + proc_time
                # type of a - list of int
                break
                print("поиск завершен за ", proc_time)
            except serial.serialutil.SerialException:
                print("не удается открыть " + COM)
                self.label_result["text"] = "не удалось открыть " + COM
                break
            except IOError:
                #self.label_result["text"] = "идет поиск..."
                if i == 247:
                    self.label_result["text"] = "на скорости " + str(mb.BAUDRATE) + "\nникто не ответил"
                    #close port
                #print("there is no answer")
                pass
        
    
        #if a == "5":
            #return a + " - right answer"
            #break
        #while not(answer) :
root = Tk()
main()
