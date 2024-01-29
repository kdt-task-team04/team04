class Photo:
    def __init__(self, id: int, album_id: int, title: str, url: str, thumbnail_url: str):
        self.id = id
        self.album_id = album_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

