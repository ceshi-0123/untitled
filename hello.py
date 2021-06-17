 # coding=utf-8
#!/usr/bin/python

"""
if True:
    print ("Answer"),
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
raw_input("按下Enter键退出，其他任意键显示...\n")


x=5
print(x)
x='BILL'
print(x)
x = "awesome"
print("Python is " + x)



x="awesome"
print(type(x))
def myfunc():
    global x
    x="fantastic"


myfunc()
print("Phthon is "+x)


x=10
y=6.8
z=1+2j

a=str(z)
b=int(y)
c=float(x)

print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1,5))

a = "Hello, World!"
print(a[-8:-1])


a = "Hello, World!"
print(len(a))

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World, Hi!"
print(a.replace("Hello", "Kitty"))

a = "Hello, World, Hi!"
print(a.split(","))

txt = "China is a great country"
x = "ina" not in txt
print(x)

a = "Hello"
b = "World"
c = a +" "+ b
print(c)


age=11
txt= "My age is {}"
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#capitalize()：首字符转换为大写
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


txt = "63 is my age."

x = txt.capitalize()

print (x)


#casefold()：字符串转换为小写-使用后报错，改用lower()

txt = "Hello, And Welcome To My World!"

x = txt.lower()

print(x)


#center() :返回居中的字符串
#打印单词 "banana"，占用 20 个字符，并使 "banana" 居中
txt = "banana"

x = txt.center(10,"o")

print(x)

 #count():返回指定值在字符串中出现的次数。
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 7, 24)

print(x)

#encode():返回字符串的编码版本


txt = "My name is St氓le"

x = txt.encode()


print(x)

txt = "My name is St氓le"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
"""


