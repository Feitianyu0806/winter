d = {"name":"小明"}  # 创建一个变量d=赋值"name":"小明"
d.update(sex="男",age=18) #将sex="男",age=18加入到变量d当中
print(d)#打印出结果{'name': '小明', 'sex': '男', 'age': 18}

d = {"name":"小明"}#创建一个变量d=赋值"name":"小明"
t = {"sex":"男","age":18}#创建一个变量t=赋值"sex":"男","age":18
d.update(t) #把变量t的内容加入变量d里面
print(d) #打印出结果{'name': '小明', 'sex': '男', 'age': 18}

d = {"name":"小明","sex":"男","age":18}#创建一个变量d=赋值"name":"小明","sex":"男","age":18
d.pop("sex")#删除字典中的性别key和值
print(d)#打印出结果{"name":"小明","age":18}

d = {"name":"小明","sex":"男","age":18}#创建一个变量d=赋值"name":"小明","sex":"男","age":18
d.clear() #清空字典
print(d) #打印出结果{}



f = open("E:\\softwaredata\\python\\gy-1911A\\test.txt","w",encoding="utf-8") #创建一个变量f=赋值 open打开文件 E:\\softwaredata\\python\\gy-1911A\\test.txt" 绝对路径 "w"写入 encoding="utf-8" 防止出现中文乱码
f.write("你好，师姐\n") #写入你好师姐
f.writelines(["123123123\n","1234sfsfsf\n","sfsfsdf\n"]) #写入列表["123123123\n","1234sfsfsf\n","sfsfsdf\n"]
f.close()#关闭文件 记得打开以后要关闭文件噢




f = open("test.txt",'r',encoding="utf-8")#创建一个变量f=赋值 open打开文件 test.txt 文件名 'r' 阅读 encoding="utf-8" 防止出现中文乱码
# c = f.read()   创造一个变量c=赋值f.read()  相当于把read 阅读的指令存入变量c
# print(c)  打印出变量c的结果
# lines = f.readlines()   #创造一个变量lines=赋值f.readlines() 相当于把readlines阅读以列表形式展示的指令存入变量lines
# print(lines)  打印出lines变量的结果
line = f.readline()  #创造一个变量line=赋值f.readline() 相当于把readline阅读以列表形式展示的指令存入变量line 只查看一条
print(line) #打印出变量line的结果
f.close()#关闭文件 记得打开以后要关闭文件噢

with open("test.txt",'r',encoding="utf-8") as f: #创建一个变量f as 等于 with open("test.txt",'r',encoding="utf-8") with open 打开 test.txt 文件名 'r' 阅读 encoding="utf-8" 防止出现中文乱码
c = f.read() #创建一个变量c=赋值阅读查看f变量
print(c) #打印出test.txt文件的全部内容


class Product(): #创建一个类Product()
size="6寸"  #创建一个变量size=赋值"6寸"
def __init__(self,color): #def定义一个__init__()方法 只有在类实例化的时候才会自动调用
self.color=color #把self.color变量存入 color中 可以在后面引用

def call(self):#def定义一个call方法
print("hello") #打印hello
def send_message(self):#def定义一个send_message()方法
print("你有一个快递！") #打印你有一个快递！
phone1 = Product("土豪金") #把类实例化存入phone1变量中 方便后面引用 并传入参数土豪金给init方法
print(phone1.color) #调用phone1.color 打印出结果土豪金
print(phone1.size)#调用phone1.size 打印出结果6寸
phone1.call() #调用call方法 结果是print("hello") 打印hello

from gy_A.module_A import Product  #从gy_A 文件夹.module_A 文件名中获取Product类 可以在当前文件中使用

import json  #调用json内置函数
j = ''' 
{"name":"小明", 
"sex":null 
} 
'''
#创建一个变量j=赋值{'name': '小明', 'sex': None}
d = json.loads(j) #创建一个变量d=赋值json.loads json转字典
print(d)  #打印{'name': '小明', 'sex': None}
d["sex"] = "男" #修改sex这个key的值为"男"
print(d) #打印出结果为{'name': '小明', 'sex': '男'}

import json #调用json内置函数
d ={"name":"小明","sex":None} #创建一个变量d=赋值"name":"小明","sex":None 字典
j = json.dumps(d,ensure_ascii=False) #创建一个变量j=赋值 json.dumps()语法  ensure_ascii=False防止乱码  字典转json
print(j) #打印出结果为{"name": "小明", "sex": "男"}


import random#调用random内置函数 random随机模块函数
a = random.randint(10,20) #创建一个变量a=赋值random.randint(10,20) random.randint随机取值
print(a) #打印出a变量的内容  在10，20之间随机一个数


import random  #调用random内置函数 random随机模块函数
s = "abcdefghi"  #创建一个变量s=赋值abcdefghi
c = random.choice(s) #把这个s的变量放进random.choice里面并用c存起来 random.choice随机选择一个元素
print(c)  #打印出c变量的内容 随机选择一个abcdefghi字符串里的值


import os  #调用os内置函数
p = os.path.abspath(__file__) #创建一个变量s=赋值os.path.abspath(__file__)
print(p)#打印出当前文件的绝对路径 E:\software\python\wudi\QAQ.py
d = os.path.dirname(p)#创建一个变量d=赋值os.path.dirname()
print(d)#打印出这个文件所在的目录 E:\software\python\wudi
f = os.path.basename(p)#创建一个变量f=赋值os.path.basename() 显示出文件名
print(f)#打印出这个文件的文件名 QAQ.py
path = os.path.join(d,f) #创建一个变量path=赋值os.path.join(d,f) d是文件所在目录 f是文件名
print(path)#打印结果  join 拼接文件名和路径E:\software\python\wudi\QAQ.py
os.mkdir("gy_C") #os.mkdir() 在该文件的目录里创建一个文件夹 "gy_C"