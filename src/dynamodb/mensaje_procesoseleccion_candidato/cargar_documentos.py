def cargar_archivo_a_tabla_mensaje_procesoseleccion_candidato(mensajes, dynamodb):
    '''
    Cargar los registros de la lista en la tabla en AWS DynamoDB.
    :param mensajes:
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.Table('Mensaje_ProcesoSeleccion_Candidato')
    for mensaje in mensajes:
        id = int(mensaje['id'])
        id_mensaje = int(mensaje['id_mensaje'])
        print("Agregando mensaje:", id, id_mensaje)
        tabla.put_item(Item=mensaje)
