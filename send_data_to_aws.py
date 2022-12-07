from flask import Flask, render_template, request , flash
import boto3 , os
from werkzeug.utils import secure_filename
from configparser import ConfigParser

#Read config.ini file
file = 'config.ini'
config = ConfigParser()
config.read(file)
config = config['default']

# Create a client
s3 = boto3.client('s3',aws_access_key_id= config['aws_access_key_id'],
                    aws_secret_access_key= config['aws_secret_access_key'],
                    aws_session_token=config['aws_session_token']
                    )
# Name bucket want to connect
BUCKET_NAME='s3-to-email'  

# Check if connect or not 
response = s3.list_buckets()     
for bucket in response['Buckets']:
    if bucket['Name'] == BUCKET_NAME:
        print("Found successfully !")
        print('Bucket had found is : '+ bucket['Name'])
print(os.path.join( "UploadtoS3", "file.txt"))

# app flask begin
app = Flask(__name__)

def SendToS3(bucketname,filename, key):
    try:
        s3.upload_file(
                        Bucket = bucketname,
                        Filename=filename,
                        Key = key
                        )
        return True                        
    except :                    
        return False

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename) # str html.png
                img.save(os.path.join('UploadtoS3',filename)) # save at UploadtoS3 folder
                path = os.path.join('UploadtoS3',filename)
                check =  SendToS3(BUCKET_NAME,path,filename)

                if check :
                    msg = "Upload Done ! "
                else :
                    msg = "Sorry Upload to S3 is not success"
        else :
            flash('No file path')

    return render_template("file_upload_to_s3.html",msg =msg)

if __name__ == "__main__":
    
    app.run(debug=True)


