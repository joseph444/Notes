import time
class Notes:
    tablename="Notes"
    def __init__(self,name,data):
        self.name=name
        self.data=data
        self.created_at=time.ctime()

    @property
    def Tablename(self):
        return self.tablename
    def retData(self):
        data=dict()
        data['name']=self.name
        data['data']=self.data
        data['created_at']=self.created_at
        return data
    def setId(self,id):
        self._id=id

    @property
    def FullData(self):
        data=dict()
        data['_id']=self._id
        data['name']=self.name
        data['data']=self.data
        data['created_at']=self.created_at
        return data