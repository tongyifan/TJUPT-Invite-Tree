from threading import Lock

import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

DB_NAME = ''
DB_USER = ''
DB_PASS = ''
DB_HOST = ''
DB_PORT = 5432


@app.route('/')
def tree():
    try:
        uid = int(request.args.get('uid', 0))
    except ValueError:
        return render_template('index.html', msg="错误：UID是数字啦!", data=[]), 418
    if not uid:
        username = request.args.get('username', '')
        if username:
            uid = db.get_uid_by_username(username)
        else:
            return render_template('index.html', msg="欢迎使用TJUPT邀请树，请输入UID或用户名", data=[])
    if not uid:
        return render_template('index.html', msg="错误：未找到用户", data=[]), 400
    else:
        privacy = db.check_privacy(uid)
        if privacy[0][0]:
            return render_template('index.html', msg="错误：用户隐私等级为高!", data=[]), 403
        else:
            data = db.select_tree(uid)
            return render_template('index.html', msg="",
                                   data=[{'uid': i[0], 'alive': i[1], 'name': i[2], 'master': i[3]} for i in data])


class Database:
    _commit_lock = Lock()

    def __init__(self):
        self.conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

    def exec(self, sql, *args):
        with self._commit_lock:
            cur = self.conn.cursor()
            cur.execute(sql, args)
            data = cur.fetchall()
        return data

    def select_tree(self, uid):
        data = self.exec('''
with recursive tree as (
    select uid, alive, username, master
    from users
    where uid = %s
    union all
    select origin.uid, origin.alive, origin.username, origin.master
    from tree
             join users origin
                  on origin.master = tree.uid and origin.privacy = 0
)
select *
from tree;
''', uid)
        return data

    def check_privacy(self, uid):
        return self.exec("SELECT privacy FROM users WHERE uid = %s LIMIT 1", uid)

    def get_uid_by_username(self, username):
        uid = self.exec("SELECT uid FROM users WHERE username = %s LIMIT 1", username)
        return uid[0][0] if len(uid) > 0 else 0


db = Database()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
