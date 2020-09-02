def eliminar_tabla_testpsicologico_instrucciones(dynamodb):
    '''
    Eliminar tabla de DynamoDB.
    :param dynamodb:
    :return:
    '''
    table = dynamodb.Table('TestPsicologico_Instrucciones')
    table.delete()
