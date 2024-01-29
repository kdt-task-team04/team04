from crud_module import *

if __name__ == '__main__':
    # 회원 추가
    save_many_query = "insert into tbl_users(name, username, email, phone, website) values(%s, %s, %s, %s, %s)"
    save_many_params = (
        ('홍길동', 'hgd', 'hgd1234@gmail.com', '01012341234', 'www.gmail.com'),
        ('이순신', 'lss', 'lss1234@gmail.com', '01012341111', 'www.gmail.com')
    )

    save_many(save_many_query, save_many_params)

    # 게시글 추가
    save_many_query = "insert into tbl_post(title, body, user_id) values(%s, %s, %s)"
    save_many_params = (
        ('게시글 제목1', '게시글 내용1', '1'),
        ('게시글 제목2', '게시글 내용2', '2'),
        ('게시글 제목3', '게시글 내용3', '1'),
        ('게시글 제목4', '게시글 내용4', '2'),
        ('게시글 제목5', '게시글 내용5', '1'),
    )
    save_many(save_many_query, save_many_params)

    # 댓글 추가
    find_by_id_query = "select id from tbl_post where id = %s"
    find_by_id_params = 2,

    post = find_by_id(find_by_id_query, find_by_id_params)

    save_many_query = "insert into tbl_comment (post_id, name, email, content) values(%s, %s, %s, %s)"
    save_many_params = (
        (post.get('id'), 'aaa', 'aaa@gmail.com', '1번 댓글입니다.'),
        (post.get('id'), 'bbb', 'bbb@gmail.com', '2번 댓글입니다.'),
        (post.get('id'), 'ccc', 'ccc@gmail.com', '3번 댓글입니다.'),
    )
    save_many(save_many_query, save_many_params)

    # 해당 post의 전체 댓글 조회
    find_all_by_query = "select c.* from tbl_post p \
                         join tbl_comment c on p.id = %s "
    find_all_by_params = 1,
    # comments에는 1번 게시글의 전체 댓글이 담겨있다.
    comments = find_all_by(find_all_by_query, find_all_by_params)
    # print(comments)

    # 댓글 수정
    # 수정하고 싶은 댓글 하나 조회하기 + 해당 댓글이 달려있는 게시글도 함께 조회
    find_by_id_query = "select c.*, p.* from tbl_post p join \
                        tbl_comment c on c.id = %s "
    find_by_id_params = 1,
    # 1번 댓글의 정보와, 1번 댓글이 달려있는 게시글 정보가 조회된다.
    comment = find_by_id(find_by_id_query, find_by_id_params)
    # print(comment)

    # 댓글 정보중에 수정하고 싶은 것을 수정한다.
    comment['content'] = '수정된 댓글입니다.'
    update_query = "update tbl_comment \
                    set name = %s, email = %s, content = %s \
                    where id = %s"
    update_params = (comment.get('name'), comment.get('email'), comment.get('content'), comment.get('id'))
    update(update_query, update_params)
    # print(comment)


    # 댓글 삭제
    # 삭제하고 싶은 댓글 하나와 해당 댓글이 달려있는 게시글 정보를 select한다.
    find_by_id_query = "select c.*, p.* from tbl_post p join \
                            tbl_comment c on c.id = %s "
    find_by_id_params = 2,
    # 1번 댓글의 정보와, 1번 댓글이 달려있는 게시글 정보가 조회된다.
    comment = find_by_id(find_by_id_query, find_by_id_params)

    delete_query = "delete from tbl_comment where id = %s"
    delete_params = comment['id'],

    delete(delete_query, delete_params)


