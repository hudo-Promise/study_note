### 变量

```python
'''
变量:就是可以变化的量，量指的是事物的状态。（先定义后引用）
变量名 = 变量值
id 反映的是变量值的内存地址，内存地址不同id则不同
type 不同类型的值用来记录不同的状态
value 值本身

变量名：指向变量值的内存地址，用来来访问变量值
1. 变量名只能是 字母、数字或下划线的任意组合
2. 变量名的第一个字符不能是数字
3. 关键字不能声明为变量名，常用关键字如下

['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from','global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

is 与 ==
is 比较左右两个值身份ID是否相等
== 比较俩个值是否相等

# 小整数池---为程序开辟一个整数空间
'''
```

### 常量

```python
'''
python并没有常量的概念，通常我们以变量名全大写的形式表示变量
'''
```

### 基本数据类型

```python
# 整形 int
age =18
以整数的类型记录数据

# 浮点型 float
money = 100.00
以小数的是形式记录数据
整形与浮点型可以进行相加 整形会被强制转换为浮点型

# 字符串类型 str
name = "张三"
记录描述性质的状态
字符串可以与字符串相加 相当于拼接
字符串与数字相乘 相当于复制拼接

# 列表 list
lis = [1, 2.3, 'aaa',[ 4, 5]]
列表通过索引取值 索引从0开始
列表是有序的
索引:值的内存地址

# 字典 dict
dic = {'name':'张三', 'age':18, '爱好':['唱','跳','rap']}
key与 values 通过键与值一一对应的关系实现数据存储，其中字典的key必须是不可变类型。value可以是任意类型
字典是无序的

# 布尔类型 boolean
记录状态
```

### 引用

```python
# 直接引用和间接引用
直接引用：变量名直接指向内存地址
间接引用：通过索引对应的内存地址 引用值

引用计数
	增加引用计数 
	减少引用计数 减少到零则回收资源

标记清除(可以避免循环引用)
	先扫描栈区的变量名，从变量名出发在堆区寻找直接指向的内存地址和间接指向的内存地址，被指向的地址标记为存活,没有被指向的地址，则清除。
    
垃圾回收---分代回收
```

### 可变与不可变类型

```python
'''
所有的赋值操作都会开辟一个新的内存空间
'''
可变类型：值改变，id不变
list dict set
不可变类型：值改变，id也改变
int float str tuple bool
```

### 运算符和优先级

```python
and 逻辑与 （第二高）
or  逻辑或
not 逻辑非（优先级最高）
in  判断元素是否存在（字典需要判断Key）
not in 判断元素是否存在（字典需要判断Key）

```

### 深浅拷贝

```python
'''拷贝一定得到了一个新的列表'''
# 深拷贝
import copy
copy.deepcopy()
不可变类型直接指向原先的数据 可变类型产生新的内存空间
# 浅拷贝
	把原列表第一层的内存地址不加区分完全拷贝一份给新列表  （如果原列表中全是不可变类型，浅拷贝不存在问题）
```

### 纯计算无io的死循环会引起致命的效率问题

### 数据类型

