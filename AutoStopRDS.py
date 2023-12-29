import boto3
import json
instances_rds = ['']

def lambda_handler(event, context):
    rds = boto3.client('rds')
    for instance_rds in instances_rds:
        rds.stop_db_instance(DBInstanceIdentifier = instance_rds)

    return {
        'statusCode': 200,
        'body': json.dumps('stops rds')
    }