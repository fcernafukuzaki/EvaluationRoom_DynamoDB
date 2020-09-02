def eliminar_tabla_testpsicologico_pregunta(dynamodb):
    '''
    Eliminar tabla de DynamoDB.
    :param dynamodb:
    :return:
    '''
    table = dynamodb.Table('TestPsicologico_Pregunta')
    table.delete()