```python
int()
bin() 转二进制  oct() 转八进制   hex() 转十六进制
float()
str()
'''
取值---按索引取（正向取 写整数 反向取 写负数）
切片---[0:5]  （原字符串不变 复制出一个新字符串 （顾头不顾尾）[0:5:1] 第三个参数为步长 
				[5:0:-1] 步长为负反向切 默认步长为1 省略参数表示从头开始）
移除空白---strip(), lstrip(), rstrip()       strip('*') 只去俩边 不去中间
切分---split()  默认按照空格分隔 split() 括号内可以指定分隔符和 切割次数split('#', 1)
获取长度---len()
转大小写---lower() upper()
判断开头结尾---startswith()  endswith()
format
lsplit rsplit
拼接字符串---join() 例如 ':'.join(l)   # l是一个列表
替换---replace()   replace('old', 'new', 2) # 第三个参数表示替换的个数 省略默认全部替换
判断是否是纯数字---isdigit()
了解：find()  index()  count() center()  ljust()  rjust()  zfill()
'''
list()
'''
类型转换： list(可迭代对象)
按索引取值---lis[索引]  正数正向区 负数反向取  修改是取出直接赋值
追加内容--- lis.append() 追加至末尾
插入---lis.insert() insert(索引，'插入内容')
以单个值的形式追加多个值---extend()   lis.extend('可迭代对象')
删除---pop()根据索引删除，默认删除最后一个元素    remove() 指定元素内容删除  del lis[1] 只删除
切片---lis[0:5:2] 顾头不顾尾 切片等同于浅拷贝
统计长度---len()
count()---统计元素出现次数
index()---查询元素索引
clear()---清除列表
reverse()---将列表翻转
sort()---排序 sort(reverse=False) 默认从小到大排 reverse=True 从大到小排  前提：列表中元素必须同种类型

列表和字符串比大小都是比较对应位置上的元素在ASCII码中的大小
'''
tuple()
'''
不可变类型 内存地址不可变 如果元组中的元素为可变类型 那么该元素可以改变，其地址不变
如果元组只有一个元素 创建时 需要加逗号 tup = (10,) 
tup[0] 正反向取
切片 [0:9:3]
长度 len()
'''
dict()
'''
key 必须为不可变类型 且不可重复
dic = {'k1':'value1', 'k2':'value2', 'k3':'value3',}
dic = {} 默认定义出来的是空字典
dic = {x=1, y=2, c=3}
dict()---生成字典
dic['key'] = value 存在则修改 不存在则追加
len()---获取长度
in   not in 成员运算
del  根据键删
pop()  根据键删  返回value
popitem()  随机删  返回一个元组（key, value）
# 在python2中
keys()  取出字典的key   在python3中生成一个能生成key的对象
values()  取出字典的value  在python3中生成一个能生成value的对象
items()  取出字典的key, value  在python3中生成一个能生成key, value的对象
clear()  清空
get()  按key取 不存在返回None
update() 用新字典更新老字典
setdefault(key, value) key不存在则添加 存在则返回key对应的值  
'''
set()
'''
集合内必须为不可变类型 集合内元素无序 集合内元素不重复
se = {1, 2, 3} 定义一个集合
se = set() --- 定义一个空集合
取交集--- &   intersection()
取并集--- |   union()
取差集--- - （注意先后顺序）  defference()
取对称差集 去掉共有部分--- ^   symmetric_defference()
父子集--- >  issuperset()   issubset()
去重---set(去重对象)  可以是字符串 列表(列表内不能存在可变类型) 无法保证原顺序
len()--- 长度 
in--- 判断存在
discard()  如果存在则删除 不存在pass
remove()  存在则删除 不存在报错
difference_update()  比较完并赋值给原集合
isdisjoint()  无交集返回True
update()
pop()
add()
'''
```

### 字符编码

```python
'''
由字符转换成内存中的unicode，以及由unicode转换成其他编码的过程，都称为编码encode
由内存中的unicode转换成字符，以及由其他编码转换成unicode的过程，都称为解码decode
utf-8（全称Unicode Transformation Format，即unicode的转换格式）
'''
```

### 函数

````python
函数调用的三种方式
#1、语句形式：
foo()
#2、表达式形式：
m=my_min(1,2) #将调用函数的返回值赋值给x
n=10*my_min(1,2) #将调用函数的返回值乘以10的结果赋值给n
#3、函数调用作为参数的形式：
# my_min（2，3）作为函数my_min的第二个参数，实现了取1,2,3中的较小者赋值给m
m=my_min(1，my_min（2，3）)
````

### 装饰器

```python
'''
开放封闭原则
开放---对拓展功能是开放的
封闭---对源代码是封闭的

将原函数名指向的内存地址 转换为了 装饰器函数wapper的内存地址
'''
def outer(func):
    def wapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wapper

# 调用方式采用语法糖
@outer
def index():
	...

warps的作用是将原函数的属性 转递给wapper装饰器函数
from functools import warps
def outer(func):
	@warps(func)
    def wapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wapper

# 有参装饰器
from functools import warps
def outer(x, y, z ...):
    def inner(func):
        @warps(func)
        def wapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wapper
    return outer

'''
叠加多个装饰器
加载顺序 自下而上 
执行顺序 自上而下
'''
@deco3
@deco2
@deco1
def index():
```

