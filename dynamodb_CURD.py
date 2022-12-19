from flask import Flask, render_template, request , flash , redirect
import boto3 
# from werkzeug.utils import secure_filename
from configparser import ConfigParser
from SubcriptionToSNS import Subscribe  ,PublishMsgToTopic , UnSubscribe
from model import Items ,DynamoDb , Account  #thu vien tu tao

#Read config.ini file
file = 'config.ini'
config = ConfigParser()
config.read(file)
config = config['default']

# Create a resource 
dynamodb = boto3.resource('dynamodb',
                    region_name='us-east-1',
                    aws_access_key_id= config['aws_access_key_id'],
                    aws_secret_access_key= config['aws_secret_access_key'],
                    aws_session_token=config['aws_session_token']
                    )
#print(list(dynamodb.tables.all()))

#FLask app begin

NAMETABLE = 'TaiKhoan'

app = Flask(__name__)


@app.route('/')  
@app.route('/home')  
def home():
    table = DynamoDb(dynamodb,NAMETABLE)
    LISTACCOUNT = table.loadDATA()
    return render_template("crudtable.html",LISTACCOUNT = LISTACCOUNT)

@app.route('/loginform')  
def loginform():
    return render_template("loginform.html")

@app.route('/upload',methods=['post','get'])
def upload():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')

        table = DynamoDb(
            dynamodb=dynamodb,
            nametable=NAMETABLE,
            name = username,
            email= email)
        check = table.addAccount()

        if check :
            return redirect('/home')
        else:
            msg ="Đăng ký không thành công !"
            return render_template("loginform.html", msg = msg)

@app.route('/delete/<email>&<name>',methods=['post','get'])
def delete(email,name):
    table = DynamoDb(
            dynamodb=dynamodb,
            nametable=NAMETABLE,
            name = name,
            email= email)
    check = table.deleteAccount()
    UnSubscribe(email)
    if check :
        return redirect('/home')
    else:
        msg ="Xóa không thành công !"
        return render_template("loginform.html", msg = msg)

@app.route('/send/<email>&<name>',methods=['post','get'])
def send(email,name):
    Subscribe(email)
    return redirect('/home')

@app.route('/publish', methods=['GET', 'POST'])
def publish():
    textarea = request.form.get('textarea')
    print(textarea)
    PublishMsgToTopic(textarea)
    return redirect('/home')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
