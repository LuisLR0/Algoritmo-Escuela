import os

from Monstrar_Escuelas import *
from Crear_Escuelas import *


sch.formateo()

while True:

    print('''
|~~~~~~~~~~~   Opciones   ~~~~~~~~~~~|
|                                    |
|                                    |
|   1-) Crear Escuelas               |
|                                    |
|   2-) Monstrar Escuelas            |
|                                    |
|   0-) Salir                        |
|                                    |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
''')
        
    opc = input("\n ~~> ")

    match opc:
        case '1':
            sch.formateo()
            menu_Crear()
        case '2':
            sch.formateo()
            menu_Monstrar()
            pass
        case '0':
            sch.formateo()
            break
        case _:
            sch.formateo()
