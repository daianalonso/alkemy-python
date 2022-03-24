from decouple import config
import pandas as pd
from sqlalchemy import create_engine, Date, String, Integer

# Me conecto a base de datos PostgreSQL usando sqlalchemy
engine = create_engine('postgresql+psycopg2://' + config('DB_USER') + ':' + config('DB_PASSWORD') + '@' + config('DB_HOST') + ':' + config('DB_PORT') + '/'+ config('DB_NAME'))

def subir_tablas():
    '''
    Se conecta a la base de datos y se actualiza con las tablas creadas
    '''
    # Obtengo la tabla conjunta
    df_conjunta = pd.read_csv('df_conjunto.csv')

    # Subo la tabla a la base de datos
    df_conjunta.to_sql('datos_conjuntos', con=engine, if_exists='replace', index=False, dtype={
        'cod_localidad':String, 'id_provincia':String, 'id_departamento':String, 'categoria':String,
        'provincia':String, 'localidad':String, 'nombre':String, 'domicilio':String, 'código postal':String,
        'número de teléfono':String, 'mail':String, 'web':String, 'fecha_carga':Date})

    # Obtengo la tabla de cantidad de registros
    df_registros = pd.read_csv('df_cantidad_registros.csv')

    # Subo la tabla a la base de datos
    df_registros.to_sql('cantidad_registros', con=engine, if_exists='replace', index=False, dtype={
        'categoría':String, 'total por categoría':Integer, 'fuente':String, 'total por fuente':Integer, 'provincia':String, 
        'categorías por provincia':Integer, 'fecha_carga':Date})

    # Obtengo la tabla de salas de cine
    df_cines = pd.read_csv('df_cines.csv')

    # Subo la tabla a la base de datos
    df_cines.to_sql('info_cines', con=engine, if_exists='replace', index=False, dtype={
        'provincia':String, 'pantallas':Integer, 'butacas':Integer, 'espacios_INCAA':Integer, 'fecha_carga':Date})

if __name__ == '__main__':
    subir_tablas()