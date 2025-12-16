import csv
from pathlib import Path

notas_UF1_UF2 = {}
ruta = Path(__file__).parent
Notas_UF1 = ruta / "Notas_Alumnos_UF1.csv"

with open(Notas_UF1, 'r', newline='', encoding='utf-8') as Notas1:
    reader = csv.DictReader(Notas1, delimiter=';')
    reader.fieldnames = [fn.replace("\ufeff", '').strip() for fn in reader.fieldnames]
    for row in reader:
        row = {k.strip(): v.strip() for k,v in row.items()}
        alumno_id = row['Id']
        row[alumno_id] = {
            
        }