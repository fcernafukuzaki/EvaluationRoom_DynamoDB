import boto3
from dynamodb.testpsicologico_pregunta.eliminar_tabla import eliminar_tabla_testpsicologico_pregunta
from dynamodb.candidato_respuesta.eliminar_tabla import eliminar_tabla_candidato_respuesta
from dynamodb.testpsicologico_instrucciones.eliminar_tabla import eliminar_tabla_testpsicologico_instrucciones
from dynamodb.mensaje_procesoseleccion_candidato.eliminar_tabla import eliminar_tabla_mensaje_procesoseleccion_candidato
from dynamodb.candidato_resultado.eliminar_tabla import eliminar_tabla_candidato_resultado

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')

    eliminar_tabla_mensaje_procesoseleccion_candidato(dynamodb)
    print("Tabla eliminada.")

    eliminar_tabla_testpsicologico_instrucciones(dynamodb)
    print("Tabla eliminada.")

    eliminar_tabla_testpsicologico_pregunta(dynamodb)
    print("Tabla eliminada.")

    eliminar_tabla_candidato_respuesta(dynamodb)
    print("Tabla eliminada.")

    eliminar_tabla_candidato_resultado(dynamodb)
    print("Tabla eliminada.")