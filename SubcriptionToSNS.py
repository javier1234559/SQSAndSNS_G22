from flask import Flask
import boto3 
# from werkzeug.utils import secure_filename
from configparser import ConfigParser


#Read config.ini file
file = 'config.ini'
config = ConfigParser()
config.read(file)
config = config['default']

# Create a client 
sns = boto3.client('sns',
                    region_name='us-east-1',
                    aws_access_key_id= config['aws_access_key_id'],
                    aws_secret_access_key= config['aws_secret_access_key'],
                    aws_session_token=config['aws_session_token']
                    )

TOPPIC_NAME= 'demoSQStoSNS'
TOPIC_ARN='arn:aws:sns:us-east-1:407415326349:demoSQStoSNS'

def checkConfirm(email):
    subscriptions = sns.list_subscriptions_by_topic(TopicArn=TOPIC_ARN)
    for sub in subscriptions['Subscriptions']:
        if email in sub['Endpoint'] and 'arn:aws' in sub['SubscriptionArn']:
            return True 
    return False  

def Subscribe(email):
    response = sns.subscribe(TopicArn=TOPIC_ARN, Protocol="email", Endpoint=email)
    subscription_arn = response["SubscriptionArn"]
    if subscription_arn :
        print("Subscribe successfully !")

def PublishMsgToTopic(message):
    if message : 
        response = sns.publish(
                        TopicArn=TOPIC_ARN,
                        Message=message,
                        Subject="Tin nhan tu chu de "+TOPPIC_NAME
                    )
        print("Publish message to topic successfully !")
        return True
    print("Publish message to topic failed ")
    return False

def UnSubscribe(email):
    subscriptions = sns.list_subscriptions_by_topic(TopicArn=TOPIC_ARN)
    for sub in subscriptions['Subscriptions']:
        if email in sub['Endpoint'] and 'arn:aws' in sub['SubscriptionArn']:
            reponse = sns.unsubscribe(SubscriptionArn= sub['SubscriptionArn'])
            print("UnSubscribe successfully !")

#ENDPOINT = 'nguyenhue1234559@gmail.com'
#LIST_SUBSCRIBER = []
