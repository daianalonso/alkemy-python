import download
import connect
import process
from logging_config import log
from utils import *

log.info('Descargando archivos fuente')
download.descargar_csv(URL_BIBLIOTECAS, 'bibliotecas')
download.descargar_csv(URL_MUSEOS, 'museos')
download.descargar_csv(URL_CINES, 'cines')

log.info('Procesando datos y creando tablas')
process.procesar_datos()

log.info('Conectando con base de datos y subiendo tablas')
connect.subir_tablas()

log.info('Ejecución finalizada con éxito')