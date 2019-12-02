#coding:utf-8
l = 0
c = 0
m = 12*12
while c<m:
	l += 180*(1.015**(m-c))
	c += 1
n = 16000*1.13**20
print(int(l),int(n),m/12,"年",enconding="utf-8")