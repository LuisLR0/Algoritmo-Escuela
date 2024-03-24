import json
import sqlite3 as sq
import School_Catalogue as sch

co = sq.connect('Escuelas.db')
curs = co.cursor()

def cargar_datos(escuelas, niveles):
    for i in range(1, 4):
        selectALL = curs.execute(f'SELECT * FROM {niveles[i-1]}').fetchall()

        for a in range(len(selectALL)):
            match i:
                case 1:
                    escuelas[i].append(sch.Primaria(selectALL[a][1], selectALL[a][3]))
                    escuelas[i][a].set_students(selectALL[a][2])
                case 2:
                    escuelas[i].append(sch.Intermedio(selectALL[a][1]))
                    escuelas[i][a].set_students(selectALL[a][2])
                    pass
                case 3:
                    escuelas[i].append(sch.Secundaria(selectALL[a][1], json.loads(selectALL[a][3])))
                    escuelas[i][a].set_students(selectALL[a][2])
                    print(len(escuelas[3]))
                    pass