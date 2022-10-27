#Crea una clase llamada Alumno que tenga los atributos nombre y nota
#Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
#Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota

#Crea algunos alumnos
#Prueba a ejecutar el método calificación de cada objeto que has creado


class Alumno():
    def __init__ (self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print("El alumno {} se ha agregado con éxito".format(self.nombre))

    def __str__(self):
        return ("El alumno  {}  ha sacado una nota de {}".format(self.nombre, self.nota))

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
