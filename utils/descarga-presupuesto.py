# Script para descargar y descomprimir los archivos de créditos presupuestarios
# acumulados por año desde 1995 hasta 2024
import requests
import os
import zipfile

# Crear la carpeta "credito-anual" si no existe
if not os.path.exists('../credito-anual'):
    os.makedirs('../credito-anual')
os.chdir('../credito-anual')

# Descargar y descomprimir los archivos .zip
for year in range(1995, 2025):
    url = f'https://dgsiaf-repo.mecon.gob.ar/repository/pa/datasets/{
        year}/credito-anual-{year}.zip'
    zip = requests.get(url)
    with open(f'credito-anual-{year}.zip', 'wb') as f:
        f.write(zip.content)
        print(f'Descargado credito-anual-{year}.zip')
        with zipfile.ZipFile(f'credito-anual-{year}.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
        print(f'Descomprimido credito-anual-{year}.zip')

        os.remove(f'credito-anual-{year}.zip')
        print(f'Eliminado credito-anual-{year}.zip')
        print(f'Listo credito-anual-{year}.csv')
        print('------------------------------------')

print('Descarga y descompresión finalizada')
