#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

dict1={}
print(dict1)

dict2={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dict2)

print(dict2[""bobtn""])
Traceback (most recent call last):
  File ""<pyshell#2>"", line 1, in <module>
    print(dict[""bobtn""])
KeyError: 'bobtn'

print(dict2[""arbeg""])
Traceback (most recent call last):
  File ""<pyshell#3>"", line 1, in <module>
    print(dict2[""arbeg""])
KeyError: 'arbeg'


print(dict2.keys())
#dict_keys([1, 2, 3])
tp=tuple(dict2.items())
print(type(tp))

p2=(dict2[2])
p3=sum(p2)/len(p2)
print(p3)
