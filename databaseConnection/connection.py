import pymongo
from bson.objectid import ObjectId

class Mongo:
    def __init__(self,URL:str):
        self.client = pymongo.MongoClient(URL)
        self.db=self.client['notes']
        print(self.db)
        pass
    def Insert(self,tablename,Data):
        try:
            col = self.db[tablename]
            x = col.insert(Data)
            print(x)
            return x
            pass
        except Exception as e:
            print(e)
            pass
        return False
    def Find(self,tablename,Name):
        try:
            col=self.db[tablename]
            results=col.find({'name':Name})
            data=[]
            for result in results:
                data.append(result)
            return data
            pass
        except Exception as e:
            print(e)
            pass
        return False
    def Delete(self,tablename,Ids):
       try:
           col=self.db[tablename]
           S=0
           for id in Ids:
               x=col.delete_one({'_id':ObjectId(id)})
               S=S+int(x.deleted_count)
           return S
           pass
       except Exception as e:
           print(e)
       return False