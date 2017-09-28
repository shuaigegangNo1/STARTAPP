from model.person import Person
import json

personBuild = json.loads('{"id": "15", "lastname": "xin", "firstname": "su", "Address": "china", "city": "suzhou",'
                         ' "telephone": "13424566"}')
person = Person()
person.__dict__ = personBuild
print(person.Address)
# 1: 定义json字符串
# json_str={"name": "lilei","sex": 'man',"age": 18}
# print json_str
# #把一个Python对象编码转换成Json字符串
# print  json.dumps(json_str)

# 把Json格式字符串解码转换成Python对象
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print(s)
print(s.keys())
# print s["name"]
# print s["type"]["name"]
# print s["type"]["parameter"][1]

# # -*- coding: UTF-8 -*-
# import json
#
#
# # 自定义类
# class MyClass:
#     # 初始化
#     def __init__(self):
#         self.a = None
#         self.b = None
#
#
# ##########################
# # 创建MyClass对象
# # myClass=MyClass()
# # 添加数据c
# # myClass.c=123
# # myClass.a=3
# # #对象转化为字典
# # myClassDict = myClass.__dict__
# # #打印字典
# # print (myClassDict)
# # #字典转化为json
# # myClassJson = json.dumps(myClassDict)
# # #打印json数据
# # print (myClassJson)
#
# myClassJson = '{"a": 3, "b": "bb", "c": 123}'
# ##########################
# # json转化为字典
# myClassReBuild = json.loads(myClassJson)
# # 打印重建的字典
# print(myClassReBuild)
# # 新建一个新的MyClass对象
# myClass2 = MyClass()
# # 将字典转化为对象
# myClass2.__dict__ = myClassReBuild;
# # 打印重建的对象
# print(myClass2.a)
