"""
集中存放项目中需要用到的SQL语句
"""
from grade_statistics.src.vals.db import md5


def login(username, password):
    """
    管理员登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    password = md5(password)
    return "select * from admin where a_username='%s' and a_password='%s'" % (username, password)


def getClassList(idStr, name):
    """
    根据id查询班级列表
    :param idStr: id，多个用','分隔。0表示获取所有数据
    :return:
    """
    sql = "select * from class_ where c_name like '%" + name + "%'"
    if idStr == "0":
        pass
    else:
        sql += " and c_id in (" + idStr + ")"
    print(sql)
    return sql


def getStudentById(id):
    """
    获取学生info
    :param id: s_id
    :return:
    """
    sql = "select * from student where s_id=" + str(id)
    print(sql)
    return sql


def getStudentByClassId(id):
    """
    获取学生info
    :param id: 班级id
    :return:
    """
    sql = "select * from student where s_class=" + str(id)
    print(sql)
    return sql


def getStudentList(classids, name):
    """
    获取学生列表
    :param classids: 学生所在班级id，多个用逗号间隔。0表示获取所有数据
    :return:
    """
    sql = "select * from student where s_realname like '%" + name + "%'"
    if classids == "0":
        pass
    else:
        sql += " and s_class in (" + classids + ")"
    sql += " order by s_number"
    print(sql)
    return sql


def getGradeList(classids, name):
    """
    获取学生成绩列表
    :param classids: 学生所在班级id，多个用逗号间隔。0表示获取所有数据
    :return:
    """
    sql = "select * from student where s_realname like '%" + name + "%'"
    if classids == "0":
        pass
    else:
        sql += " and s_class in (" + classids + ")"
    sql += " order by s_chinese + s_math + s_english DESC"
    print(sql)
    return sql


def getAdminList(name):
    """
    获取管理员列表
    :param name: 用户名
    :return:
    """
    sql = "select * from admin where a_username like '%" + name + "%'"
    sql += " order by a_id"
    print(sql)
    return sql


def getAdminById(id):
    """
    获取管理员信息
    :param id: 管理员id
    :return:
    """
    sql = "select * from admin where a_id=" + str(id)
    print(sql)
    return sql


def delStudentById(id):
    sql = "delete from student where s_id=" + str(id)
    print(sql)
    return sql


def delClassById(id):
    sql = "delete from class_ where c_id = " + str(id)
    print(sql)
    return sql


def delAdminById(id):
    sql = "delete from admin where a_id = " + str(id)
    print(sql)
    return sql


def delStudentByIds(ids):
    sql = "delete from student where s_id in " + ids
    print(sql)
    return sql


def updateStudentById(id, name, number, sex, class_):
    sql = "update student set s_realname='%s',s_number=%s,s_sex=%s,s_class=%s where s_id=" % (
        name, number, sex, class_) + str(id)
    print(sql)
    return sql


def updateGradeById(id, chinese, math, english):
    sql = "update student set s_chinese=%s,s_math=%s,s_english=%s where s_id=" % (chinese, math, english) + str(id)
    print(sql)
    return sql


def updateGradeByNum(num, chinese, math, english):
    sql = "update student set s_chinese=%s,s_math=%s,s_english=%s where s_number=" % (chinese, math, english) + str(num)
    print(sql)
    return sql


def updateClassById(id, name):
    sql = "update class_ set c_name='%s' where c_id=" % name + str(id)
    print(sql)
    return sql


def updateAdminById(id, username, mark, classids):
    sql = "update admin set a_username='%s',a_mark='%s',a_classid='%s' where a_id=" % (username, mark, classids) + str(
        id)
    print(sql)
    return sql

def updateUsernameById(id, username):
    sql = "update admin set a_username='%s' where a_id=" % username + str(id)
    print(sql)
    return sql


def resetAdminPasswById(id, passw):
    passw = md5(passw)
    sql = "update admin set a_password='%s' where a_id=" % passw + str(id)
    print(sql)
    return sql


def insertStudent(name, number, sex, class_):
    sql = "insert into student (s_realname,s_number,s_sex,s_class) VALUES ('%s',%s,%s,%s)" % (
        name, str(number), sex, str(class_))
    print(sql)
    return sql


def insertClass(name):
    sql = "insert into class_ (c_name) VALUES ('%s')" % name
    print(sql)
    return sql


def insertAdmin(username, passw, mark, classids):
    passw = md5(passw)
    sql = "insert into admin (a_username,a_password,a_mark,a_classid) VALUES ('%s','%s','%s','%s')" % (
        username, passw, mark, classids)
    print(sql)
    return sql


if __name__ == "__main__":
    print(getClassList("1,2,3"))
