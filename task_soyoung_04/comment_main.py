from crud_module import *

if __name__ == '__main__':
    # 게시글 추가
    # save_many_query = "insert into tbl_post(title) values(%s)"
    # save_many_params = (
    #     ('게시글1'),
    #     ('게시글2'),
    #     ('게시글3'),
    #     ('게시글4'),
    #     ('게시글5')
    # )
    # save_many(save_many_query, save_many_params)

    # 댓글 추가
    # find_by_id_query = "select id from tbl_post where id = %s"
    # find_by_id_params = 4,
    #
    # post = find_by_id(find_by_id_query, find_by_id_params)
    #
    # save_many_query = "insert into tbl_comment (post_id, name, email, content) values(%s, %s, %s, %s)"
    # save_many_params = (
    #     (post.get('id'), 'aaa', 'aaa@gmail.com', '1번 댓글입니다.'),
    #     (post.get('id'), 'bbb', 'bbb@gmail.com', '2번 댓글입니다.'),
    #     (post.get('id'), 'ccc', 'ccc@gmail.com', '3번 댓글입니다.'),
    # )
    # save_many(save_many_query, save_many_params)

    # 댓글 수정
    # find_by_id_query = "select * from tbl_comment where id = %s"
    # find_by_id_params = 3,
    #
    # comment = find_by_id(find_by_id_query, find_by_id_params)
    # comment['content'] = '수정된 댓글입니다.'
    # update_query = "update tbl_comment \
    #                 set name = %s, email = %s, content = %s \
    #                 where id = %s"
    # update_params = (comment.get('name'), comment.get('email'), comment.get('content'), comment.get('id'))
    # update(update_query, update_params)

    # 댓글 삭제
    delete_query = "delete from tbl_comment where id = %s"
    delete_params = 5,

    delete(delete_query,delete_params)
