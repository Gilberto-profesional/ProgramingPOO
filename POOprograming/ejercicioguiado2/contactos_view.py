import tkinter as tk
import tkinter.messagebox as mb


#Create a form

class ContactosForm(tk.LabelFrame):
    campos=["Last Name","First Name","Email","Phone"]

    def __init__(self,master,**kwargs):
        super().__init__(master,text="Contacts",padx=10,pady=10,**kwargs)
        self.frame=tk.Frame(self)
        self.frame.pack()
        self.entries=list(map(self.create_campos,enumerate(self.campos)))
        


    def create_campos(self,campo):
        position,text=campo
        label=tk.Label(self.frame,text=text)
        entry=tk.Entry(self.frame)
        label.grid(row=position,column=0, pady=10)
        entry.grid(row=position,column=1, pady=10)
        return entry
        
class ContactoNew(tk.Toplevel):

    def __init__(self,parent):
        super().__init__(parent)
        self.form=ContactosForm(self)
        self.form.pack(padx=10,pady=10)
        self.button_add=tk.Button(self,text="Agregar contacto",command=self.confirm)
        self.button_add.pack(padx=10,pady=10)

    def confirm(self):
        print("Confirm contact")    
       
    def show(self):
        self.grab_set()
        self.wait_window() 

 

#Create a window

class ContactosView(tk.Tk):
    def __init__(self):
        #Permite utilizar todo lo de la clase padre
        super().__init__()
        self.title("Lista de contactos")
        self.geometry("400x400")
        self.button_new=tk.Button(self, text="New Contact")
        self.button_new.pack(side=tk.BOTTOM,padx=10,pady=10)

    def set_controller(self,controller):
        self.button_new.config(command=controller.create_contact) 

       
