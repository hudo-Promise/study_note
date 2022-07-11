st#### git 使用手册

* 查看当前仓库信息  git remote -v

* 设置新的仓库地址 git remote set-url origin git@192.168.30.29:chenwei/em-data.com.cn.git

* 1、切换远程仓库地址：
  方式一：修改远程仓库地址

  【git remote set-url origin URL】 更换远程仓库地址，URL为新地址。

  方式二：先删除远程仓库地址，然后再添加

  【git remote rm origin】 删除现有远程仓库
  【git remote add origin url】添加新远程仓库

* 查看当前分支信息  git remote show origin

* git 提交流程

  * 第一种方法：（简单易懂）

    1、git add .（后面有一个点，意思是将你本地所有修改了的文件添加到暂存区）

    2、git commit -m""(引号里面是你的介绍，就是你的这次的提交是什么内容，便于你以后查看，这个是将索引的当前内容与描述更改的用户和日志消息一起存储在新的提交中)

    3、git pull origin 远程分支名  这是下拉代码，将远程最新的代码先跟你本地的代码合并一下，如果确定远程没有更新，可以不用这个，最好是每次都执行以下，完成之后打开代码查看有没有冲突，并解决，如果有冲突解决完成以后再次执行1跟2的操作

    4、git push origin master（git push origin 本地分支名:refs/remotes/远程分支名） 将代码推至远程就可以了

  * 第二种方法：

    1、git stash （这是将本地代码回滚值至上一次提交的时候，就是没有你新改的代码）

    2、git pull origin 远程分支名（将远程的拉下来）

    3、git stash pop（将第一步回滚的代码释放出来，相等于将你修改的代码与下拉的代码合并）

    然后解决冲突，你本地的代码将会是最新的代码

    4、git add .

    5、git commit -m ""

    6、git push origin master（git push origin 本地分支名:refs/remotes/远程分支名）

    这几步将代码推至了远程

    最后再git pull origin 远程分支名一下，确保远程的全部拉下来，有的你刚提交完有人又提交了，你再拉一下会避免比的不是最新的问题 

* 清除缓存命令
  * git rm -rf --cache s

* 分支命令
  * git checkout -b branch_name  创建分支
  * git checkout branch_name  切换分支
  * git branch -a (-r) 查看分支


### Git的使用

```python
#1 协同开发 版本管理
# svn集中式管理 git分布式管理
# git装完既有客户端 又有服务端
'''
工作区：
暂存区：
版本库：

远程仓库：github 码云 公司内部库
'''
# 1.安装git客户端
# 2. 使用git bash here
# 3. git init 文件夹名 ---初始化一个文件夹
# 4. cd 到这个文件夹
# 5. git status ---查看当前文件夹下文件状态  --红色表示未被管理 --绿色表示提交到暂存区
# 6. git add   ---提交文件到暂存区
# 7. git commit -m '注释内容' --提交文件到本版库
# 8. git checkout --回滚
# 9. git log --查看版本管理
# 10. git reset --hard 版本号
# 11. git config --global user.email "12345@qq.com"  --添加作者信息
# 12. git config --global user.email "12345"  --添加作者信息
# 13. git config user.email "12345@qq.com"
# 14. git config user.email "12345"
# 15. 在.git同级目录下创建.gitignore文件 在其中配置不需要被管理的文件夹/文件
		#在windows下创建此文件 需要 .gitignore.
	# 文件夹/文件名字 表示文件夹/文件被忽略
    # # --是注释 
    # / --表示当路径
    # * --通配符
 --------
'''分支操作'''
# 1. git branch  ---查看所有分支
# 2. git branch dev  ---创建分支
# 3. git branch -d dev  ---删除分支
# 4. git checkout dev  ---切换分支
# 5. git merge 分支名  ---合并分支  将dev合并至master 需要先切换至master 再合并

```
