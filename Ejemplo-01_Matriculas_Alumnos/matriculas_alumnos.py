from dominio.alumnos import Alumno
from servicio.alumnos_matriculados import AlumnosMatriculados


def menu():
    
    while True:
        print("----Matricular Alumnos Ejemplo 01----")
        print("----1.- Añadir Alumnos----")
        print("----2.- Listar Alumnos----")
        print("----3.- Eliminar Alumnos----")
        print("----Salir----")
            
        opcion = input("Elije una opcion: ")
            
        if opcion == "1":
                nombre = input("Introduce el nombre del Alumno: ")
                alumno = Alumno(nombre)
                AlumnosMatriculados.matricular_alumnos(alumno)
                print(f"El {alumno} ha sido agregado")
        elif opcion == "2":
                alumnos = AlumnosMatriculados.listar_alumnos()
                if alumnos:
                    print("Alumnos Matriculados:")
                    for alumno in alumnos:
                        print(alumno.strip("\n"))
                else:
                    print("no hay alumnos")
        
        elif opcion == "3":
                nombre = input("Introduce el nombre del Alumno: ")
                alumno = Alumno(nombre)
                AlumnosMatriculados.eliminar_alumnos(alumno)
                print(f"El {alumno} ha sido eliminado")
            
if __name__ == "__main__":
    menu()
                        
            