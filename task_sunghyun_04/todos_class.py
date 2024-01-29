class User :
    def __init__(self,id:int,name:str,username:str,email:str,phone:int,website:str) :
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

class Todo:
    def __init__(self, user_id:int, id:int, title:str, completed:bool):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.completed = completed


