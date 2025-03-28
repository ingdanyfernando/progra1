global opcion,perro1
import time
import os

class perro:
    nombre = ""
    raza = ""
    color = ""
    peso = ""
    edad = ""
    def __init__(self):
        pass
        print("Perro listo para agregar datos")
    def AgregarPerro(self, nom,raz,col,pes,eda):
        self.nombre = nom
        self.raza = raz
        self.color = col
        self.peso = pes
        self.edad = eda
        print("Perro Agregado satisfactoriamente")
    def __str__(self):
        return f"{self.nombre}\t"+f"{self.raza}"+f"{self.color}"

ListaPerros=[]

def menu():
    global opcion
    global perro1
    print("1.Crear perro")
    print("2. Agregar Datos Perro")
    print("3. Listar perros")
    print("4. Salir")
    print("Ingrese el numero de opcion que desea:")
    opcion = int(input())
    if opcion == 1:
        perro1 = perro()
        time.sleep(0.8)
        return True
    elif opcion == 2:
        nombre = input("Ingrese nombre del perro")
        raza = input("Ingrese la raza:")
        color = input("Ingrese color del perro:")
        peso = int(input("Ingrese el peso"))
        edad = int(input("Ingrese la edad"))
        perro1.AgregarPerro(nombre,raza,color,peso,edad)
        ListaPerros.append(perro1)
        time.sleep(0.9)
        return True
    elif opcion == 3:
        os.system("cls")
        print("NOMBRE\tRAZA\tCOLOR")
        print("-"*30)
        for i in ListaPerros:
            print(i)       
        time.sleep(1)
        return True
    else:
        return False    
    
while(menu()!=False):
    menu()