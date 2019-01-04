from modelado.Equipos import *
from modelado.cargar_archivo import *

x = ReadFichero()
y = WriteFichero()

lista = x.obtener_informacion()
lista = [l.split("|") for l in lista]

lista_equipos = []

for z in lista:
    e = Equipos(z[0], z[1], z[2], z[3])
    lista_equipos.append(e)
x.cerrar_archivo()

print("Como desea ordenar los archivos?")
opcion=input("(nombre) - (campeonatos)")

operacion = Operaciones(lista_equipos)
for o in lista_equipos:
    y.agregar_informacion(o)
y.cerrar_archivo()


