a="Dikesh is a good boy so day by day glow his beauty"
"""
print(a)
#for length calculation
print(len(a))
#for no of ocerrance letter in string
print(a.count("e"))
print("occurance of b=",a.count("b"))
#convert srting upper case
print(a.upper())
#convert string lower case
print(a.lower())
#convrt string capitalize
print(a.capitalize())
#find  index of occurance in string
print(a.find("o"))
#format of string
print(a.format(a))
#center of string
print(a.center(50,"*"))
#case fold string  convert similiar to lower case
print(a.casefold())
#format a string
name="Dikesh"
age=19
b="my Name is {}.and my age is{}"
print(b.format(name,age))
#center 
name="Dikesh"
print(name.center(20,"!"))
"""

""""
#for isalnum
a="Dikeshkumar"
print(a.isalnum())
#for isalpha
a="dikesh"
print(a.isalpha())
#for is decimal
a="123"
print(a.isdecimal())
#for digit
a="123456"
print(a.isdigit())
#for islower
a="dikesh"
b="Dikesh"
print(a.islower())
print(b.islower())
#for is upper
a="DIKESH"
b="dikesh"
print(a.isupper())
print(b.isupper())
# for is space
c="dikesh kumar"
print(c.isspace())
#for is titile
a="Harry Potter And the Potter"
print(a.istitle())
"""
"""

#endwith()
a="Harry Potter"
print(a.endswith("r"))# tue
print(a.endswith("y"))# false
#startswith()
a="Harry Potter"
print(a.startswith("h"))#false
print(a.startswith("H"))# true
#swapcasea();
a="Harry Potter"
print(a.swapcase()) #hARRY pOTTER
#strip()
a="Harry Potter"
print(a.strip()) #Harry Potter
b="******harry potter"
print(b.strip("*")) #0/p=harry potter
# splict()
a="#dikesh #ramesh #suresh #dinesh"
print(a.split("#"))
b="naya.laya.paya"
print(b.split("."))
# Lust()
a="harry potter"
x=a.ljust(20)
print(x,"is my favourite movie")# harry potter       is my fav movie
b="harry potter"
x=b.ljust(20,"*")
print(x,"is my favourite movie") # harry potter ********* is my fav movie

#rjust
a="harry potter"
x=a.rjust(20)
print(x,"is my favourite movie")#          harry potter is my fav movie
b="harry potter"
x=b.rjust(20,"*")
print(x,"is my favourite movie") # *********harry potter is my fav movie
# replace
a="My name is dikesh"
print(a.replace("dikesh","rudra")) # my nmae is  rudra
print(a.replace("dikesh","mahesh")) # my name is mahesh
#rindex
a="dikesh is a gooder boy"
print(a.rindex("gooder")) # 12
#rfind()

a="dikesh is a gooder boy"
print(a.rfind("gooder")) #12

"""
#slicing in string
a="Harry Potter and the Goblet of fire"
print(a[0:5]) #Harry
print(a[:12]) #Harry potter
print(a[:7:3]) #hrp
b="0123456789"
print(b[::3]) #0369










