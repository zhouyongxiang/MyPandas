import os
os.chdir("H:\zyx")

def git_push():
    os.system("git add -A")
    str = input("输入上传信息：")
    os.system("git commit -m"+str)
    os.system("git push")
def git_pull():
    os.system("git pull")
def my_python():
    p = ["python","jupyter","exit"]
    
    while 1:
        for i,j in enumerate(p,1):
            print(i,j)
        my_p = input("请选择>>>").strip()
        if my_p.isdigit() and my_p in ["1","2","3"]:
            my_p = int(my_p)
            if my_p == 1:
                os.system("ipython")
            if my_p == 2:
                os.system("jupyter lab")
            if my_p ==3:
                break
        else:
            print("输入错误")
def git_bash():
	while 1:
		print("输入2退出")
		str = input("git指令>>>")
		if str != "2":
			os.system(str)
		else:
			break
def git_status():
    os.system("git status")

while 1:
    list = [("上传",git_push),("下载",git_pull),("状态",git_status),("bash",git_bash),("python",my_python),("退出",exit)]
    print("------------  git  -------------")
    for i,j in enumerate(list,1):
        print(i,j[0])
    choise = input("请选择>>>").strip()
    if choise.isdigit():
        choise = int(choise) - 1
        if choise < len(list) and choise>=0:
            list[choise][1]()
        else:
            print("没有此菜单")
    else:
        print("类型错误")
