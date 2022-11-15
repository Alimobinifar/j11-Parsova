
from tkinter import * 
from tkinter import ttk

class PhoneNumber:
    def __init__(self):
        self.form = Tk()
        self.phone_number()
        self.form.mainloop()
    
    def phone_number(self):
        phone_entry = Entry(self.form).place(x=35,y=10)
        save_btn = Button(self.form,text="Save Phone").place(x=50,y=40)

x = PhoneNumber()