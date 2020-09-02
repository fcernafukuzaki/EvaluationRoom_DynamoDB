def cargar_archivo_a_tabla_candidato_respuesta(respuestas, dynamodb):
    '''
    Cargar los registros de la lista en la tabla en AWS DynamoDB.
    :param respuestas:
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.Table('Candidato_Respuesta')
    for respuesta in respuestas:
        idcandidato = int(respuesta['idcandidato'])
        idtestpsicologico_idparte_idpregunta = respuesta['idtestpsicologico_idparte_idpregunta']
        print("Agregando respuesta de candidato:", idcandidato, idtestpsicologico_idparte_idpregunta)
        tabla.put_item(Item=respuesta)
