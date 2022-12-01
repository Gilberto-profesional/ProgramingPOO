import sqlite3
from contactos_view import ContactosView
from contactos_controller import ContactosController 

def main():
    with sqlite3.connect("contactos.db") as conn:
        c=conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contactos' ''')
        if c.fetchone()[0]==1 :
            print("La tabla contactos ya existe.")
            view = ContactosView()
            controller = ContactosController(view)
            view.set_controller(controller)
            controller.star()
            
        else:
            c.execute('''CREATE TABLE contactos(
                last_name text,
                first_name text,
                email text,
                phone text
                )''')
            print("La tabla contactos ha sido creada.")    

if __name__ == "__main__":
    main()   