#Task1:

#Using Range function  print multiples of 5 from 0 to 75
#Using Range function  print multiples of 8 from 0 to 72

#Using Range function  print multiples of 5 from 75 to 0
#Using Range function  print multiples of 8 from 96 to 72

for a in range(0,75,5):
    print(a)

for b in range(0,72,8):
    print(b)

for c in range(-75,0,5):
    print(-c)

for d in range(-96,-72,8):
    print(-d)

#Task2:
#Get a dynamic list from user

a = []
b = int(input("Enter the elements in list: "))
for i in range(0, b):
    x = int(input("Enter the element:"))
    a.append(x)
    print(a)



#Task3:
#Get a dynamic dictionary from user
#clues Task2 and Task3
#1. get number of elements from user
#Loop through range
#append to list/dicti

c = {}
d = int(input("Enter the elements in list: "))
for i in range(0,d):
    k = int(input("Enter the key :"))
    v = (input("Enter the value:"))
    c[k] = v
    print(c)

	
#Task4:
#Get two integers from user
#print multiples of 8 between them
#add in to list

a=int(input("enter an integer  "))
b=int(input("enter another integer  "))
c=[]
for i in range(a,b):
    if i%8==0:
        c.append(i)
        print(c)


#Task5:
#Input:
#Li1 = [3,4,5,2,7,8,9,10]
#Output:
#Li_odd = [3,5,7,9]
#Li_even = [4,2,8,10]

Li1 = [3,4,5,2,7,8,9,10]
Li_even =[]
Li_odd=[]
for i in Li1:
    if(i%2==0):
        Li_even.append(i)
        print(Li_even)
    elif(i%2==1):
        Li_odd.append(i)
        print(Li_odd)


#Task 6
#Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]  
#Output:
#neg_LI = [-1,-7,-3]
#pos_LI = []
#Zeros = []

Li=[-1, -7,8,10,20,21,17,28,-3,0,0,]
neg_LI =[]
pos_LI = []
Zeros = []
for i in Li:
    if(i < 0):
        neg_LI.append(i)
        print(neg_LI)
    elif(i > 0):
        pos_LI.append(i)
        print(pos_LI)
    else:
        Zeros.append(i)
        print(Zeros)


#Task7:
#Study range function and for loop properly

print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))

[0, 1, 2, 3, 4]
[1, 2, 3, 4]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[-5, -2, 1, 4]
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[10, 8, 6, 4, 2]