### 迭代器

```python
'''
调用可迭代对象下的__iter__()方法 可以得到一个迭代器对象
每次调用这个迭代器对象的__next__()方法可以取到一个值
可迭代对象：内置有 __iter__()方法
迭代器对象：内置有 __iter__()  __next__()方法
可迭代对象：字符串 列表 字典 集合 文件对象
迭代器对象：文件对象

总结：
优点：可以统一有序无序的对象  节省内存空间
缺点：只能依次取 不能按索引取  具有生命周期 取完即结束
'''
```

### 生成器（generator）

```python
'''
自定义迭代器
yield --- 返回值，返回后不会结束 而是挂起函数
函数体内部 出现yield 调用该函数并不会执行代码，通过__next__() 调用则开始执行
'''
def func(start, stop, step=1):
    while start < stop:
        yield start
        start += stop

def func(name):
    print(name)
    while True:
        x = yield None
        ptint(name)

send()  # 为yield传递值
```

### 三元表达式

```python
条件表达式 ---  x if x > y else y   条件成立返回的值 if 条件 else 条件不成立返回的值
```

### 列表生成式

```python
new_list = [x for x in old_list if 条件]  new_list = [x for x in old_list]
```

### 字典生成式

```python
{k:v for k,v in items}
```

### 函数的递归调用

```python
'''
递归的本质就是循环

递归不应该无限制的调用下去 必须在满足某种条件下结束递归调用

回溯：一层层调用
递推：满足某种条件结束，然后一层层结束
'''
递归的应用
 l = [1,[2,[3,[4,[5,[6,[7,[8]]]]]]]]
 
def func(lis):
    for x in lis:
        if type(x) is list:
            func(x)
        else:
            print(x)
func(l)
```

### 编程思想/范式

```python
'''
面向过程的编程思想
'''
# 按步骤进行编程 写流水线 -- 问题流程化 进而简单化 但是 可拓展性差

# 应用场景
'''
编写脚本
数据分析
'''
```

### 函数式编程

```python
'''
匿名函数 与 lambda
'''
# 匿名函数：
# 定义函数：
lambda x,y: x+y
# 调用函数：
方式一
res = (lambda x,y: x+y)(1,2)
方式二
func = lambda x,y: x+y
func()
'''以上俩种方式 均不用'''
临时调用一次的场景

---------------------------------------------------------
map() --- 将可迭代对象中的值传递给函数
map(func, 可迭代对象) 返回值是一个生成器
filter() --- 将可迭代对象中的值传递给函数
max()
min()
sorted()
reduce() 将多个值合并到一起

```

### 模块

```python
'''
模块
1. 内置模块
2. 第三方模块
3. 自定义模块

一个.py文件本身 就是一个模块
具有__init__.py的文件夹（这个文件夹被称为包） 也是一个模块
'''
```

### 面向对象的编程思想

```python
'''对象就是将数据和功能封装在一起的容器'''
# 对象是具体的 类是抽象的
# 类
class MyClass:
	def __init__(self):  # 对象一旦创建 __init__()方法会将对象作为参数传递给self参数
        ...              # __init__() 内可以存放其他任意代码的 在对象创建时立即执行
        				# __init__() 只能返回None 默认返回None
      
   	def method(self):
        pass
# 对象
my_obj = MyClass()  # 实例化
my_obj.method()


```



```

```

### 一切皆对象

```python
type继承了object
type是object的类
type也是自己的类
```

### 魔法方法

```python
__init__()：类实例化会触发
__str__()：答应对象会触发
__call__(): 对象加（）会触发
__new__():在类实例化会触发，比__init__早触发
__del__():对象回收时触发
__setattr__(), __getaattr__(): 拦截方法  对象.属性 赋值调用set 取值调用get
__getitem__(): __setitem__() 
__repr__():交互式环境下打印对象
__enter__() 和 __next__() 

```



