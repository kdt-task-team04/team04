from crud_module import *


save_many_query = ("insert into tbl_users (name, username, email, phone, website)"
                   " values (%s, %s, %s, %s, %s)")  # VALUES 절의 괄호가 추가되었습니다.
save_many_params = (
    ('Leanne Graham', 'Bret', "Sincere@april.biz", "1-770-736-8031 x56442", "hildegard.org"),
    ("Ervin Howell", "Antonette", "Shanna@melissa.tv", "010-692-6593 x09125", "anastasia.net"),
    ("Clementine Bauch", "Samantha", "Nathan@yesenia.net", "1-463-123-4447", "ramiro.info")
)

save_many(save_many_query, save_many_params)

save_many_query = ("insert into tbl_address (street, suite, city, zipcode)"
                   " values (%s, %s, %s, %s)")  # VALUES 절의 괄호가 추가되었습니다.
save_many_params = (
    ("Kulas Light", "Apt. 556",  "Gwenborough", "92998-3874"),
    ("Victor Plains", "Suite 879", "Wisokyburgh",  "90566-7771"),
    ("Douglas Extension", "Suite 847",  "McKenziehaven",  "59590-4157")
)
save_many(save_many_query, save_many_params)


# tbl_geo 정보 추가

save_many_query = ("insert into tbl_geo(lat,lng,address_id)"
                   "values (%s,%s,%s)")

save_many_params = (
    ("-37.3159","81.1496",1),
    ("-43.9509","-34.4618",2),
    ("-68.6102","-47.0653",3)
)
save_many(save_many_query, save_many_params)


# 회사 정보 추가

save_many_query = ("insert into tbl_company(name,catchPhrase,bs,user_id)"
                   "values(%s,%s,%s,%s)")

save_many_params = (
    ("Romaguera-Crona", "Multi-layered client-server neural-net","harness real-time e-markets",1),
    ("Deckow-Crist", "Proactive didactic contingency", "synergize scalable supply-chains",2),
    ( "Romaguera-Jacobson","Face to face bifurcated interface","e-enable strategic applications",3)

)

save_many(save_many_query, save_many_params)