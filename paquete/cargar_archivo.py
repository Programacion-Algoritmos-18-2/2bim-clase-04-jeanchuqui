import codecs

class ReadFichero:
    def __init__(self):
        self.archivo = codecs.open("paquete\informacion.csv","r")

    def obtener_informacion(self):
        return self.archivo.readlines()
    def cerrar_archivo(self):
        self.archivo.close()


class WriteFichero:

    def __init__(self):
        self.archivo = codecs.open("paquete/info_resumida.csv","w")


    def agregar_informacion(self, a):
        self.archivo.write("%s-%s-%d-%d\n" % (a.getNombre(), a.getCiudad(), a.getCampeonatos(), a.getPart_totales()))


    def cerrar_archivo(self):
        self.archivo.close()
        print("\n\t---GUARDADO---\n")