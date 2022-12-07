import json

class Items :
    def __init__(self, dynamodb ,NAMETABLE):
        table = dynamodb.Table(NAMETABLE)
        response = table.scan()

        self.tablename = NAMETABLE
        self.listItems = response
        self.names = response['Items']
        self.count = response['Count']

    def listItem (self):
        print(json.dumps(self.listItems, indent=4) )
    def getcountItem (self):
        print('Number of items in table : '+ self.count)
        return self.count
    def getlistItemNames (self):
        return self.names

class DynamoDb :
    def __init__(self ,dynamodb ,nametable , name=None,email=None):
        self.dynamodb = dynamodb
        self.nametable = nametable
        self.name = name
        self.email = email

    def loadDATA (self):
        LISTACCOUNT = []
        list = Items(self.dynamodb,self.nametable)
        for obj in list.getlistItemNames() :
            acc = Account( obj['Name'],obj['Email'])
            LISTACCOUNT.append(acc)
        return LISTACCOUNT

    def addAccount (self):
        try :
            table = self.dynamodb.Table(self.nametable)
            response = table.put_item(
                Item = { 
                    'Name': self.name,
                    'Email': self.email
                }
            )
            return True
        except:
            print("Tao tai khoan khong thanh cong !")
            return False

    def deleteAccount (self):
        try :
            table = self.dynamodb.Table(self.nametable)
            response = table.delete_item(
                Key = {
                    'Name': self.name,
                     'Email': self.email
                     })
            print(response)
            return True
        except:
            print("Tai khoan khong ton tai !")
            return False

    def readAccount (self):
        try :
            table = self.dynamodb.Table(self.nametable)
            response = table.get_item(
                Key={
                    'Name': self.name,
                    'Email': self.email
                }
            )
            resp = response['Item']
            print(resp)
            return resp
        except:
            print("Tai khoan khong ton tai !")
            return None

class Account :
    def __init__(self, name, email):
        self.name = name
        self.email = email
