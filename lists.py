#lists in Python
"""
a=["dikesh","shivam","suresh","dinesh"]
print(a)
b=[2,5,6,8,9,3.7]
print(b)
#slicing in lists
print(a[2])
print(a[-1])
print(b[1:5])
print(a[::3])
print(b[1:6])
"""
#Iteration in list
"""
a=["dikesh","shivam","suresh","dinesh"]
b=[2,5,6,8,9,3.7]
#for loop
for i in range (len(a)):
    print(a[i])

for i in range (len(b)):
      print(b[i])

      # while loop
      i=0
      while i<(len(a)):
           print(a[i])
           i=i+1
            #using short hand for loop

[print(i) for i in a]
"""
#lists function
#calculate lenth of lists
"""
a=["dikesh","shivam","suresh","dinesh"]
print(len(a))
#count ocuurance of elemnt in the lists
a=["dikesh","shivam","suresh","dinesh","dikesh"]
print(a.count("dikesh"))
#To add element of list
a=["dikesh","shivam","suresh","dinesh"]
a.append("naina")
print(a)
# To Add elemnt in Specfic Location
a=["dikesh","shivam","suresh","dinesh"]
a.insert(2,"shyam")
print(a)
#To Remove Elemnt from list
a=["dikesh","shivam","suresh","dinesh"]
a.remove("shivam")
print(a)
# To Remove a elemnt from a certain location in list
a=["dikesh","shivam","suresh","dinesh"]
print(a.pop(3))
print(a)
"""
#function of String
"""
#To create a copy of a List
a=["dikesh","shivam","suresh","dinesh"]
print(a)
b=a.copy()
print(b)
#To Access an Elemnt
a=["dikesh","shivam","suresh","dinesh"]
print(a.index("dikesh"))
# To Extend The List
a=["dikesh","shivam","suresh","dinesh"]
c=["Mayank","Sahil"]
a.extend(c)
print(a)
# To Reverse The List
a=["dikesh","shivam","suresh","dinesh"]
a.reverse()
print(a)
# To sort The LIst
a=["dikesh","shivam","suresh","dinesh"]
a.sort()
print(a)
b=[5,9,3,7,9,4,0,2,7,8]
b.sort()
print(b)
# To Clear the data from List
b.clear()
print(b)
a.clear()
print(a)
"""
#Lists Comprehersion
""""
l1=[4,8,9,3,56,78,90,34,56,78,90,]
l3=[i for i in l1] 
print(l3)
l3=[i for i in l1 if i>50] 
print(l3)
"""




