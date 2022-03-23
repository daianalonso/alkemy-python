import pandas as pd 
from datetime import date 
from src.utils import *

# Almaceno la fecha de descarga de los archivos
hoy = date.today()

def procesar_datos():
    '''
    Se normaliza toda la información de museos, salas de cine y bibliotecas, se crea una tabla todos los datos conjuntos.
    Se procesa la información de cines y se crea una tabla para luego poder extraer los datos requeridos. 
    '''

    # Cargo los datos del csv de bibliotecas
    carpeta = 'bibliotecas' + '/' + str(hoy.year) + '-' + meses[hoy.month]
    df_bibliotecas = pd.read_csv(carpeta + '/' + 'bibliotecas' + '-' + str(hoy.day) + '-' + str(hoy.month) + '-' + str(hoy.year) + '.csv', encoding='UTF-8')

    # Me quedo con las columnas de interés
    df_bibliotecas = df_bibliotecas[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad',
                                     'Nombre', 'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web', 'Fuente']]

    # Renombro las columnas
    df_bibliotecas.rename(
                        {'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoria',
                        'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal',
                        'Teléfono':'número de teléfono', 'Mail':'mail', 'Web':'web', 'Fuente':'fuente'}, inplace=True)

    # Cargo los datos del csv de salas de cine
    carpeta = 'cines' + '/' + str(hoy.year) + '-' + meses[hoy.month]
    df_cines = pd.read_csv(carpeta + '/' + 'cines' + '-' + str(hoy.day) + '-' + str(hoy.month) + '-' + str(hoy.year) + '.csv', encoding='UTF-8')

    # Me quedo con las columnas de interés
    df_cines = df_cines[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad',
                                     'Nombre', 'Dirección', 'CP', 'Teléfono', 'Mail', 'Web', 'Fuente']]

    # Renombro las columnas
    df_cines.rename(
                    {'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoria',
                    'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Dirección':'domicilio', 'CP':'código postal',
                    'Teléfono':'número de teléfono', 'Mail':'mail', 'Web':'web', 'Fuente':'fuente'}, inplace=True)

    
    # Creo un dataframe con la información de cines que voy a necesitar 
    df_salas_de_cine = df_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
    df_salas_de_cine.rename(
                            {'Provincia': 'provincia', 'Pantallas': 'pantallas', 'Butacas': 'butacas'},
                            inplace=True)
    
     # Agrego la columna correspondiente a la fecha de carga 
    df_salas_de_cine = df_salas_de_cine.assign(fecha_carga=hoy)

    # Lo guardo en un nuevo csv
    df_salas_de_cine.to_csv('df_cines.csv',index=False, encoding='UTF-8')

    # Cargo los datos del csv de museos
    carpeta = 'museos' + '/' + str(hoy.year) + '-' + meses[hoy.month]
    df_museos = pd.read_csv(carpeta + '/' + 'museos' + '-' + str(hoy.day) + '-' + str(hoy.month) + '-' + str(hoy.year) + '.csv', encoding='UTF-8')

    # Me quedo con las columnas de interés
    df_museos = df_museos[['cod_loc', 'idprovincia', 'iddepartamento', 'categoria', 'provincia', 'localidad',
                            'nombre', 'direccion', 'CP', 'telefono', 'mail', 'web', 'fuente']]

    # Renombro las columnas
    df_museos.rename(
                    {'cod_loc':'cod_localidad', 'idprovincia':'id_provincia', 'iddepartamento':'id_departamento', 'dirección':'domicilio',
                    'CP':'código postal','telefono':'número de teléfono'}, inplace=True)

    # Creo un dataframe con la información conjunta que acabo de procesar
    df_unido = pd.concat([df_bibliotecas, df_cines, df_museos])

    # Agrego la columna correspondiente a la fecha de carga 
    df_unido = df_unido.assign(fecha_carga=hoy)

    # Lo guardo en un nuevo csv
    df_unido.to_csv('df_conjunto.csv', index=False, encoding='UTF-8')

if __name__ == '__main__':
    procesar_datos()