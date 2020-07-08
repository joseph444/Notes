import time

class Notes:
    tablename="Notes"
    def __init__(self,name,data,_id=None,created_at=None):
        self.name=name
        self.data=data
        self.created_at=time.ctime()
        if _id:
            self._id=_id
        if created_at:
            self.created_at=created_at

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
    @property
    def Id(self):
        return self._id
    def __str__(self):
        return "name : {}\nBody:{}\nCreated at:{}\n\n".format(self.name,self.data,self.created_at)