#check if a no is postive or not
"""
a=90
if a>0: print(" number is postive")
"""
#check no is even or odd
"""
a=int(input("enter the no:"))
print("even no") if a%2==0 else print("odd no")
"""
#wap area calculator
#area of circle
"""
print("----- AREA CALCULATOR--------")
print("""  1.circle 2.rectangle 3.square 4.Triangle """)
choice=int( input("choose 1---4:"))
if choice==1:
      r=float(input("enter the radius:"))
      print("Area of circle=",r*3.14*3.14)
elif choice==2:
    lenth=int( input("Enter the length of Rectangle:"))
    width=int( input("Enter the width of Rectangle:"))
    print(" Area of Rectangle =",lenth*width)

elif choice==3:
    side=int( input("Enter the  side of Square:"))
    print(" Area of Square =",side**2)

elif choice==4:
    height=int( input("Enter the Height of Triangle:"))
    width=int( input("Enter the width of Triangle:"))
    print(" Area of triangle =",(height*width)/2)
else:
    print("Invalid Choice")
    """



#wap to check vowel or not
"""
letter=input("enter a letter:")
if letter in "aeiou": print("vowel")
else: print(" not a vowel")
"""
  
               
