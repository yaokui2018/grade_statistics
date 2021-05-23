# -*- coding: UTF-8 -*-
import pymysql
import hashlib
global conn
conn = None
def md5(text):
    """
    获取MD5加密结果
    :param text: 待加密字符串
    """
    text = bytes(text, encoding='utf-8')
    return hashlib.md5(text).hexdigest()


def conn_mysql():
    """
    获取数据库连接
    :return: conn or None(connect fail)
    """
    conn = None
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1', db='grade_statistics',
                               charset='utf8')
    except Exception as e:
        print(e)
    return conn

def sql_execute(sql):
    """
    根据SQL语句操作数据库
    :param sql: 完整SQL语句
    :return: 执行结果
    """
    global conn
    if None == conn:
        conn = conn_mysql()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    # conn.close()
    return result


if __name__ == "__main__":
    print(conn_mysql())
    str_md5 = md5("admin123")
    print('MD5加密后为 ：' + str_md5)
