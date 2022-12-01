from contactos_view import contactosView

class ContactosController(object):
    def __init__(self,view):
        self.view=view
        
    def star(self):
        self.view.mainloop()