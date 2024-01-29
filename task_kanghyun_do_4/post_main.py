from crud_module import *
from user import User
# import os
# print(os.getcwd())
if __name__ == '__main__':
     # 게시글 추가
    find_by_id_query = "select id from tbl_users where id = %s"
    find_by_id_params = 1,

    user = find_by_id(find_by_id_query, find_by_id_params)

    save_many_query = "insert into tbl_post(user_id, title, body) values(%s, %s, %s)"
    save_many_params = (
        (user.get('id'), 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit','quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
        (user.get('id'), 'qui est esse','est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'),
        (user.get('id'), 'ea molestias quasi exercitationem repellat qui ipsa sit aut','et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'),
        (user.get('id'), 'eum et est occaecati','ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit')
    )
    save_many(save_many_query, save_many_params)

    #  # 게시글 수정
    # find_by_id_query = "select * from tbl_post where id = %s"
    # find_by_id_params = 2,
    #
    # post = find_by_id(find_by_id_query, find_by_id_params)
    # post['body'] = '수정된 테스트내용'
    # update_query = "update tbl_post \
    #                 set body = %s \
    #                 where id = %s"
    # update_params = (post.get('body'), post.get('id'))
    # update(update_query, update_params)
    #
    # #게시글 삭제
    # delete_query = "delete from tbl_post where id = %s"
    # delete_params = 4,
    #
    # delete(delete_query, delete_params)