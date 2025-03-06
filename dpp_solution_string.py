# dpp solution-3
"""

a="why fit in,when you are born to stand out!"
#length of the string
print("length of string  is:",len(a))
#for occuring of alphabet o in string
a="why fit in,when you are born to stand out!"
print(a.count("o"))
#for lower cases
a="why fit in,when you are born to stand out!"
print(a.lower())
print(a.upper())
#is title
a="why fit in,when you are born to stand out!"
print(a.istitle())
#for index
a="why fit in,when you are born to stand out!"
print(a.index("fit in"))
"""
#dpp solution- 4
"""
A="OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(A.split("."))
#sort alphabetically
a="hello"
print(sorted(a))
#remove char from string
a="hello F.R.I.E.N.D"
print(a.replace("F.R.I.E.N.D"," "))
# replace dot from string
A="OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(A.replace(".",""))
# no of ocuuring substring in any string
a="dikesh is a very very dangeroues and very clear mindset person"
print(a.count("very"))
"""

"""
#dpp solution ->5
a=input("Enter here somthing:")
print(a[::-1])
# string contains only digits or not
b=input("enter here somthing:")
c=a.isdigit()
if c== True:
    print("it's contains only digites")
else:
         print("it's  not contains only digites:")
         # check srting is palindrome or not
         a=input("enter here somthing")
         b=a[::-1]
         if a==b:
          print(" it is palindrome")
         else:
            print("it is not a palindrome")
            #find no of vowels in a string
            a=input("enter something here:")
            count =0
            for i in a:
                if i=="a" or i=="e" or i=="i" or i=="u" or i=="o" or  i=="A" or i=="E" or i=="I" or i=="U" or i=="O":
                    count=count+1
                print("count of vowels is=",count) 
                
                #check in words in string begins capitals letter
a=input("enter here somthing")
print(a.istitle())
"""
                




