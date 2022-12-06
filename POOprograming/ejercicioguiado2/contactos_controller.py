from contactos_view import ContactosView, ContactosForm,ContactoNew

class ContactosController(object):
    def __init__(self,repo,view):
        self.selection=None
        self.repo=repo
        self.view=view
        self.contacts=list(repo.get_contacts())

    def create_contact(self):
        print("Funcion create_contact") 
        nuevo_contacto=ContactoNew(self.view).show()

        if nuevo_contacto:
            contact=self.repo.add_contact(nuevo_contacto)
            self.contacts.append(contact)
            self.view.add_contact(contact)

    #Add a update contact form
    def update_contact(self):
        if not self.selection:
            return
        else:
            rowid=self.contacts[self.selection].rowid
            update_contact=self.view.get_data()
            update_contact.rowid=rowid
            contac=self.repo.update_contact(update_contact)
            self.contacts[self.selection]=contac
            self.view.update_contact(contac,self.selection)
            print("Funcion update_contact")


    def select_contact(self,index):
        print("Funcion selecect_contact")
        self.selection=index
        contact=self.contacts[index]
        self.view.load_details(contact)    

    def delete_contact(self):
        if not self.selection:
            return
        else:
            contact=self.contacts[self.selection]
            self.repo.delete_contact(contact)
            self.view.remove_contact(self.selection)   
            print("Funcion delete_contact")

    def star(self):
        for c in self.contacts:
            self.view.add_contact(c)
        self.view.mainloop()