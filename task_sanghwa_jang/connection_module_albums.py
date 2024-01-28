# 43.202.58.90
import pymysql
from pymysql.cursors import Cursor

def connect():
    conn = pymysql.connect(host='43.202.58.90', user='mysql', passwd='1234', db='comments', charset='utf8', autocommit=False)
    # cursor : 내가 작성한 쿼리가 직접 실행될 수 있게 해주는 객체
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        conn, cursor = connect()
        try:
            result = crud(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()

        # 오류 발생 여부와 상관없이 무조건 닫아야함.
        finally:
            cursor.close()
            conn.close()

        return result

    return manage
