import datetime

from crud_module import *
from user import User
from address import Address
from geo import Geo
from company import Company
import hashlib

# if __name__ == '__main__':
    # 유저 정보 추가
    # save_many_query = ("insert into tbl_users (name, username, email, phone, website)"
    #                    " values (%s, %s, %s, %s, %s)")  # VALUES 절의 괄호가 추가되었습니다.
    # save_many_params = (
    #     ('Leanne Graham', 'Bret', "Sincere@april.biz", "1-770-736-8031 x56442", "hildegard.org"),
    #     ("Ervin Howell", "Antonette", "Shanna@melissa.tv", "010-692-6593 x09125", "anastasia.net"),
    #     ("Clementine Bauch", "Samantha", "Nathan@yesenia.net", "1-463-123-4447", "ramiro.info")
    # )

    # address 추가
    # save_many_query = ("insert into tbl_address (street, suite, city, zipcode,user_id)"
    #                    " values (%s, %s, %s, %s , %s)")  # VALUES 절의 괄호가 추가되었습니다.
    # save_many_params = (
    #     ("Kulas Light", "Apt. 556",  "Gwenborough", "92998-3874", 1),
    #     ("Victor Plains", "Suite 879", "Wisokyburgh",  "90566-7771", 2),
    #     ("Douglas Extension", "Suite 847",  "McKenziehaven",  "59590-4157",3)
    # )
    # save_many(save_many_query, save_many_params)

    # # tbl_geo 정보 추가
    #
    # save_many_query = ("insert into tbl_geo(lat,lng,address_id)"
    #                    "values (%s,%s,%s)")
    #
    # save_many_params = (
    #     ("-37.3159","81.1496",1),
    #     ("-43.9509","-34.4618",2),
    #     ("-68.6102","-47.0653",3)
    # )
    # save_many(save_many_query, save_many_params)

    # # 회사 정보 추가

    # save_many_query = ("insert into tbl_company(name,catchPhrase,bs,user_id)"
    #                    "values(%s,%s,%s,%s)")
    #
    # save_many_params = (
    #     # ("Romaguera-Crona", "Multi-layered client-server neural-net","harness real-time e-markets",1),
    #     # ("Deckow-Crist", "Proactive didactic contingency", "synergize scalable supply-chains",2),
    #     # ( "Romaguera-Jacobson","Face to face bifurcated interface","e-enable strategic applications",3),
    #     ("fff-sss", "Fssse to fassssed interface", "gggggcations", 4),
    #     ("www-rrr", "fffd interface", "eddddfflications", 4)
    #
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 유저 상세보기
    # find_by_id_query = "select id, name, username, email, phone, website \
    #                     from tbl_users \
    #                     where id = %s"
    # find_by_id_params = 4,
    # user = find_by_id(find_by_id_query, find_by_id_params)
    #
    # users_find = Address(user.get("id"), user.get("name"), user.get("username"), user.get("email"), user.get("phone"), user.get("website"))
    # print(users_find.__dict__)
    # 유저 목록
    # find_all_by_query = "select u.id, u.name, u.email, u.phone \
    #                          from tbl_users u join tbl_address a \
    #                          on u.id = a.user_id \
    #                          order by id desc"
    # addresses = find_all(find_all_by_query)
    # for address in addresses:
    #     print(address)

    # 주소 상세보기
    # find_by_id_query = "select id, street, suite, city, zipcode \
    #                     from tbl_address \
    #                     where id = %s"
    # find_by_id_params = 4,
    # address = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select u.id, u.name, u.email, u.phone \
    #                     from tbl_users u join tbl_address a \
    #                     on u.id = %s and u.id = a.user_id"
    #
    # users = find_all_by(find_all_by_query, find_by_id_params)
    #
    # address_find = Address(address.get("id"), address.get("street"), address.get("suite"), address.get("city"), address.get("zipcode"), users)
    # print(address_find.__dict__)
    #
    # # 주소 목록
    # find_all_by_query = "select a.id, a.street, a.suite, a.city, a.zipcode \
    #                      from tbl_users u join tbl_address a \
    #                      on u.id = a.user_id \
    #                      order by id desc"
    # addresses = find_all(find_all_by_query)
    # for address in addresses:
    #     print(address)

    # 주소 업데이트
    # update_id = 1
    # update_query = "update tbl_address " \
    #                "set street =  %s, suite = %s, city = %s, zipcode = %s " \
    #                "where id = %s"
    # update_params = ['29382 street', '29382 suite', '29382 city', '38487', update_id]
    # update(update_query, update_params)

    # 회원 삭제
    # delete_query = "delete from tbl_users where id = %s"
    # delete_params = 1
    #
    # delete(delete_query, delete_params)

    # geo 상세보기
    # find_by_id_query = "select id, lat , lng, address_id \
    #                     from tbl_geo \
    #                     where id = %s"
    # find_by_id_params = 4,
    # address = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select g.id, a.street, a.city, a.suite, a.zipcode \
    #                     from tbl_geo g join tbl_address a \
    #                     on g.id = %s and a.id = g.address_id"
    #
    # addresses = find_all_by(find_all_by_query, find_by_id_params)
    #
    # address_find = Geo(address.get("id"), address.get("lat"), address.get("lng"), addresses)
    # print(address_find.__dict__)


    #geo 목록
    # find_all_by_query = "select g.id, g.lat, g.lng, a.street, a.city, a.suite \
    #                      from tbl_address a join tbl_geo g \
    #                      on a.id = g.address_id \
    #                      order by id desc"
    # geos = find_all(find_all_by_query)
    # for geo in geos:
    #     print(geo)

    # geo 업데이트
    # update_id = 1
    # update_query = "update tbl_geo " \
    #                "set lat = %s, lng = %s " \
    #                "where id = %s"
    # update_params = ['-23.333333', '33.2222222', update_id]
    # update(update_query, update_params)

    # 회사 상세보기
    # find_by_id_query = "select id, name, catchPhrase, bs, user_id  \
    #                     from tbl_company \
    #                     where id = %s"
    # find_by_id_params = 3,
    # companies = find_by_id(find_by_id_query, find_by_id_params)
    #
    # find_all_by_query = "select u.id, u.name, u.email, u.phone \
    #                     from tbl_users u join tbl_company c \
    #                     on u.id = %s and u.id = c.user_id"
    #
    # users = find_all_by(find_all_by_query, find_by_id_params)
    #
    # address_find = Company(companies.get("id"), companies.get("name"), companies.get("catchPhrase"), companies.get("bs"), users)
    # print(address_find.__dict__)

    # 회사 목록
    # find_all_by_query = "select c.id, c.name, c.catchPhrase, c.bs, c.user_id \
    #                      from tbl_users u join tbl_company c \
    #                      on u.id = c.user_id \
    #                      order by id desc"
    # addresses = find_all(find_all_by_query)
    # for address in addresses:
    #     print(address)

    # 회사 업데이트
    # update_id = 7
    # update_query = "update tbl_company " \
    #                "set name =  %s, catchPhrase = %s, bs = %s " \
    #                "where id = %s"
    # update_params = ['kebin-clean', 'database', 'revolustions woo', update_id]
    # update(update_query, update_params)

    # 회사 삭제
    # delete_query = "delete from tbl_company where id = %s"
    # delete_params = 6
    #
    # delete(delete_query, delete_params)









