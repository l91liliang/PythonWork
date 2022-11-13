"""
example01 - 分支结构（选择结构）的例子

代码中有多条执行路径，但是只有其中一条会被执行

admin/Admin123

Author: larry
Date: 10/2/22

"""
import getpass  # 以掩码方式输入密码

username = input('用户名：')
if username == 'admin':
    password = getpass.getpass('请输入密码：')  # 需要在终端中运行。
    if password == 'Admin123':
        print('登录成功！')
    else:
        print("登录失败。")
else:
    print("无此用户。")
