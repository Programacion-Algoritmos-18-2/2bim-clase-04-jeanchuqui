class Equipos(object):

    def __init__(self,nombres,ciudad,part_jugados,part_totales):
        self.nombre = nombres
        self.ciudad=ciudad
        self.campeonatos=part_jugados
        self.numJugadores=part_totales

    def setNombre(self,nombres):
        self.nombre=nombres
    def getNombre(self):
        return self.nombre

    def setCiudad(self,ciudad):
        self.ciudad=ciudad
    def getCiudad(self):
        return self.ciudad

    def setCampeonatos(self,part_jugados):
        self.campeonatos=part_jugados
    def getCampeonatos(self):
        return self.campeonatos

    def setPart_totales(self,part_totales):
        self.numJugadores=part_totales
    def getPart_totales(self):
        return self.promedio

    def __str__(self):
        cadena = "\n\nEquipo:  %s - %s \n - %d - %d" % (self.nombre, self.ciudad, self.campeonatos, self.numJugadores)
        return cadena
    def __repr__(self):
        cadena = "\n\nEquipo:  %s - %s \n - %d - %d" % (self.nombre, self.ciudad, self.campeonatos, self.numJugadores)
        return cadena


class Operaciones(object):

    def __init__(self, listado):
        self.lista_equipos = listado

    def ordenar(self, opcion):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)
        """

        if opcion == "nombre":
            return sorted(self.listado_equipos, key=lambda equipo: equipo.nombre)
        elif opcion == "campeonatos":
            return sorted(self.listado_equipos, key=lambda equipo: equipo.campeonatos)
