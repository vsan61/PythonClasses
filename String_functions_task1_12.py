#Task1
#identify the middle character of the string"
name = input("Please enter the name: ");
count = len(name)
middle = count//2
out=str(name[middle])
print(f"middle letter of name is {out}")


#Task2:string1 = ""***python***""
#string2 = "**python********"
#string  = "********java*******"

string1 = "***python***"
string2 = "**python********"
string3 = "********java*******"

print(string1.strip("*"))
print(string2.lstrip("*"))
print(string3.rstrip("*"))



#Task3: (name<space>float)
#collect three strings from user  name<space>float

string1= input("Enter first name : ") 
string2= input("Enter second name : ")
string3= input("Enter third name : ")

name1 = string1.split()
name2 = string2.split()
name3 = string3.split()

print(float(name1[1])+float(name2[1])+float(name3[1]))


#Task4:
#collect two strings from user
s1 = input("Enter 1st string : ")
Enter 1st string : python
s2 = input("Enter 2nd string : ")
Enter 2nd string : java
c1 = len(s1)
c2 = len(s2)
mid1 = c1//2 
mid2 = c2//2
result = s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid1]+s2[mid2]
print(result)


#Task5:
#Collect two strings from user
#string1: wikipedia
#string2: typescript
#output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
#(ord , chr)


string1 = input("Plz enter the 1st word: ")
Plz enter the 1st word: class
string2 = input("Plz enter the 2nd word: ")
Plz enter the 2nd word: completed
c1 = len(string1)
c2 = len(string2)
mid1 = c1//2
mid2 = c2//2
a = string1[mid1]
b = string2[mid2]
total = ord(a) + ord( b)
result = ""Ascii value of "" + a + "" - "" + str(ord(a)) + "" + "" + ""Ascii value of "" + b + "" - "" + str(ord(b))+ "" = "" + str(total)
print(result)


#Task6:
#collect one string from user:
#string: computer
#output: c6r

string1=input("Enter the string : ")
var1=string1[0]
var2=len(string1)
var3=string1[var2 -1]
print((var1+str(var2)+var3))


#Task7
#Say hello world with python

print("Hello, World!")

o/p - Hello, World!


#Task8:
#swapcase

string1=input("Enter the string : ")
print(string1.swapcase())


Task9
what;s your name

first_name = input("Enter the string : ")

second_name = input("Enter the string : ")

print(f" {first_name} {second_name} ")


#Task10:
#Mutation

string = input()
asdfghjl
string  = string[:3]+"G"+string[4:]
print(string)


#Task11:
#arithmtic Operator
a = input("Enter the number 1 : ")
b = input("Enter the number 2 : ")

sums = print(int(a)+int(b))
diffs = print(int(a)-int(b))
prods = print(int(a)*int(b))


#Task12:
#division
a = input("Enter the number 1 : ")
b = input("Enter the number 2 : ")

divs = print(int(a)/float(b))






