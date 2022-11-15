

from tkinter import * 
from tkinter import ttk

class PhoneNumber:
    def __init__(self):
        self.form = Tk()
        self.phone_number()
        self.form.mainloop()
    
    def save(self,phone_number):
            with open('C:/Users/p43/Desktop/phones.txt','a') as p :
                 p.write(phone_number+"\n")
             
    def phone_number(self):
        number=StringVar()
        phone_entry = Entry(self.form,textvariable=number).place(x=35,y=10)
        
        save_btn = Button(self.form,text="Save Phone",
                 command=lambda:self.save(number.get())).place(x=50,y=40)


    

numbers = PhoneNumber()
