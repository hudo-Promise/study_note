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

