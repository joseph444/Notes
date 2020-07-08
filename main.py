from config import config
from databaseConnection import connection
from models import Notes
path=str(config.getConfig()['MongoDb']['URL'])
con = connection.Mongo(path)
newNote=Notes.Notes("Hello","Data")
val=con.Find(newNote.tablename,newNote.name)
ids=list(map(lambda x:x['_id'],val))
#print(ids)
#print(con.Delete(newNote.Tablename,ids))
id=con.Insert(newNote.tablename,newNote.retData())
newNote.setId(id)
#print(newNote.FullData)