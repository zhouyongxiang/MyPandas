import os
os.system("git add -A")
str = input("输入上传信息")
os.system("git commit -m"+str)
os.system("git push")