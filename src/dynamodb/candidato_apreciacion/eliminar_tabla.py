def eliminar_tabla_candidato_apreciacion(dynamodb):
    '''
    Eliminar tabla de DynamoDB.
    :param dynamodb:
    :return:
    '''
    table = dynamodb.Table('Candidato_Apreciacion')
    table.delete()
