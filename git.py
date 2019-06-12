import os

class My_git:
	def	__init__(self):
		self.start
	def git_push(self):
		os.system("git add -A")
		str = input("输入上传信息：")
		os.system("git commit -m"+str)
		os.system("git push")
	def git_pull(self):
		os.system("git pull")
	def start(self):
		list = [{"上传":self.git_push},{"下载":self.git_pull},{"退出":exit}]
		while 1:
			for i,j in enumerate(list,1):
				print(i,j.keys)
			chose= input("请选择>>>")
			getattr(list(int(chose)-1))

g = My_git()