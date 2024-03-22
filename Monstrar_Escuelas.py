from Crear_Escuelas import *

def monstrar_escuelas(opci):
    sch.formateo()
    print("\n\n")
    if len(escuelas[opci]) <= 0:
        print("\n\n|~~| En Este Nivel No Hay Escuelas |~~|\n\n")
    for i in range(len(escuelas[opci])):
        print("{nmr}-) {escuela}".format(nmr = i+1, escuela = escuelas[opci][i]))
    test = input('\n\n| ~~~~~~ Presiona ENTER Para Salir ~~~~~~ |')
    sch.formateo()

def menu_Monstrar():
    while True:

        try:

            print("| ~~~~~~~~~~~ Monstrar Escuelas ~~~~~~~~~~~ |")

            print("|~~~~~~ Ingresa el Nivel de la Escuela ~~~~~~|")
            
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

            for nivel in range(len(niveles)):
                print("|~~~| {level}-) {nivel} ".format(nivel = niveles[nivel], level = nivel+1))
            
            print("\n|~~~| 0-) SALIR")

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

            opci = int(input('~~~>  '))

            if (opci <= len(niveles) and opci > 0):
                sch.formateo()
                match opci:
                    case 1:
                        monstrar_escuelas(opci)
                    case 2:
                        monstrar_escuelas(opci)
                    case 3:
                        monstrar_escuelas(opci)
            elif opci == 0:
                sch.formateo()
                break
            else:
                raise TypeError

        except:
            sch.formateo()
            print("\n|~~~| Ingrese una Opcion Valida |~~~|\n".upper())

