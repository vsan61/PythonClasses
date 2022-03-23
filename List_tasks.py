#Create an empty list (two ways)
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple

list1=[]
print(list1)

list2=[5,6,7,8]
print(list1+list2)

list2.append(8)
list2.append(9)
list2.append(1)
list2.append(5)
list2.append(6)
list2.append(7)
list2.append(8)
list2.append(1)
print(list2)


print(list2.count(8))

mean=sum(list2)/len(list2)
print(mean)

print(sum(list2))
print(max(list2))
print(min(list2))

list2.sort()
median=len(list2)//2
print(list2[median])

print(list(set(list2)))



