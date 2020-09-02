import boto3
from dynamodb.testpsicologico_pregunta.crear_tabla import crear_tabla_testpsicologico_pregunta
from dynamodb.candidato_respuesta.crear_tabla import crear_tabla_candidato_respuesta
from dynamodb.testpsicologico_instrucciones.crear_tabla import crear_tabla_testpsicologico_instrucciones
from dynamodb.mensaje_procesoseleccion_candidato.crear_tabla import crear_tabla_mensaje_procesoseleccion_candidato
from dynamodb.candidato_resultado.crear_tabla import crear_tabla_candidato_resultado

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')

    tabla_mensaje_procesoseleccion_candidato = crear_tabla_mensaje_procesoseleccion_candidato(dynamodb)
    print("Estatus de la tabla:", tabla_mensaje_procesoseleccion_candidato.table_status)

    tabla_testpsicologico_instrucciones = crear_tabla_testpsicologico_instrucciones(dynamodb)
    print("Estatus de la tabla:", tabla_testpsicologico_instrucciones.table_status)

    tabla_testpsicologico_pregunta = crear_tabla_testpsicologico_pregunta(dynamodb)
    print("Estatus de la tabla:", tabla_testpsicologico_pregunta.table_status)

    tabla_candidato_respuesta = crear_tabla_candidato_respuesta(dynamodb)
    print("Estatus de la tabla:", tabla_candidato_respuesta.table_status)

    tabla_candidato_resultado = crear_tabla_candidato_resultado(dynamodb)
    print("Estatus de la tabla:", tabla_candidato_resultado.table_status)
