import mysql.connector
import os
import yaml
import sys
path = os.getcwd()
global config

ruta_del_archivo_yaml = f'{path}\config\settings.yaml'
print(ruta_del_archivo_yaml)
# Cargar el contenido del archivo YAML
with open(ruta_del_archivo_yaml, 'r') as archivo_yaml:
    datos = yaml.safe_load(archivo_yaml)

# Modificar o agregar datos
yaml_user = datos['databaseUser']
yaml_password = datos['databasePassword']
config = {
    'host': 'localhost',
    'user': f'{str(yaml_user)}',
    'password': f'{str(yaml_password)}',
    'database': 'ibcapp',
}
def consulta(query):
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultado
def add(query):
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return resultado
