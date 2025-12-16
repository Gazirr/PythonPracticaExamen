import csv
import os

notas_UF1_UF2 = {}
base_path = os.path.dirname(__file__)
Notas_Alumnos_UF1 = os.path.join(base_path,'Notas_Alumnos_UF1.csv')
Notas_Alumnos_UF2 = os.path.join(base_path,'Notas_Alumnos_UF2.csv')
with open (Notas_Alumnos_UF1, newline='', encoding ='utf-8-sig') as notas1:
    reader = csv.DictReader(notas1, delimiter= ';')
    reader.fieldnames = [fn.replace('\ufeff', '').strip() for fn in reader.fieldnames]
    for row in reader:
        row = {k.strip(): v.strip() for k,v in row.items()}
        alumno_id = row['Id']
        notas_UF1_UF2[alumno_id] = {
            'Id': alumno_id,
            'Nombre': row['Nombre'],
            'Apellido': row['Apellidos'],
            'Nota_UF1': row['UF1'],
            'Nota_UF2': ''
        }

with open (Notas_Alumnos_UF2, newline='', encoding='utf-8-sig') as notas2:
    reader = csv.DictReader(notas2, delimiter=';')
    reader.fieldnames = [fn.replace('\ufeff', '').strip() for fn in reader.fieldnames]
    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items()}
        alumno_id = row['Id']
        if alumno_id in notas_UF1_UF2:
            notas_UF1_UF2[alumno_id]['Nota_UF2'] = row['UF2']
        else:
            notas_UF1_UF2[alumno_id] = {
                'Id' : alumno_id,
                'Nombre': row['Nombre'],
                'Apellido': row['Apellidos'],
                'Nota_UF1': '',
                'Nota_UF2': row['UF2']
            }
            

with open("notas_total.csv", "w", newline="", encoding="utf-8-sig") as notas_totales:
    campos = ["Id", "Nombre", "Apellido", "Nota_UF1", "Nota_UF2"]
    writer = csv.DictWriter(notas_totales, fieldnames=campos)
    writer.writeheader()
    for alumno in notas_UF1_UF2.values():
        writer.writerow(alumno)
