import json
import boto3

print('Loading function')


def publish_msg(message):
	sqs = boto3.client('sqs')
	response  = sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/407415326349/mySQStoSNS' ,
            MessageBody= message
        )
	return response


def lambda_handler(event, context):
	print('------------------------')
	print(event)
	#1. Iterate over each record
	try:
		for record in event['Records']:
			#2. Handle event by type
			if record['eventName'] == 'INSERT':
				handle_insert(record)
			elif record['eventName'] == 'MODIFY':
				handle_modify(record)
			elif record['eventName'] == 'REMOVE':
				handle_remove(record)
		print('------------------------')
		return "Success!"
	except Exception as e: 
		print(e)
		print('------------------------')
		return "Error"


def handle_insert(record):
	print("Handling INSERT Event")
	
	#3a. Get newImage content
	newImage = record['dynamodb']['NewImage']
	
	#3b. Parse values
	email = newImage['Email']['S']

	#3c. Print it
	message = 'Da them 1 email moi = ' + email
	publish_msg(message)
	print(message)

	print("Done handling INSERT Event")



def handle_remove(record):
	print("Handling REMOVE Event")

	#3a. Parse oldImage
	oldImage = record['dynamodb']['OldImage']
	
	#3b. Parse values
	oldemail = oldImage['Email']['S']

	#3c. Print it
	message = 'Da xoa di email = ' + oldemail
	publish_msg(message)
	print(message)
	print("Done handling REMOVE Event")
	
def handle_modify(record):
	print("Handling MODIFY Event")

	#3a. Parse oldImage and score
	oldImage = record['dynamodb']['OldImage']
	oldemail = oldImage['Email']['S']
	
	#3b. Parse oldImage and score
	newImage = record['dynamodb']['NewImage']
	newemail = newImage['Email']['S']

	#3c. Check for change
	if oldemail != newemail:
		message = 'Da thay doi email tu email =  '+ oldemail +' thanh email = ' + newemail
		publish_msg(message)
		print(message)

	print("Done handling MODIFY Event")