def eliminar_tabla_candidato_respuesta(dynamodb):
    '''
    Eliminar tabla de DynamoDB.
    :param dynamodb:
    :return:
    '''
    table = dynamodb.Table('Candidato_Respuesta')
    table.delete()
