import os

def git_push():
    os.system("git add -A")
    str = input("输入上传信息：")
    os.system("git commit -m"+str)
    os.system("git push")
def git_pull():
    os.system("git pull")
def git_exit():
    exit()
while 1:
    list = [("上传","git_push"),("下载","git_pull"),("退出","git_exit")]
    print("------------  git  -------------")
    for i,j in enumerate(list,1):
        print(i,j[0])
    choise = input("请选择>>>").strip()
    if choise.isdigit():
        choise = int(choise) - 1
        if choise <= len(list)+1:
            locals()[list[choise][1]]()
    else:
        print("类型错误")