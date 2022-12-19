import json
import boto3
import os
 
def send_request(body):
    # Create an SNS client
    sns = boto3.client('sns')
    response = sns.publish(
        TargetArn='arn:aws:sns:us-east-1:407415326349:Bao-Cao-Cloud',    
        Message=body,    
    )
    print('(Debug)Gui thanh cong tn : ' + body)
    
def lambda_handler(event, context):
    #batch_processes=[]
    for record in event['Records']:
        print (record)
        send_request(record["body"])
    
 
