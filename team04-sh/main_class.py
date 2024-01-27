class User :
    def __init__(self,id,name,username,email,phone,website) :
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

class Todo:
    def __init__(self, user_id, id, title, completed):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.completed = completed


