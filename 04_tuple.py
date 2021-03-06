#基本数据类型
#使用r原始字符可以防止\反斜杠的转义。
ss = r'abc\ndef'
print(ss)
#深复制浅复制
#可变对象：list,set,dict    可以直接修改对象本身
#不可变对象：str,tuple     



#元组 tuple
'''
元组的特点：元组是不可变对象
元组的属性及方法：
  .count（obj）统计某个元素在元组中出现的次数
.index（obj）从列表中找某个值第一个匹配项的索引位置
'''
tp = 1,2,3,4
#集合set
'''
集合的创建：{}，set([])
集合的特点：无序，元素不重复
集合的运算：
  & 交集， |并集， -差集 
  成员判断 in、not in
集合的属性及方法：
 s.add(x)     添加单个元素
 s.update()   添加多个元素
 s.remove()   移除元素
 s.clear()    清空集合
'''
sett = {1,2,3,4,5}

#字典
'''
字典的创建：{key:value}    (大括号创建字典的键时要加引号)
            dict(key=value) （括号里赋值方式，名字=对象，不要引号）
字典里的键和值用‘：’隔开，一对键和值组成一个项，项和项之间用‘，’隔开

字典的特点：
1.字典中的元素是无序的
2.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

3.键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
'''
#创建字典：

dict1 = { 'name':'jack' , 'age':20 , 'gender':'male'}
#访问字典中的值：
dict1['name']
'''
字典添加和修改：

新值所要对应的键名如果存在，就是修改操作，如果不存在就相当于添加操作
'''
#添加：
dict1['country'] = 'China'


#修改：
dict1['country'] = 'England'
#in 、not in  判断键在不在字典中，在则返回True 

#字典的属性及方法：
'''
 .update({ })  在字典中添加多个项
        
 .items()      返回字典的各个项
            
 .keys()       返回字典的键
            
 .values()     返回字典的值
	
 .get(k)       如果键k在，返回键k的值，不存在则返回None

 .get(k,x)     如果键k在，返回键k的值，不存在则返回x

 .pop(k)       返回并移除键k所对应的元素，不存在则抛出异常
	
 .pop(k,x)     返回并移除键k所对应的元素，不存在则返回x
'''
#字典的特性总结：
'''
不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。
'''
a = 1
b = 2
a += b
print(a+b)
#运算符：
'''
算术运算符：+ ，- ， *， /， %， **，//
赋值运算符：= ，+=，-=， *=，/=，%=， **=

比较运算符：==，!=， >， <， >=，<=
成员运算符：in , not in
身份运算符：is , is not
     判断两个名字是否指向同一个对象，当id相同时返回True(==比较运算是判断的值)
逻辑运算符：and，or，not，优先级 not>and>or
     and(与) 两个条件都满足时才返回True
     or(或)  有一个条件满足了就返回True
     not(非) 取反
'''
#运算符优先级