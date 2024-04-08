from collections import OrderedDict
import datetime
import peewee as pw

db = pw.SqliteDatabase('diary.db')


menu_items = OrderedDict([
    ('a', 'add_entry'),
    ('v', 'view_entries'),
    ('d', 'delete_entry'),
    ('s', 'search_entries')
])
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Entry],safe=True)


def menu_loop():
    """Show menu"""
    choice= None 
    while choice !='q':
        print("Press 'q' to quit")
        for key,value in menu.items():
            print("{}){}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    """Agregar una nueva entrada."""
    print("Escribe tu entrada. Presiona 'ctrl+d' cuando termines.")
    data = input()
    if data:
        if input('Guardar entrada? [Yn] ').lower() != 'n':
            Entry.create(content=data)
            print("Guardado exitosamente!")
def view_entries(delete=False):
    """Ver todas las entradas."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp))
        print('n) siguiente entrada')
        print('d) borrar entrada')
        print('q) volver al menú principal')

        next_action = input('Acción: [Nq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd' and delete:
            delete_entry(entry)

def delete_entry(entry):
    """Eliminar una entrada existente."""
    if input("¿Estás seguro? [yN] ").lower() == 'y':
        entry.delete_instance()
        print("Entrada borrada.")
if __name__ == "__main__":
    create_and_connect()
    menu_loop()