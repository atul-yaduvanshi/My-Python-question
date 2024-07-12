""""
x = int(input("enter a number"))
x =x//10%10
print(x)
"""
# x=x//100
# x=x%10
# swapp the a,b = a,b
# a,b = b,a
""""
s = input("Enter a string")
print("my" in s)
"""
""""
print("Enter Two String")
s1 = input()
s2 = input()
print(s1 is s2)
"""
# print(5>10<5)
# print("white" and "red")
# print(True or False)
""""
x = int(input("enter a number"))
if x>=0:
    print("positive number")
else:
    print("negative number")
"""
"""
x = int(input("enter a number"))
if x%5==0:
    print("number is divisible by 5")

else:
    print("number is not divisible by 5")
"""
"""
x = int(input("enter a number"))
if x%2==0:
    print("number is even")
else:
    print("number is odd")
"""
""""
print("Enter a two numbers")
a = int(input())
b = int(input())
if a>b:
    print("greater number")
else:
    print("b is greater then a")
"""
"""
w1 = input()
w2 = input()
if w1<w2:
    print(w1,w2 ,end=" ")
else:
    print(w2,w1,end=" ") 
"""
""""
x = int(input("enter a three digit number"))
if 999>=x=<999:
    print("number is three digit")
else:
    print("number is not a three digit")    
"""
"""
x = int(input("enter a number"))
if x>0:
    print("Number is positive")
elif x<0:
    print("Number is Negative")    
else:
    print("zero")
"""
"""
n = int(input("Enter a Number"))
i = 1
while i<=n:
    print("mysirg")
    i+=1
"""
"""
n = int(input("Enter a Number"))
i = 1
while i<=n:
    print(i)
    i+=1
"""
"""
n = int(input("Enter a Number"))
# 987654321
i=1
while i<=n:
    print(2*i-1)
    i+=1
"""
"""
n = int(input("Enter a Number"))
i = 1
while i<=n:
    print(2*i-2)
    i+=1
"""
"""
n = int(input("Enter a Number"))
while n:
    print(2*n,end=" ")
    n-=1
"""
"""
n = int(input("Enter a Number"))
i=1
while i<=n:
    print(i**3,end=" ")
    i+=1
"""
"""
n = int(input("Enter a Number"))
i = 1
while i<=n:
    print(i**3,end=" ")
    i+=1
"""
"""
n = int(input("Enter a Number"))
i = 1
while i<=n:
    print(i*n, sep=" ")
    i+=1
"""
"""
x = input("Enter a String")
for e in x :
    print(e,ord(e))
"""
"""
s = input("Enter a String")
v = "aieouAIEOU"
for e in s:
    if e in v:
        print(e)
"""
"""
s = input("Enter a String")
count = 0
for e in s:
    if e == " ":
     count +=1
print("count=",count)     
"""
"""
s = input("Enter a Number")
count = 0
for e in s:
    count+=1
    print("count=",e)
"""
"""
for x in range(1,11):
    print(x*5)
"""
""""
n = int(input("Enter a Number"))
for x in range(1,10):
    print(x*n)
"""
"""
n = input("Enter a nuber")
for x in range(1,11):
    print(x*n)
"""
"""
n = int(input("enter a number"))
for x in range(10,0,-1):
    print(n*x)
"""
"""
n = int(input("enter a number"))
for x in range(1,11):
    print("{}*{}={}".format(n,x,n*x))
"""
"""
for e in range(1,10):
    print(e*10,end=" ")
"""
"""
n = int(input("Enter a Number"))
for e  in range(1,n+1):
    print(e*2)
"""
"""
n = int(input("enter a number"))
for e in range(1,1+n):
    print(2*e-1)   
"""
"""
n = int(input("enter a number"))
for e in range(1,1+n):
    print(e**2)
"""
"""
start = int(input("enter a start value"))
end = int(input("enter a end value"))
for x in range(start,end):
    for i in range(2,x):
        if(x%i==0):
            break
        else:
            print(x,end=" ")
"""
"""
s = 0
n = int(input("enter a number"))
for i in range(1,n+1):
    s=s+i
    print("sum is ",s)
"""
"""
s=0 
n=int(input("enter a number"))
for i in range(1,n+1):
    s=i**2
    print("square is",s)
"""
# factorial using while loop
"""
n = int(input("enter a number"))
f = 1
while n:
    f=n*f
    n-=1
    print("factorial is",f)
"""
# count number of digits
"""
x = int(input("Enter a Number"))
count = 0
while x:
    x = x//10
    count +=1
    print("Total digit is:",count)
"""
# add number of digits
"""
x = int(input("enter a number"))
c = 0
while x:
    c = c+x%10
    x=x//10
    print(c)
"""
# sum of list
"""
print("enter a number a separated bu comma")
l1 = [int (e) for e in input().split(",")]
s = sum(l1)
print(s)
"""
# avg of element of list
"""
print("enter a number separated by comma")
l1 = [int(e) for e in input().split(",")]
avg = sum(l1)/len(l1)
print(avg)
"""
# square of number to given list
"""
print("enter a number separated by comma")
l1 = [int(e) for e in input().split(",")]
l2 = [e**2 for e in l1]
print(l2)
"""
# short list element in descending order
"""
print = input("enter a number separated by comma")
l1 = [int(e) for e in input().split(",")]
l1.sort(reverse=True)
print(l1) 
"""
# create first N even natural number
"""
l1 = list(range(2,2*int(input("enter a number"))+1,2))
print(l1)
"""
# first n erm of fibonaccii sereis
# 0 1 1 2 3 5 8 13......fibonacii series
"""
a,b= -1,1
l2 = []
n = int(input("enter a number"))
while n:
   c=a+b
   l2.append(c)
   a=b
   b=c
   n-=1
print(l2) 
"""
# create a first N prime number
"""
n = int(input("enter a number"))
l3=[]
x=2
while n:
    for i in range(2,x):
        if x%i==0:
            break
        else:
            l3.append(x)
            n-=1
        x+=1
print(l3)            
"""
# check a given only alphabet in str
""""
s1 = input("Enter a String")
for e in s1:
    if e>'a' or e<='z' and e>='A' or e<='Z':
        pass
    else:
        print("String atleast one character which is not an alphabet")
        break
else:
    print("String contain only alphabet")    
"""
# python script to check if a given character is present a given string or not.
""""
s1 = input("Enter a String")
ch = input("Enter a character")
if ch in s1:
    print("%s is in %s"%(s1,ch))
else:
    print("%s is not in %s"%(s1,ch))
"""
# count vowels given stirng.
"""
s1 = input("Enter a String")
count = 0
for e in s1:
    if e in 'aieouAIEOU':
        count +=1
else:
    print("count vowels =",count)        
"""
# Reverse string 
"""
s1 = input("Enter a String")
print(s1[::-1])
"""
# pyhton script to reverse a string word wise (atul kumar yadav) resulting should be (yadav kumar atul).
""""
s1 = input("Enter a String")
print(' '.join(s1.split(' ')[::-1]))
"""
# python script to check whether it is palindrome or not.
"""
s1 = input("Enter a String")
print("palindrome"if s1==s1[::-1] else "not a palindrome")
"""
# python script to transform a given string to upper case.
"""
s1 = input("Enter a string")
print(s1.upper())
"""
# python script to find a maximum length word in a given text.
"""
s1 = input("Enter a String ")
print(len(s1.split(' ')))
"""
"""
s1 = input("Enter a String")
i = 0
index = 0
maxLength=-1
for w in s1.split(' '):
    if maxLength<len(w):
        maxLength=len(w)
        index=i
    i+=1
print("maximum length word",s1.split(' ')[index],"is",maxLength)
"""
#Python script to remove all non int values from a list.
"""
l1 = [20 ,2,3.4,'abc',3+7j,True,307,40]
i=0
l2=[]
while (i<len(l1)):
    if type (l1[i])==int:
        l2.append(l1[i])
    i+=1
print(l2)         
"""
# acurrence of number in python script 
""""
l1 = [20,30,20,40,50,60,20,40,30,50,90]
i = 0
for x in l1:
    if i==l1.index(x):
        print(x," ",l1.count(x))
    i+=1
"""
# write a python script to short a list of string.
""""
l1 = ['meerut','delhi','surat','shimla']
l1.sort()
print(l1)
"""
# write a python script to find first reapeted string in a list of string.
"""
l1 = ["meerut","agra","delhi","reeva",'meerut']
i = 0
for s in l1:
    if l1.index(s)!=i:
        print("first repeated string is",s,"at index",i)
        break
    i+=1
"""
# write a python script to count string which end at character 's' in a list of string.
""""
l1 = ["meeruts","agra","delhi","reevas",'merts']
count = 0
for s in l1:
   if s.endswith('s'):
      count+=1
print("count =",count)      
"""
# write a python script to create tuple from a given list.
"""
l1 = ['atul','meerut',10,30,'abc',1+9j,3.4]
t1 = tuple(l1)
print(t1,type(t1))
"""
# write python script to reverse a tuple.
""""""
l1 = ['atul','meerut','abc']
t1 = tuple(l1)[::-1]
print(t1)
"""

  










        






