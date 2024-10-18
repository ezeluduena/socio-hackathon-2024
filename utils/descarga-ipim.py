import requests
import os

os.makedirs('data/ipim', exist_ok=True)
os.chdir('data/ipim')

# Datos de 2015 a 2019
url = 'https://www.indec.gob.ar/ftp/cuadros/economia/indice_ipim.csv'
csv = requests.get(url)
with open('indice_ipim_2016_2019.csv', 'wb') as f:
    f.write(csv.content)
    print('Descargado indice_ipim_2016_2019.csv')
    print('Listo indice_ipim_2016_2019.csv')
    print('------------------------------------')

# Datos de 1996 a 2014
url = 'https://www.indec.gob.ar/ftp/cuadros/economia/sipm-dde1996.xls'
xls = requests.get(url)
with open('sipm_1996_2014.xls', 'wb') as f:
    f.write(xls.content)
    print('Descargado sipm_1996_2014.xls')
    print('Listo sipm_1996_2014.xls')
    print('------------------------------------')

print('Descarga finalizada')
