import os

class Escuela:
    
    def __init__(self, nombre, nivel, numero_de_estudiantes=None):

        self.nombre = nombre
        self.nivel = nivel
        self._numero_de_estudiantes = numero_de_estudiantes

    def get_name(self):

        return self.nombre
    
    def get_nivel(self):

        return self.nivel
    
    def get_students(self):

        return self._numero_de_estudiantes
    
    def set_students(self, nmr_estudiante):
        if isinstance(nmr_estudiante, int):
            self._numero_de_estudiantes = nmr_estudiante
        else:
            raise TypeError

    def __repr__(self):
        return "Escuela {nivel} llamada {nombre} cuenta con {numeroDeEstudiantes} estudiantes".format(nivel = self.get_nivel(), nombre = self.get_name(), numeroDeEstudiantes = self.get_students())





class Primaria(Escuela):
    
    def __init__(self, nombre, politica, nivel = 'Primaria', numero_de_estudiantes=None):
        super().__init__(nombre, nivel, numero_de_estudiantes)
        self.politica = politica

    def get_politicaDeRetiro(self):
        return "Retirar después de las {retiro}".format(retiro = self.politica)
    
    def __repr__(self):
        result = super().__repr__() + ' | Hora de Retiro {retiro}'.format(retiro = self.politica)
        return result




class Intermedio(Escuela):

    def __init__(self, nombre, nivel = 'Intermedio', numero_de_estudiantes=None):
        super().__init__(nombre, nivel, numero_de_estudiantes)




class Secundaria(Escuela):

    def __init__(self, nombre, equipos, nivel = 'Secundaria', numero_de_estudiantes=None):
        super().__init__(nombre, nivel, numero_de_estudiantes)
        self.equipos = equipos

    def get_equiposDeportivos(self):

        result = '| '

        for equipo in list(self.equipos):
            result += equipo + ' | '

        return result
    
    def __repr__(self):
        result = super().__repr__() + ' | Equipos deportivos: {equipos}'.format(equipos=self.get_equiposDeportivos())
        return result


def formateo():
    return os.system('cls' if os.name == 'nt' else 'clear')