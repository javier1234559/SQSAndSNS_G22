from flask import Flask, render_template, request , flash
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)


s3 = boto3.client('s3',
                    aws_access_key_id="ASIAV5W6YQ2GUAQCQVR3",
                    aws_secret_access_key= "YrVrhkhHCmbC2rv7L3YysHGp/rgc455AriKosv9z",
                    aws_session_token="FwoGZXIvYXdzENz//////////wEaDMHBr6v51A0VfnjkXyLPAd2eiUjwZHc5iG1fiOYQoDX6mn0WCjNO4Bmm+fifFi3D2Gj7RmCBiouFvus7zSl6FApIO/0NzuI7GQzNfpNOiutiZeGNosfY6Q5HP7ZgqHisa1T5SH9rpfbSG80bh/YWTRCt5VPbiMteCQdJszmnV0+2cyJTqCozPSPoy5eGZUHcVlz+SjnDT3yql2gP5YHscALwp4xkhSgV5IvsPzt1Y/GOn2KDe2rIUfyL/j8f9UCqNqlDQxZ+BANG+j9Sq6NGrc3oXJT8SOBNtVyT8ghAtCiWg/2bBjItpkJXjkR2kvIplayIBYli/2sHMrdr7Rt5rCU0RewRauQyfS4GgeMi8PHUUYj2"
                     )

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])
    print(bucket)

BUCKET_NAME='pre1-my-bucket'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")


@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "
        else :
             flash('No file path')

    return render_template("file_upload_to_s3.html",msg =msg)




if __name__ == "__main__":
    
    app.run(debug=True)


