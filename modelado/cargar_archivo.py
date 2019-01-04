import codecs

class ReadFichero:
    def __init__(self):
        self.archivo = codecs.open("modelado\informacion.csv","r")

    def obtener_informacion(self):
        return self.archivo.readlines()
    def cerrar_archivo(self):
        self.archivo.close()

class WriteFichero:

    def __init__(self):
        self.archivo = codecs.open("modelado/info_resumida.txt","a")

    def agregar_informacion(self, a):
        self.archivo.write(" ")

    def cerrar_archivo(self):
        self.archivo.close()
        print("\n\t---GUARDADO---\n")