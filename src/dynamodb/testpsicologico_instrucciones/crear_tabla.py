def crear_tabla_testpsicologico_instrucciones(dynamodb):
    '''
    Crear una tabla en AWS DynamoDB a partir de un archivo JSON.
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.create_table(
        TableName='TestPsicologico_Instrucciones',
        KeySchema=[
            {
                'AttributeName': 'id_testpsicologico',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'id_testpsicologico_idparte',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id_testpsicologico',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'id_testpsicologico_idparte',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return tabla