import os
#os.chdir()
def git_push():
    os.system("git add -A")
    str = input("输入上传信息：")
    os.system("git commit -m"+str)
    os.system("git push")
def git_pull():
    os.system("git pull")
def git_status():
    os.system("git status")

while 1:
    list = [("上传",git_push),("下载",git_pull),("状态",git_status),("退出",exit)]
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
