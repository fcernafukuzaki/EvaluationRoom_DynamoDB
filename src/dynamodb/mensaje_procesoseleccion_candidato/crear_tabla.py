def crear_tabla_mensaje_procesoseleccion_candidato(dynamodb):
    '''
    Crear una tabla en AWS DynamoDB a partir de un archivo JSON.
    :param dynamodb:
    :return:
    '''
    tabla = dynamodb.create_table(
        TableName='Mensaje_ProcesoSeleccion_Candidato',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'id_mensaje',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'id_mensaje',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return tabla