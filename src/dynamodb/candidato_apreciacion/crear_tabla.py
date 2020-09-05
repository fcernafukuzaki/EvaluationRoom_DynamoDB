def crear_tabla_candidato_apreciacion(dynamodb):
    '''
    Crear una tabla en AWS DynamoDB a partir de un archivo JSON.
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.create_table(
        TableName='Candidato_Apreciacion',
        KeySchema=[
            {
                'AttributeName': 'idcandidato',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'idtestpsicologico_idparte_idpregunta',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'idcandidato',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'idtestpsicologico_idparte_idpregunta',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return tabla