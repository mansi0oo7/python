from tkinter import NONE
#a='mansi'
#a="mansi"
'''(start with underscore variable)'''
_a = '''mansi
hello
welcome
nmc
hi '''
b1 = 345
c = 45.32
d = True 
f= False
g=NONE 
#printing the variable(aam krvathi a,b,c,d,f.. ni value print krse  like :- b=345, c = 45.32)
print(_a)
print(b1)#(can not start with digit ..like - 1b . u can use digit after using alphabet..like - b1)
print(c)
print(d)
print(f)
#printing the type of variable # (aam krvvathi a,b,c,d,f..ni datatype print krse like:- a=<class 'str'>)
print(type(_a))
print(type(b1))
print(type(c))
print(type(d))
print(type(f))
print(type(g))
#*************oprator******************
a=3
b=4
#arithmetic oprator
print("the value of 3+4=",3+4)
print("the value of 3-4=",3-4)
print("the value of 3*4=",3*4)
print("the value of 3/4=",3/4)
#assignment oprator
a=34
a+=2
print(a)
b=6
a-=4
print(b)
# comparison oprator ..... a comparison oprator is return a boolean ..
b=(4!=5) #4 not equle to 5
#b=(4>5)
#b=(4<5)
#b=(4>=5)
#b=(4<=5)
#b=(4==5)
print(b)
#logical operators