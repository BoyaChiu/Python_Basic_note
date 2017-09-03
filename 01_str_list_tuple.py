#名字和对象   name = object
'''名字是以字母数字下划线组成，但名字不能以数字开头，区分大小写。
“=” 作用就是赋值，给对象一个名字后就可以通过这个名来调用这个对象。
一个名字名字对应一个对象，后创建的对象会覆盖掉先创建的对象。
关键字del用来删除对象，名字被删除这个对象也就被删除了
'''
## 单行注释  三引号多行注释
#类型与类
'''通过内置函数type()查看对象类型
基本数据类型：
数字类型: int ,float,bool complex
字符串类型：str ,(bytes)
列表：list
元组：tuple
字典：dict
集合：set
不同类型的对象有不同的属性和方法
类型也是一个类，通过关键字class创建我们自己的类，定义这个类的属性和方法。
'''
a = 12
b = "python"
c = [1,2,3,4]
d = 4,5,6
print(d)

e = {'a':1,'b':2}
f = {2,3,4}
#print(a,b,c,d)
class Fruits:
    def __init__(self,name):
        self.name = name
    def eat(self):
        return 'lalalla'
fr1 = Fruits('apple')

#关键字
'''关键字是在python中有特殊作用的单词
在idle里面关键是以橘色显示
导入keyword模块，可以查看所有的关键字
'''
import keyword
print(keyword.kwlist)

#流程
#在python中语句都是从上往下执行的，函数是先创建好了调用时才会执行

def fun():
    a = 'xxxx'
    print(a,b)
    return 'hahahhahah'

print(a)
print(fun())
print(33333)

#作用域
#不同空间的相同名字表示的是不同的对象
#这个函数里面的a和外面的定义的a = 12是存在于不同作用域的两个对象

#异常
#看懂并知道怎么解决报错


# 模块及包
#内置模块  自定义模块
