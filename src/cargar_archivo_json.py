from decimal import Decimal
import json
import boto3
from dynamodb.testpsicologico_pregunta.cargar_documentos import cargar_archivo_a_tabla_testpsicologico_pregunta
from dynamodb.testpsicologico_instrucciones.cargar_documentos import cargar_archivo_a_tabla_testpsicologico_instrucciones
from dynamodb.mensaje_procesoseleccion_candidato.cargar_documentos import cargar_archivo_a_tabla_mensaje_procesoseleccion_candidato

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')

    with open("dynamodb/mensaje_procesoseleccion_candidato/mensaje-procesoseleccion-candidato.json", encoding='utf-8') as json_file:
        mensajes = json.load(json_file, parse_float=Decimal)
    cargar_archivo_a_tabla_mensaje_procesoseleccion_candidato(mensajes, dynamodb)

    with open("dynamodb/testpsicologico_instrucciones/testpsicologico-instrucciones.json", encoding='utf-8') as json_file:
        testpsicologicos_instrucciones = json.load(json_file, parse_float=Decimal)
    cargar_archivo_a_tabla_testpsicologico_instrucciones(testpsicologicos_instrucciones, dynamodb)

    with open("dynamodb/testpsicologico_pregunta/testpsicologico-pregunta.json", encoding='utf-8') as json_file:
        testpsicologicos = json.load(json_file, parse_float=Decimal)
    cargar_archivo_a_tabla_testpsicologico_pregunta(testpsicologicos, dynamodb)