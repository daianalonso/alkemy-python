import os 
import requests
from logging_config import log
from utils import *
from datetime import date

# Almaceno la fecha de descarga de los archivos
hoy = date.today()

def descargar_csv(url, categoria):
    '''
    Descarga el csv desde la url pasada por parámetro, guardándolo en la ruta de archivo correspondiente a su categoría y
    fecha de descarga.
    '''
    try:
        # Especifico la carpeta donde guardar la descarga
        carpeta = categoria + '/' + str(hoy.year) + '-' + meses[hoy.month]
        
        # Si no existe la carpeta, la creo
        if not os.path.exists(carpeta):
                os.makedirs(carpeta)
        
        # Creo la ruta con el nombre de archivo 
        filename = carpeta + '/' + categoria + '-' + str(hoy.day) + '-' + str(hoy.month) + '-' + str(hoy.year) + '.csv'

        # Descargo el archivo y lo guardo en esa ruta
        req = requests.get(url)
        url_content = req.content
        csv_file = open(filename, 'wb')
        csv_file.write(url_content)
        csv_file.close()

        log.info('Se realizó la descarga de los archivos')
        
    except Exception as e:
        log.error('No se pudo completar la descarga de los archivos')
        print(f'Error al realizar la descarga: {e}')

if __name__ == "__main__":
    descargar_csv(URL_BIBLIOTECAS, 'bibliotecas')
    descargar_csv(URL_MUSEOS, 'museos')
    descargar_csv(URL_CINES, 'cines')
