class Comment:
    def __init__(self, id: int, post_id: int, name: str, email: str, content: str):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.content = content
