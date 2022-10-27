#Copia el ejercicio anterior y realicemos una modificación:

#Junto al método init y calificación, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

#def __str__(self): return "Lo que quiero mostrar"
 

#Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).
 


#Implementa el método str y haz que muestre el nombre y la nota del alumno
#Crea algun objeto de la clase Alumno
#Realiza print de esos objetos para visualizar por pantalla la información del str

class Alumno():
    def __init__ (self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print("El alumno {} se ha agregado con éxito".format(self.nombre))

    def __str__(self):
        return ("El alumno {} ha sacado una nota de {}".format(self.nombre, self.nota))

    def calificacion(self):
        if self.nota < 5:
            print("El alumno {} ha suspendido con un {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha aprobado con una nota de {}".format(self.nombre, self.nota))    
Alumno1=Alumno("Elena", 8)
Alumno1.calificacion()
print(Alumno1) 

Alumno2=Alumno("Paula",2)
Alumno2.calificacion()
print(Alumno2)

Alumno3=Alumno("Rubén", 7)
Alumno3.calificacion()
print(Alumno3) 

Alumno4=Alumno("Daniel", 4)
Alumno4.calificacion()
print(Alumno4) 
