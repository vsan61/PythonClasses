#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2"

s1=set()
s2=set()
print(s1)
print(type(s1))
print(type(s2))

s1={7,8,9,1,2,3,4,5,0}
s2={4,5,6,0}
s1.update(s1)
print(s1)
s2.update(s2)
print(s2)

print(set1.issubset(set2))
False

s1.remove(8)
print(s1)

s2.remove(8)
print(s2)
#Traceback (most recent call last):
 # File "F:/Python/Docs/Set_tasks.py", line 26, in <module>
  #  s2.remove(8)
#KeyError: 8

s1.discard(0)
print(s1)

s2.discard(0)
print(s2)

s3=s1.intersection(s2)
print(s3)

  
