print("Programacion POO")
# Definicion de objeto
class Perro:
    # Funciones dentro de la clas
    def morder(self):
        print("El perro me mordio")
    def Datos_Perro(self,nombre,edad):
        print(f" Nombre: {nombre} Edad: {edad}")
        

# Zona de creacion de objeto
pitbull=Perro()

# Zona de uso de objetos

pitbull.Datos_Perro("boby", 4)
pitbull.morder()