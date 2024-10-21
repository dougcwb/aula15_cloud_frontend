import json
import random
import boto3
from time import gmtime, strftime

# Criar o objeto DynamoDB usando o SDK boto3
dynamodb = boto3.resource('dynamodb')
# Selecionar a tabela que criamos
table = dynamodb.Table('SorteiosJornada')

# Função Lambda que realiza o sorteio e persiste os dados
def lambda_handler(event, context):
    nome_sorteio = event['nomeSorteio']
    num_min = int(event['numMin'])
    num_max = int(event['numMax'])
    numero_sorteado = random.randint(num_min, num_max)
    
    # Salvar os dados no DynamoDB
    response = table.put_item(
        Item={
            'ID': strftime("%Y%m%d%H%M%S", gmtime()),  # Gerar um ID único baseado no horário
            'NomeSorteio': nome_sorteio,
            'NumeroMin': num_min,
            'NumeroMax': num_max,
            'NumeroSorteado': numero_sorteado,
            'DataSorteio': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())  # Data e hora do sorteio
        }
    )
    
    # Retornar o resultado do sorteio
    return {
        'statusCode': 200,
        'body': json.dumps({
            'nomeSorteio': nome_sorteio,
            'numeroSorteado': numero_sorteado
        })
    }