from crud_module_albums import *

if __name__ == '__main__':
    # 앨범 정보 추가
    save_many_query = ("insert into tbl_albums (user_id, title)"
                       " values (%s , %s)")
    save_many_params = (
        (1, 'album1'),
        (2, 'album2'),
        (3, 'album3')
    )
    save_many(save_many_query, save_many_params)

    # user_id로 회원 1명 조회하기
    # 조회 후 title 수정하기
    find_by_id_query = "select * from tbl_albums where user_id = %s"
    find_by_id_params = 3,
    albums = find_by_id(find_by_id_query, find_by_id_params)
    # print(albums)

    update_query = "update tbl_albums " \
                   "set title = %s " \
                   "where user_id = %s "
    update_params = (albums.get('title'), albums.get('user_id'))
    # update(update_query, update_params)

    # user_id로 회원 1명 삭제하기
    delete_query = "delete from tbl_albums where user_id %s"
    delete_params = (albums.get('user_id_3'))
    # delete(delete_query, delete_params)

