#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

v1=(1,4,5,6,7,8)
v2=(5,6,7,8,9)
print(v1)
print(v2)

print (set(v1+v2))

v3=(v1+v2)
print(v3.index(9))

print(v3*3)





