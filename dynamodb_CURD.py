from flask import Flask, render_template, request , flash , redirect
import boto3 
# from werkzeug.utils import secure_filename
from configparser import ConfigParser

from model import Items ,DynamoDb , Account  #thu vien tu tao

#Read config.ini file
file = 'config.ini'
config = ConfigParser()
config.read(file)
config = config['default']

# Create a resource 
dynamodb = boto3.resource('dynamodb',aws_access_key_id= config['aws_access_key_id'],
                    aws_secret_access_key= config['aws_secret_access_key'],
                    aws_session_token=config['aws_session_token']
                    )
print(list(dynamodb.tables.all()))

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
    if check :
        return redirect('/home')
    else:
        msg ="Xóa không thành công !"
        return render_template("loginform.html", msg = msg)


if __name__ == "__main__":
    
    app.run(debug=True)


