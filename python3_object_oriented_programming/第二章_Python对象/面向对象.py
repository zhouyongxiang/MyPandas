'''
1、创建一个类	
'''
# class MyFirstClass:
#     pass
'''
2、添加属性
   a、类可直接添加属性赋值	
'''
# class Point:
#     pass
# p1 = Point()
# p1.x = 5
# p1.y = 4
# print(p1.x, p1.y)

'''
3、对象的初始化
	a、__init__的对象，全部共用且可修改
'''
# class Point:
#     def __init__(self, x=0, y=0):
#         self.move(x, y)
#     def reset(self):
#         self.x = 0
#         self.y = 0
#     def move(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(3, 5)
# print(p.x, p.y)
# p.reset()
# print(p.x,p.y)
'''
4、组织模块
'''
# class UsefulClass:
#     pass
# def main():
#     useful = UsefulClass()
#     print(useful,123)
# if __name__ == "__main__":
#     main()
'''
5、数据访问
'''
# class SecretString:
#     """
#     一个不安全的方法
#     """
#     def __init__(self, plain_string, pass_phrase):
#         self.__plain_string = plain_string
#         self.__pass_phrase = pass_phrase

#     def decrypt(self, pass_phrase):
#         if pass_phrase == self.__pass_phrase:
#             return self.__plain_string
#         else:
#             return ""


# secret_string = SecretString("ACME", "password")
# print(secret_string.decrypt("password"))
# # print(secret_string.__plain_string) # 报错
# print(secret_string._SecretString__plain_string)
