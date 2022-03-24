from utils import *
import download
import connect
import process

download.descargar_csv(URL_BIBLIOTECAS, 'bibliotecas')
download.descargar_csv(URL_MUSEOS, 'museos')
download.descargar_csv(URL_CINES, 'cines')

process.procesar_datos()

connect.subir_tablas()