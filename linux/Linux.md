### Linux

```python
# linux操作命令

'''远程连接'''
ssh user@ip

'''linux语法格式'''
命令 + 一个或多个空格 + 参数 + 空格 + 文件/文件夹（可写可不写）

''''''
whoami  # 显示当前用户
hostname  # 显示当前主机名
pwd  # 显示当前工作目录的绝对路径
cat  # 查看文件
logout  # 退出
su - 用户名  # 用户切换
```

### cd

```python
cd  # 变换目录
.  # 当前的工作目录
..  # 上一级的工作目录
-  # 上一次的工作目录
~  # 当前系统的用户家目录
```

### ls

```python
ls 可选参数 可选的文件夹对象
参数 
-a  # 显示所有的文件（包括隐藏文件）
-l  # 详细输出文件信息
-h  # 输出文件大小
--full--time  # 显示文件修改时间 
ls -alh --full-time a.txt
-t  # 根据时间修改排序
-f  # 在不同的文件结尾 输出不同的特殊符号
-d  # 显示文件夹本身 不输出文件夹内的信息
-r  # 反转排序
-S  # 大写的S正对文件夹大小进行排序 默认从大到小
-i  # 显示文件的inode信息
```

### mkdir

```python
mkdir 123  # 创建一个文件夹
mkdir {,,,,}  # 同一目录下创建多个文件夹
mkdir -p /1/2/3/4  # 递归创建文件夹
mkdir wenjianjia{1..100}  # 创建100个文件夹
```

### touch

```python
touch # 通过touch创建的文件为普通文件 没有则创建 有则查看
touch abc{1..100} # 创建100个文件

```

### cp

```python
cp 源文件 目标文件 目录 # 省略目录则复制到当前文件夹 省略目标文件则创建同名文件
cp 源文件 目录/目标文件 
-r # 递归复制目录 ---复制文件夹
-d # 复制保持软链接
-a # 相当于-pdr
-p # 复制保持源文件的权限 属性
-i，--interactive # 覆盖前询问提示

```

### mv

```python
mv 源文件 目标文件夹 # 移动 *通配符
mv 旧文件名 新文件名 # 重命名

```

### rm

```python
rm 文件名 #  删除普通文件
-f # 强制删除
-i # 删除前确认
-r # 删除超过三个文件或者递归删除前确认
-d. --dir # 删除空目录
-r, -R , --recursive # 递归删除目录及内容
-v, --verbose # 详细显示进行步骤
    -- help   # 显示帮助信息并退出
    --version # 显示版本信息并退出
```

### 帮助命令

```python
man 命令 # 
命令 --help
info 命令 # 获取帮助
```

### 开关机命令

```python
shutdown -h now # 立即关机 企业用法
shutdown -h 1 # 1分钟后关机 也可以写具体时间
halt # 立即关闭系统 需要手动切断电源
init 0 # 切换运行级别为0 0表示关机
poweroff # 立即关闭系统 且关闭电源
reboot # 重启
shutdown -r now # 立即重启 企业用法
shutdown -r 1 # 1分钟后重启 也可以写具体时间
init 6 # 切换运行级别为6 6表示重启
logout # 注销退出当前用户
exit   # 注销退出当前用户 快捷键ctrl + d

```

### 快捷操作

```python
ctrl + c # 取消当前操作
ctrl + l # 清空屏幕内容
ctrl + d # 退出当前用户
ctrl + a # 光标移动至行首
ctrl + e # 光标移动至行尾
ctrl + u # 删除光标到行首的内容
```

### 环境变量

```python
echo $path
```

### vim

```python
yum install vim -y # 通过yum软件管理工具 安装vim
vim 文件名 # 不存在则创建
i # 输入模式
a
o
： # 底线命令模式
:wq! # 写入并退出 !强制性的 
:q!  # 不保存 直接退出
'''快捷键'''
h # 向左
j # 向下
k # 向上
i # 向右
w # 移动到下一个单词
b # 移动上一个单词
0 # 移动至行首
$ # 移动至行尾
g # 移动至文章首
G # 移动至文章尾
H # 移动至屏幕开头
L # 移动至屏幕结尾
M # 移动至屏幕中间
/ # 向下查找
？# 向上查找
yy # 复制光标所在行
4yy # 复制4行
p # 打印复制内容
dd # 删除光标当前行
999 dd # 删除光标当前位置到行尾的内容
x # 删除光标当前字符 向后删除
X # 删除光标当前字符 向前删除
u # 撤销
C # 删除光标所在位置到行尾的内容 且进入编辑模式
o # 在当前光标的下一行开始编辑
O # 在光标的上一行开始编辑
A # 快速进入行尾 且进入编辑模式
zz # 快速保存退出
-------------------
wc [option] file # 统计数字相关信息
sort [option] file # 对文件中的数据进行排序
uniq [option] file # 检查文件中重复的行列
head # 获取前N条数据

grep # 
sed # 批量操作文件
awk # 
'''批量快捷操作'''
ctrl + v # 进入可视块模式
用上下左右 选择你操作的块
选中块 输入d 删除块内容
选中块后 输入I 进行写代码
按下esc俩次 自动生成多行代码
```





### linux文件夹

```python
/dev  # 存放抽象硬件
/lib  # 存放系统库文件
/sbin  # 存放特权级二进制文件
/var  # 存放经常变化的文件
/home  # 普通用户目录
/etc  # 存放配置文件目录
/boot  #存放内核与启动文件
/bin  # 存放二进制文件
/usr  # 存放安装程序
/mnt  # 文件挂载目录
/root  # 特权用户目录
/opt  # 大型软件存放目录
```

### shell

```python
#!/bin/bash

# 添加执行权限
```

### 配置

```python
# 设置静态IP
etc/sysconfig./network-scripts/ifcfg-ens33
IPADDR  -- 本地ip 最后一位 3-254
GATEWAY  -- NAT-网关IP
DNS1 -- 同GATEWAY
service network restart 重启网卡
# hostname设置
hostname 主机名--临时
vi .etc/hostname   修改文件内容 保存退出--永久
# 关闭防火墙配置
systemctl stop firewalld --临时
systemctl disable firewalld --永久
```

