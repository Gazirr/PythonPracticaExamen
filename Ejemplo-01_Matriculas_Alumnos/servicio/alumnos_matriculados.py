from dominio.alumnos import Alumno

class AlumnosMatriculados:
    
    archivo = "/root/misCosas/PythonPracticaExamen/Ejemplo-01_Matriculas_Alumnos/alumnos.txt"
    
    @staticmethod
    def matricular_alumnos(alumno : Alumno):
        with open(AlumnosMatriculados.archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{alumno.name}\n")
            
    @staticmethod
    def listar_alumnos():
        try:
            with open(AlumnosMatriculados.archivo, 'r') as archivo:
                 return archivo.readlines()
        except FileNotFoundError:
            return[]
        
    @staticmethod
    def eliminar_alumnos(alumno: Alumno): 
        with open(AlumnosMatriculados.archivo, 'r', encoding= 'utf-8') as archivo:
            lineas = archivo.readlines()
        eliminado = False
        with open(AlumnosMatriculados.archivo, 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                if linea.strip() == alumno:
                    eliminado = True
                else:
                    archivo.write(linea)
        if eliminado:
            print("El alumno  ha sido eliminado")
        else:
            print("El alumno  no se ha encontrado")