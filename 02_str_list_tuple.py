#数字类型
#整型 int
#浮点型 float
#布尔 bool  True == 1, False ==0
#复数类型 complex
#算术运算符：+ - * /  //  %  **
#赋值运算符：=   +=    -=  *=
a = 12
b = 7
a += b  # a = a+b
#min() max() 求最大值最小值
#序列类型
#字符串str ,列表list ,元组tuple
#里面的每一个元素都有自己的编号，可以称之为索引
#序列的创建
#字符串的创建 ：单引号，双引号，三引号,但必须成对出现
ss1 = 'abasc'
ss2 = "python"   
ss3 = '''ssa
sjfsjfo'''
#列表的创建：[] 中括号，各元素之间用逗号隔开,
ll1 = [1,2,3]
#元组的创建：（）小括号，直接用逗号隔开各元素
tp = 4,5,6
#序列的通用操作
#索引取值切片,正向索引，反向索引
#类型转换 str() ,list() ,tuple()
#可变对象：list ,dict
#不可变对象：str ,tuple
#相加+
#重复*
#检查成员  in  ,   not in
#列表的方法
'''
  L.append(obj) 在列表末尾添加新的对象。
  L.clear() 清空整个列表。
  L.copy() 复制列表，和L[:]的复制方式一样属于浅复制。
  L.count(obj) 统计某个元素在列表中出现的次数。
  L.extend(seq) 用新列表扩展原来的列表。
  L.index(obj) 从列表中找某个值第一个匹配项的索引位置。
  L.insert(index,obj) 插入元素，可以指定位置。
  L.pop(obj=list[-1]) 出栈，可以指定位置。
  L.remove(obj) 移除指定元素从左边开始的第一个。
  L.reverse() 反向列表中元素。
  L.sort() 对原列表进行排序。
'''
#内置函数sortd()reversed()