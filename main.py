from config import config
from databaseConnection import connection
import os
from models import Notes
import time

allNotes=[]
def add():
    '''
    This is the function which is responsible to for additon of data to the mongoDb
    :return: node
    '''
    title=input("Add an Title :")
    Body=input("Body :")
    node=Notes.Notes(title,Body)
    return node
    pass


def find():

    name=str(input("Enter The Name of the notes :"))
    if len(allNotes) == 0:
        return {
            'status':'err',
            'name':name,
            'data':[]
        }
    else:

        data=list(filter(lambda x:x.name==name,allNotes ))
        return {
            'status': 'OK',
            'name': name,
            'data':data
        }
    pass


def delete():
    if len(allNotes)==0:
        print("No Notes is available")
        return False
        pass
    i = 1
    for notes in allNotes:
        print("{}. {}".format(i, notes))
        i = i + 1
    n = str(input("Enter the Serial Number of the notes you want to delete (separated with a comma ) :")).split(",")
    n = list(map(lambda x: int(x)-1, n))
    n = list(filter( lambda x: len(allNotes)>x>=0,n))
    ids=[]
    for i in n:
        ids.append(allNotes[i]._id)
        allNotes.pop(i)
    return ids
    pass


def findAll():
    os.system("clear")
    if len(allNotes)==0:
        return False
    else:
        for note in allNotes:
            print(note)
    return True
    pass


def main():
    '''
    This is the main Function which will be responsible for running all the functions for the version 1 , console application
    :return:
    '''
    path = str(config.getConfig()['MongoDb']['URL'])
    print("Connecting to Database")
    con = connection.Mongo(path)
    n=Notes.Notes("","")
    data=con.FindAll(n.tablename)
    if data:
        for i in data:
            allNotes.append(Notes.Notes(i['name'], i['data'], i['_id'], i['created_at']))
            print(allNotes[-1])
    while True:
        os.system("clear")
        try:

            print("Welcome To Notes Application , version 1.0.0")
            print("1.Add a Note\n2.Find a note\n3.Delete a Note\n4.See all Notes\n5.exit")
            try:
                n=int(input("Enter Your Choice >>"))
            except ValueError:
                continue
            if n==5:
                raise KeyboardInterrupt
            elif n==1:
                node=add()
                id=con.Insert(node.tablename,node.retData())
                node.setId(id)
                allNotes.append(node)
                print("Added")
                time.sleep(2)
            elif n==2:
                result=find()
                if result['status'] == 'OK':
                    for i in result['data']:
                        print(i)
                else:
                    name=result['name']
                    node=Notes.Notes(name,"")
                    data=con.Find(node.tablename,node.name)
                    if data:
                        for i in data:
                            allNotes.append(Notes.Notes(i['name'],i['data'],i['_id'],i['created_at']))
                            print(allNotes[-1])
                input()
            elif n==3:
                arr=delete()
                if not arr:
                    continue
                if len(arr)<=0:
                    print("Enter The Correct Indexes again please !!")
                    time.sleep(1.2)
                    continue
                n=Notes.Notes("","")
                count=con.Delete(n.tablename,arr)
                print("Delete Count: {}".format(count))
                input()
            elif n==4:
                if not findAll():
                    n=Notes.Notes("","")
                    data=con.FindAll(n.tablename)
                    if data:
                        for i in data:
                            allNotes.append(Notes.Notes(i['name'],i['data'],i['_id'],i['created_at']))
                            print(allNotes[-1])

                    pass
                input()
            else:
                continue
        except Exception as E:
            print("Exception has occured {} \n".format(E))
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            print("quitting...")
            exit(1)

if __name__ == '__main__':
    main()