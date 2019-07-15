# TJUPT-Invite-Tree

应叶子之邀写的一个邀请树查询系统，查询速度还是挺快的

随手糊的代码比较粗糙，就不要深究代码上的问题了= =

## 部署方式
0. 准备工作
```bash
git clone https://github.com/tongyifan/TJUPT-Invite-Tree.git
cd TJUPT-Invite-Tree
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```
1. 使用`tree.sql`建表，你可能需要修改/删除[赋权语句](https://github.com/tongyifan/TJUPT-Invite-Tree/blob/master/tree.sql#L30)
2. 使用update.py把MySQL数据库中的`users`表中数据导入PostgreSQL数据库的`users`表中
3. 直接运行或用uWSGI等方式把invite_tree.py跑起来
4. 直接访问/使用nginx反代来提供最终服务