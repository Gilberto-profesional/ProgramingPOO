from contactos_view import ContactosView, ContactosForm,ContactoNew


class ContactosController(object):
    def __init__(self,view):
        self.view=view

    def create_contact(self):
        print("Funcion create_contact") 
        nuevo_contacto=ContactoNew(self.view).show()

    def star(self):
        self.view.mainloop()