from datetime import datetime

import psycopg2
import psycopg2.extras
import pymysql

from invite_tree import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

MYSQL_USER = ''
MYSQL_PASS = ''
MYSQL_NAME = ''
MYSQL_HOST = ''
MYSQL_PORT = 3306


def update():
    try:
        mysql = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASS, db=MYSQL_NAME,
                                host=MYSQL_HOST, port=MYSQL_PORT, charset='utf8')
        mysql_cur = mysql.cursor()
        mysql_cur.execute('''
        SELECT 
            `id`,
            `username`,
            `privacy`='strong',
            `enabled`='yes',
            `invited_by`
        FROM `users`
        ''')
        data = list(mysql_cur.fetchall())
        ps = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        ps.autocommit = True
        ps_cur = ps.cursor()
        ps_cur.execute("TRUNCATE TABLE users")
        query_sql = "INSERT INTO users (uid, username, privacy, alive, master) VALUES %s"
        psycopg2.extras.execute_values(
            ps_cur, query_sql, data, template=None
        )
        print("[%s] 更新成功" % datetime.now())
    except Exception as e:
        print("[%s] 更新失败：%s" % (datetime.now(), repr(e)))


if __name__ == '__main__':
    update()
