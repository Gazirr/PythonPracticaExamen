

# Caso 1:
'''
file = open('data.txt', 'r')
lineas = file.readlines()
print(lineas)
file.close()
'''

# Caso 2:
'''
with open('data2.txt','r') as archivo:
    lineas = archivo.readlines()
    
    for l in lineas:
        print(l.replace("\n", " "))
'''

# Caso 3:
'''
with open('data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)
'''

# Caso 4:
'''
with open('data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    pos = archivo.tell()
    print(pos)
    print('El archivo tiene {0} caracteres de longitud'.format(pos))
'''

