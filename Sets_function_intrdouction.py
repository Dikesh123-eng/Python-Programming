#Sets Introduction
"""
a={3,6,7,3,8,9,4,8,9,2,3,4,5,6,7,}
print(a)
#Iteration
for i in a:
    print(i)
    """
#Sets Function
#Add()->To insert some elemnt in The sets
"""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
print("before Adding  Mahesh sets will be:",a)
a.add("Mahesh")
print("Afte rAdding Mahesh sets will be:",a)
"""
#pop()->To Remove Random value/elemnt from sets
"""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
a.pop()
print(a)
"""
#Remove()-> To Remove Specific Values/ement
'''
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
a.remove("Shyam")
print(a)
'''
#Discard()->It is similar to remove
'''
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
a.discard("Ravi")
print(a)
'''
#copy()->it is used to copy to another sets
"""""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
b=a.copy()
print(b)
"""""
#isdisjoint()->return true /false sets a elemnt present in sets b or not
""""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
b={"Dikesh","Ravi","radhe","Hulk","Shyam"}
c={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
d={"dikesh","ravi","dinesh","hulk","Naresh"}
print(a.isdisjoint(d))
"""
#issubset()->sets A Ka Sabhi Elemnt Set B me Present Hoga to True Dega Warna false Dega
""""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
b={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
c={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
d={"dikesh","ravi","dinesh","hulk","Naresh"}
print(a.issubset(b))
"""
#issuperset()->Sets A Ka Sabhi Elemnt Set B me Present Hoga to True Dega Warna false Dega
""""
a={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
b={"Dikesh","Ravi","Dinesh","Hulk","Shyam"}
c={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
d={"dikesh","ravi","dinesh","hulk","Naresh"}
print(a.issuperset(b))
"""
#update()->Sets A Aur Sets B me so similar hoga usse bs ek bar likhega
"""
c={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
d={"Dikesh","Ravi","dinesh","hulk","Naresh"}
x=c.update(d)
print(x)
"""
#clear()->clear all sets Elemnt
"""
c={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
d={"dikesh","ravi","dinesh","hulk","Naresh"}
c.clear()
print(c)
"""
#union()->Jo dono sets me  Common Hoga oh Bs Ek Bar dega  Baki DOno sets ko add krke ek sath dega
"""
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.union(b))
"""
#Differnce()->Jo done sets me similar hoga usse chhodker baki dono sets ko present karega
"""
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.difference(b))
"""
#Differnce update()->Similar to differnce bs ek usmi sets me return kr dega
"""

a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.difference_update(b))
"""
#Intersection()->Jo dono sets me coomon Hoga oh Output dega
"""
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.intersection(b))
"""
#Intersection-update()->Jo dono sets me common Hoga oh Output dega same sets me
"""
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.intersection_update(b))
"""
#symmetric _Differnece()->jo same hoga use chodkar print krega
"""
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.symmetric_difference(b))
"""
#symmetric _Differnece()->jo same hoga use chodkar print krega bs same string me
a={"Dikesh","Ravi","kartik","RAVAN","Shyam"}
b={"Dikesh","Ravi","dinesh","hulk","Naresh"}
print(a.symmetric_difference_update(b))





