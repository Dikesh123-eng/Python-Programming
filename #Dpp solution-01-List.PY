#Dpp solution-01-List

# swap first and fouth elemnt
"""
A=["ROSE","RACHEL","MONICA","JOE"]
print(A)
A[0],A[3]=A[3],A[0]
print(A)
"""
#Add New Value in 2nd Position
"""
A=["ROSE","RACHEL","MONICA","JOE"]
print(A)
A.insert(2,"dikesh")
print("New DATA:",A)
"""
#delte a value from 3rd position
"""
A=["ROSE","RACHEL","MONICA","JOE"]
print(A.pop(3))
print(A)
"""
#mul f number given in list
"""
B=[13,7,12,10]
mul=1
for i in (B):
    mul=mul*i

    print(mul)
    """
#find largest number in the list
"""
B=[13,7,12,10]
B.sort()
print("The Highest no int this list :",B[-1])
"""
#find Smallest number in the list
"""
B=[13,7,12,10]
B.sort()
print("The smallest no in this list :",B[0])
"""

 