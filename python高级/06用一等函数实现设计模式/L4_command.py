# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 下午6:57
# @Author  : Clarence_Liao
# @FileName: L4_command.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/liao-sir/

'''
   我们可以创建一个类，管理所有命令，并且将其实例重写为可调用对象
'''

class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()

