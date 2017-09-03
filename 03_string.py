#基本数据类型
#字符串
#字符串的创建：单引号，双引号，三引号
#字符串的运算：长度len，	取值，切片，重复*，成员操作in
'''
字符串的方法及属性：
s.count(x)：返回字符串x在s中出现的次数，带可选参数
s.endswith(x)：如果字符串s以x结尾，返回True
s.startswith(x)：如果字符串s以x开头，返回True
s.find(x) ：返回字符串中出现x的最左端字符的索引值，如果不在则返回-1
s.index(x)：返回字符串中出现x的最左端的索引值，如果不在则抛出valueError异常
s.isalpha ()  ：测试是否全是字母，都是字母则返回 True,否则返回 False.
s.isdigit () ：测试是否全是数字，都是数字则返回 True 否则返回 False.
s.islower () ：测试是否全是小写
s.isupper () ：测试是否全是大写
s.lower () ：将字符串转为小写
s.upper () ：将字符串转为大写 
s.replace (x,y) ：子串替换,在字符串s中出现字符串x的任意位置都用y进行替换
s.split()：返回一系列用空格分割的字符串列表
s.split(a,b)：a,b为可选参数，a是将要分割的字符串，b是说明最多要分割几个
'''
s = 'hello world!'
'''
字符串的拼接：
例： a = 'hello'  ,    b = 'python'   ,   c = '!'     将a,b ,c 中的字符串连成一句话。  
第一种方法：用  +   号      
   a + b +c    
第二种方法：格式化字符串  %s   
  '%s %s %s' % (a , b ,c)  （注：s前面可以加对象名，后面以字典的方式填入
第三种方法：''.join()方式，注意括号里是要连接的可以是列表，元祖   
      ' '.join([a,b,c])  （注：''里面是连接后面各个字符串的字符）
第四种方法：.format方式
   '{}{}{}'.format(a,b,c)    (注：{}里面可以填入与后面相对应的符号)

format方法详解：
'{}{}{}'.format(a,b,c)
当{}里面是空的时候，里面默认索引为0，1，2按format括号里的顺序依次填入
'{1}{2}{0}'.format(a,b,c)
当{}里面有索引值时，按前面的索引值将后面的每项依次填入
'{n1}{n2}{n3}'.format(n1=a,n2=b,n3=c)
{}里面可以指定对象名称，后面通过赋值的方式给前面的相应的值，后面是无序的
'''
a = 'hello'
b = 'python'
c = '！'
x1 = a + b + c
x2 = '%s %s %s '%(a,b,c)
x3 = ' '.join([a,b,c])
x4 = '{} {} {}'.format(a,b,c)
import time
date = time.asctime(time.localtime())
info = '现在的时间是%s.'%date
print(info)
'''
%s 格式化字符串
%d 格式化整数
%f 格式化小数
%c 格式化ASCII字符
%o 格式化八进制
%x 格式化十六进制
%e 用科学计数法格式化


-  用作左对齐
+ 用在正数前面显示加号
m.n  m是显示的最小长度，当m大于格式化位数时才起作用显示m位，
            n是代表小数的位数。
'''
#字符串转义
'''
\'  单引号    \"双引号

\n 换行   \a提示音  \b退格键  \r回车键  \t横向制表符 \f换页

'''
