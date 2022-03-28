#Task1
#hackerrank Write a function

a=int(input("Enter the year : "))
if a%4==0:
    print(a,"Leap year:")
else:
    print(a,"not leap year:")

#Task2
#hackerrank Python If-else

a=int(input("Enter the number : "))
if a%2 == 1:
   print('Weird')
elif a>=2 and a<=5:
    print('Not Weird')
elif a>=6 and a<=20:
    print('Weird')
elif a>20:
    print('Not Weird')

#Task3
#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

a=int(input("Enter the number : "))
if a%3 == 0 and a%5 == 0:
   print('Fizzbuzz')
elif a%5 == 0:
    print('buzz')
elif a%3 == 0:
    print('Fizz')
else:
    print('Invalid number')

#TASK4
#Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark
#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL

mark1=int(input("Enter the mark1 : "))

if mark1 > 0 and mark1 < 100:
    print("valid mark")
    if mark1 > 90 and mark1 < 100:
        print("GradeA")
        elif mark1 > 80 and mark1 < 89:
        print("GradeB")
        elif mark1 > 70 and mark1 < 79:
        print("GradeC")
        elif mark1 > 60 and mark1 < 69:
        print("GradeD")
        elif mark1 > 50 and mark1 < 59:
        print("GradeE")    
else:
    print("Fail")
