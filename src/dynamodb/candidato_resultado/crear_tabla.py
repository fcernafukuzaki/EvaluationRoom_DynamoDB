def crear_tabla_candidato_resultado(dynamodb):
    '''
    Crear una tabla en AWS DynamoDB a partir de un archivo JSON.
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.create_table(
        TableName='Candidato_Resultado',
        KeySchema=[
            {
                'AttributeName': 'idcandidato',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'fecha',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'idcandidato',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'fecha',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return tabla