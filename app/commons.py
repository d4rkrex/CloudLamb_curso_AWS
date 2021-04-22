import boto3, base64, json, requests
from boto3.session import Session
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

Dynamo_TableName = 'Cloudlamb-API'


def get_dynamo(_id):
    client = boto3.resource('dynamodb', region_name='us-east-1')
    table = client.Table(Dynamo_TableName)
    try:
        response = table.get_item(
            Key={
                'ID': _id
            }
        )
        return response['Item']['scan_id']
    except:
        return False


def put_dynamo(_id, nombre):
    response: {}
    try:
        data = {'ID': str(_id), 'Nombre': nombre}
        db = boto3.resource('dynamodb', region_name='us-east-1')
        table = db.Table(Dynamo_TableName)
        table.put_item(
            Item=data
            )
        response['codigo'] = "200"
        response['msg'] = "Registro exitoso"
        return response
    except:
        response['codigo'] = "401"
        response['msg'] = "Error guardando en base de datos"
        return False


def delete_dynamo(_id, nombre):
    response: {}
    data = {'ID': _id, 'Nombre': nombre}
    try:
        db = boto3.resource('dynamodb', region_name='us-east-1')
        table = db.Table(Dynamo_TableName)
        table.delete_item(
            Item=data
            )
        response['codigo'] = "200"
        response['msg'] = "Registro borrado con exito"
        return True
    except:
        return False



