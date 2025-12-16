from dominio.alumno import Alumno
from  pathlib import Path
class Matriculas_Alumnos:
    ruta = Path(__file__).parents[1]

    archivo = ruta / "alumno.txt"
    
    @staticmethod
    def añadir_Alumnos(alumno: Alumno):
        with open(Matriculas_Alumnos.archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f"{alumno.nombre}\n")

    
    @staticmethod
    def listar_Alumno():
        try:
            with open(Matriculas_Alumnos.archivo, 'r', encoding='utf-8') as archivo:
                return archivo.readlines()
            
        except FileNotFoundError:
            return[]
    
    @staticmethod
    def eliminar_Alumno(alumno: Alumno):
        with open(Matriculas_Alumnos.archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        eliminado = False

        with open(Matriculas_Alumnos.archivo, 'w',encoding='utf-8') as f:
            for linea in lineas:
                if linea.strip() == alumno.nombre:
                    eliminado = True
                else:
                    f.write(linea)
        if eliminado:
            print("El alumno se ha eliminado")
        else:
            print("No se ha encontrado el alumno")
        