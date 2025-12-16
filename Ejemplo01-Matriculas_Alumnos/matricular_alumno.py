from dominio.alumno import Alumno
from servicio.matriculas_alumnos import Matriculas_Alumnos


def menu():
    while True:
        print("----Matricular Alumno---")
        print("----1.- Añadir Alumno----")
        print("----2.- Listar Alumno----")
        print("----3.- Eliminar Alumno----")
        print("----4.- Salir----")

        opcion = input("Elije una Opcion ")

        if opcion == "1":
            nombre = input("Escribe el nombre del Alumno: ")
            alumno = Alumno(nombre)
            Matriculas_Alumnos.añadir_Alumnos(alumno)
            print(f"El alumno {alumno} ha sido añadido")

        elif opcion == "2":
            alumnos = Matriculas_Alumnos.listar_Alumno()
            if  alumnos:
                for alumno in alumnos:
                    print(f"- {alumno.strip()}")
            else:
                print("No hay alumnos")

        elif opcion == "3":
            nombre = input("Escribe el nombre del Alumno: ")
            alumno = Alumno(nombre)
            Matriculas_Alumnos.eliminar_Alumno(alumno)
            print(f"El alumno {alumno} ha sido eliminado")

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de Nuevo")

if __name__ == "__main__":
    menu()