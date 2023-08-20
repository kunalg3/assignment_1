#ans 1
a="Hello"#Ans  (i) string 
print(a)
alist=["banana","apple","mango"]#ans (ii) list
print(alist)
b=14.19#ans (iii) float
print(b)
var=("maths","english","science")#ans (iv) tuple
print(var)

#ans 2
var1=''
print(type(var1))#ans i
var2='[ DS , ML , Python]'
print(type(var2))# ans ii
var3 = [ 'DS' , 'ML' , 'Python' ]
print(var3)#ans iii
var4 = 1.
print(type(var4))#ans iv

#ans 3
#(i) / division operator is used for division purpose 
c=9/3 # a will hold the value 3 as answer after division of 9/3
#(ii) % modulus operator is used for modulus purpose i.e. it returns the remainder after division 
d=10%3# d will hold the value 1 as 10%3=1
#(iii) // floor division operator is used as to return floor division 
e=15//2# e=2 as floor division
#(iv) ** is exponentiation operator is used to return exponential value
f=2**3# f= 8 as f= 2*2*2

#ans 4
list_cutom=["rahul",45,"akash","true","kunal",6,"manoj",10,4.5,10]
for i in list_cutom:
    print(i)
    print(type(i))

#ans 5
count=0
while A%B==0:
    A=A/B
    count=count+1
print (count)

#ans 6
list l=[12,1,92,3,49,-3,34,6,24,8,5,3,6,8,4,2,8,9,5,8,5,3,7,8,8]
for i in l:
    if i%3==0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 3")

#ans 7
#Basically, mutable data types in Python are those whose value can be changed in place after they have been created.
# example to demonstrate list is a mutable data type in python

# our current list
my_list = [1,2,3,4,5]

# using append operation in our list
my_list.append(10)
# printing our list after the operation
print("List after appending a value = ",my_list)
#immutable data type in python, immutable object cannot be changed after it is created
#In python, the string data types are immutable. Which means a string value cannot be updated. We can verify this by trying to update a part of the string which will led us to an error.
#example to demonstrate string is immutable data type in python
# Can not reassign 
t= "Tutorialspoint"
print type(t)
t[0] = "M"