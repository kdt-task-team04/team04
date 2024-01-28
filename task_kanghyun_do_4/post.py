class Post:
    def __init__(self, id: int, user_id: int, title: str, body: str):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body