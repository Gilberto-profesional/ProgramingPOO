import tkinter as tk
import tkinter.messagebox as mb

#Create a window
class ContactosView(tk.Tk):
    def __init__(self):
        #Permite utilizar todo lo de la clase padre
        super().__init__()
        self.title("Lista de contactos")
        self.geometry("400x400")
        self.button_new=tk.Button(self, text="New Contact")
        self.button_new.pack(side=tk.BOTTOM,padx=10,pady=10)
