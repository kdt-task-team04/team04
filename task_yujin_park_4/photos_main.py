from connection_module import *
from crud_module import *
from photos_class import *

if __name__ == '__main__':
    #사진 추가
    find_by_id_query = "select id from tbl_album where id = %s"
    find_by_id_params = 1,

    album = find_by_id(find_by_id_query, find_by_id_params)

    save_many_query = ("insert into tbl_photos (album_id, title, url, thumbnail_url) values (%s, %s, %s, %s)")
    save_many_params = ((album.get('id'), 'title1', 'http://example1-1.com', 'http://example1-2.com'),
                        (album.get('id'), 'title2', 'http://example2-1.com', 'http://example2-2.com'),
                        (album.get('id'), 'title3', 'http://example3-1.com', 'http://example3-2.com'))

    save_many(save_many_query, save_many_params)

    #사진 수정, 수정된 사진에 title뒤에 '수정됨'을 붙임
    find_by_id_query = "select id from tbl_photos where id = %s"
    find_by_id_params = 1,

    photos = find_by_id(find_by_id_query, find_by_id_params)
    
    photos['content'] = '수정됨'
    update_query = "update tbl_photos set title = %, url = %s, thumbnail_url = %s where id = %s"
    update_params = ((album.get('id'), photos.get('title'), photos.get('url'), photos.get('thumbnail_url')))
    update(update_query, update_params)


    #사진 삭제
    delete_query = "delete from tbl_photos where id =%s"
    delete_params = 1,

    delete(delete_query, delete_params)