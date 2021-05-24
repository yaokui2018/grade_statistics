
"""
存放系统中需要多次使用的全局变量
在别的文件使用方法:
import global_var as gl
"""

# 当前登录用户信息
gl_user=(1, 'admin', '0', '0', '0')

# 管理模块标识
FLAG_STUDENT = 1 # 学生管理
FLAG_CLASS = 2 # 班级管理
FLAG_ADMIN = 3 # 角色管理
FLAG_GRADE = 4 # 成绩管理
FLAG_INFO = 5 # 修改资料

# 登录窗口
LOGIN_WINDOW = None
