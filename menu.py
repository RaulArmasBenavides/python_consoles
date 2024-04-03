import keyboard

selected = 1

def show_menu():
    global selected
    print("\n" * 30)  # Limpia la pantalla.
    print("Menú interactivo:")
    print("Elige una opción usando las flechas hacia arriba/abajo y presiona Enter para seleccionar.")
    for i in range(1, 5):
        prefix = "->" if selected == i else "  "
        print("{prefix} Opción {i}. Hacer algo {i}".format(prefix=prefix, i=i))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()

def select_option():
    print(f"\nHas seleccionado la Opción {selected}. ¡Haciendo algo interesante!\n")
    # Aquí puedes añadir código para manejar cada selección de manera específica.
    if selected == 4:
        print("Seleccionaste salir. ¡Adiós!")
        exit()  # Sale del programa.

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', select_option)  # Agrega la tecla Enter para seleccionar una opción.

keyboard.wait('esc')

