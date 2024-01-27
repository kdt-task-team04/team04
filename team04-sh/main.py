from connection_module import *
from crud_module import *
from main_class import *
#
if __name__ == '__main__':
    find_by_id_query = "select id,name,username,email,phone,website from tbl_users where id = %s"
    # find_by_id_params = 1,
    # find_by_id_params = 2,
    find_by_id_params = 3,
    users = find_by_id(find_by_id_query, find_by_id_params)
    user_id = users.get('id')

    # todos 정보 추가
    save_many_query = ("insert into tbl_todos (user_id,title, completed) "
                       "values (%s,%s, %s)")
    save_many_params = (
        # (user_id, "delectus aut autem", False),
        # (user_id, "et porro tempora", False),
        # (user_id, "fugiat veniam minus", False),
        # (user_id, "distinctio vitae autem nihil ut molestias quo", True),
        (user_id, "voluptatum omnis minima qui occaecati provident nulla voluptatem ratione", True),

    )
    save_many(save_many_query, save_many_params)
#
#     #
    # 유저 정보 추가
    save_many_query = ("insert into tbl_users (name, username, email, phone, website)"
                       " values (%s, %s, %s, %s, %s)")  # VALUES 절의 괄호가 추가되었습니다.
    save_many_params = (
        ('Leanne Graham', 'Bret', "Sincere@april.biz", "1-770-736-8031 x56442", "hildegard.org"),
        ("Ervin Howell", "Antonette", "Shanna@melissa.tv", "010-692-6593 x09125", "anastasia.net"),
        ("Clementine Bauch", "Samantha", "Nathan@yesenia.net", "1-463-123-4447", "ramiro.info")
    )

    save_many(save_many_query, save_many_params)
