from crud_module import *
from user import User
from post import Post
# import os
# print(os.getcwd())
if __name__ == '__main__':
     # 게시글 추가

     # find_by_id_query = "select id from tbl_users where id = %s"
     # find_by_id_params = 4,
     #
     # user = find_by_id(find_by_id_query, find_by_id_params)
     #
     # save_many_query = "insert into tbl_post(user_id, title, body) values(%s, %s, %s)"
     # save_many_params = (
     #     (user.get('id'), 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit','quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
     #     (user.get('id'), 'qui est esse','est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'),
     #     (user.get('id'), 'ea molestias quasi exercitationem repellat qui ipsa sit aut','et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'),
     #     (user.get('id'), 'eum et est occaecati','ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit')
     # )
     # save_many(save_many_query, save_many_params)

     #  # 게시글 수정
     # find_by_id_query = "select * from tbl_post where id = %s"
     #  find_by_id_params = 2,
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


     # 게시글 목록 보기
     # find_all_query = "select u.username, p.title from tbl_users u join tbl_post p\
     #                    on u.id= p.user_id"
     # posts = find_all(find_all_query)
     # for post in posts:
     #     print(post)

     # 게시글 상세 보기
     find_by_id_query = "select id, title, body, user_id from tbl_post where id = %s"
     find_by_id_params = 5,
     post = find_by_id(find_by_id_query, find_by_id_params)

     find_all_by_query = "select p.id, p.title, p.body, p.user_id, u.username, u.email \
      from tbl_users u join tbl_post p \
      on p.user_id = u.id"

     # print(post)
     posts = find_all_by(find_all_by_query, find_by_id_params)
     post_find = Post(post.get("id"), post.get("title"), post.get("body"), posts)
     print(post_find.__dict__)


