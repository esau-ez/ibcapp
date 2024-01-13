import mysql.connector
import os
import yaml
import sys
from pathlib import Path
global config
directorio_base = Path(__file__).resolve().parent
ruta_del_archivo_yaml = f'{directorio_base}\settings.yaml'
# Cargar el contenido del archivo YAML
with open(ruta_del_archivo_yaml, 'r') as archivo_yaml:
    datos = yaml.safe_load(archivo_yaml)

# Modificar o agregar datos
yaml_user = datos['databaseUser']
yaml_password = datos['databasePassword']
yaml_host = datos['host']
config = {
    'host': f'{str(yaml_host)}',
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
