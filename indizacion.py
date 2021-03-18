import os
import json

APP_FOLDER = 'C:\\Users\\Ary\\Documents\\GitHub\\Proyecto1RIT\\man.es\\man1'

totalFiles = 0
totalDir = 0

data = []

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    #for directories in dirs:
    #    totalDir += 1
    for File in files:
        with open(base + '\\' + File, 'r') as f:
            datosArchivo = f.read()
        totalFiles += 1
    listaDireccion = base.split('\\')
    data.append([listaDireccion[len(listaDireccion) - 1], base, len(files)])

print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))