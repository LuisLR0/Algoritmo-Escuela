import School_Catalogue as sch

niveles = ['Primaria', 'Intermedio', 'Secundaria']
escuelas = { 1: [], 2: [], 3: []}

sch.formateo()

def Ingresar_datos(nivel, opcion):

    sch.formateo()

    while True:

        nombre = input("|~~| Ingrese el nombre de la escuela: ")

        sch.formateo()

        while True:
            try:
                nmr_estudiantes = int(input("|~~| Ingrese el Numeros de Estudiantes: "))
                if isinstance(nmr_estudiantes, int):
                    break
            except:
                sch.formateo()
                print("|~~| Ingresa Solamente Numeros |~~|\n\n".upper())
        
        if nivel is sch.Primaria:
            index = 0

            politica = input("|~~| Ingresa a que hora se retiran: ")
            escuelas[opcion].append(nivel(nombre, politica))
            escuelas[opcion][index].set_students(nmr_estudiantes)

            index += 1

        elif nivel is sch.Secundaria:
            equipos = []
            index = 0

            while True:
                sch.formateo()
                print("|~~| Ingresar equipos Deportivos | Ingresa 0 Para Salir |~~|")
                equipo = input("|~~| Ingresa Equipo: ")
                if equipo == '0':
                    break
                else:
                    equipos.append(equipo)
                
            escuelas[opcion].append(nivel(nombre, equipos))
            escuelas[opcion][index].set_students(nmr_estudiantes)

            index += 1

        else:
            index = 0

            escuelas[opcion].append(nivel(nombre))
            escuelas[opcion][index].set_students(nmr_estudiantes)

            index += 1

        sch.formateo()
        break

def menu_Crear():
    while True:

        try:

            print("| ~~~~~~~~~~~ Crear Escuelas ~~~~~~~~~~~ |")

            print("|~~~~ Ingresa el Nivel de la Escuela ~~~~|")
            
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

            for nivel in range(len(niveles)):
                print("|~~~| {level}-) {nivel} ".format(nivel = niveles[nivel], level = nivel+1))
            
            print("\n|~~~| 0-) SALIR")

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

            opcion = int(input('~~~>  '))

            if (opcion <= len(niveles) and opcion > 0):
                sch.formateo()
                match opcion:
                    case 1:
                        Ingresar_datos(sch.Primaria, opcion)
                    case 2:
                        Ingresar_datos(sch.Intermedio, opcion)
                    case 3:
                        Ingresar_datos(sch.Secundaria, opcion)
            elif opcion == 0:
                sch.formateo()
                break
            else:
                raise TypeError

        except:
            sch.formateo()
            print("\n|~~~| Ingrese una Opcion Valida |~~~|\n".upper())
