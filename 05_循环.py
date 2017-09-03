#控制流程
# if 判断语句
'''
基本形式：
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
'''
if语句
注意事项：
1.判断条件的表达式的值一般为布尔型的值，当值为True就执行里面的语句块。
  一般是使用比较运算符或者成员运算符。
2.条件表达式后面接的“:”是语法的一部分不能少。
  有了“:”号后，满足条件时要的执行语句以缩进后的形式写在下面。
3.if，elif是写分支条件，当前面的if和elif不满足时就执行else里面的语句。
  可以有零到多个elif，else是可选的。
4.语句是从上往下执行的，当前面有条件已经满足了，那么直接执行里面的语句。
  后面的条件判断不再执行。

#input() 读取键盘输入，返回字符串
#猜字游戏
import random
a = random.randint(1,10)
n = 0
while n<3:
    number = input('请输入数字：')
    if number.isdigit():
        number = int(number)
        if number==a:
            print('猜对了')
            break
        elif number > a:
            print('大了，大了')
        else:
            print('小了，小了')
        #print('这个数是：',a)
    else:
        print('你输入的不是数字')
    n+=1
else:
    print('3次机会用完了')
    print('这个数是：',a)
#循环
#while循环
#break跳出整个循环，并且不会执行else里面的语句
#continue 跳出本次循环
#else
#pass
a = 1
while a<10:
    a+=1
    if a == 5:
        continue
    print(a)
'''
#for 循环，for迭代
#range() range(0,100,2)
#用循环来写0-100之间的偶数
'''
x = 0
while x<=100:
    if x%2==0:
        print(x)
    x +=1
while x<=100:
    print(x)
    x +=2

li = []
for i in range(101):
    if i%2==0:
        li.append(i)
print(li)
  
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('xxxxx')
  '''
'''
import random
a = random.randint(1,10)
for i in range(3):
    number = input('请输入数字：')
    if number.isdigit():
        number = int(number)
        if number==a:
            print('猜对了')
            break
        elif number > a:
            print('大了，大了')
        else:
            print('小了，小了')
        #print('这个数是：',a)
    else:
        print('你输入的不是数字')
else:
    print('3次机会用完了')
    print('这个数是：',a)
    
'''
#写个完整的猜字游戏
#分数等级测试，可以循环测试的。
'''
 写一个程序用来判定分数的等级，总分为100分，
 90以上为等级A，大于等于80小于90为等级B，
 大于等于60小于80为等级C，小于60分为等级D，
 输入的分数不在0~100中时显示输入有误。
'''
x= 1
if x>0:
    pass
else:
    print('xxx')
