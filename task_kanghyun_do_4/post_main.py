from crud_module import *

if __name__ == '__main__':
     # 게시글 추가
    find_by_id_query = "select id from tbl_user where id = %s"
    find_by_id_params = 1,

    user = find_by_id(find_by_id_query, find_by_id_params)

    save_many_query = "insert into tbl_post(user_id, title, body) values(%s, %s, %s)"
    save_many_params = (
        (user.get('id'), '테스트 제목1','테스트 내용1'),
        (user.get('id'), '테스트 제목2','테스트 내용2'),
        (user.get('id'), '테스트 제목3','테스트 내용3'),
        (user.get('id'), '테스트 제목4','테스트 내용4'),
    )
     save_many(save_many_query, save_many_params)

     # 게시글 수정
    find_by_id_query = "select * from tbl_post where id = %s"
    find_by_id_params = 2,

    post = find_by_id(find_by_id_query, find_by_id_params)
    post['body'] = '수정된 테스트내용'
    update_query = "update tbl_post \
                    set body = %s \
                    where id = %s"
    update_params = (post.get('body'), post.get('id'))
    update(update_query, update_params)

    #댓글 삭제
    delete_query = "delete from tbl_post where id = %s"
    delete_params = 3,

    delete(delete_query, delete_params)