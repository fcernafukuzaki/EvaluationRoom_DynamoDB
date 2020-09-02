def eliminar_tabla_mensaje_procesoseleccion_candidato(dynamodb):
    '''
    Eliminar tabla de DynamoDB.
    :param dynamodb:
    :return:
    '''
    table = dynamodb.Table('Mensaje_ProcesoSeleccion_Candidato')
    table.delete()
