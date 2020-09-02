def cargar_archivo_a_tabla_testpsicologico_instrucciones(testpsicologicos, dynamodb):
    '''
    Cargar los registros de la lista en la tabla en AWS DynamoDB.
    :param testpsicologicos:
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.Table('TestPsicologico_Instrucciones')
    for testpsicologico in testpsicologicos:
        idtestpsicologico = int(testpsicologico['id_testpsicologico'])
        idparte_idpregunta = testpsicologico['id_testpsicologico_idparte']
        print("Agregando test psicológico:", idtestpsicologico, idparte_idpregunta)
        tabla.put_item(Item=testpsicologico)
