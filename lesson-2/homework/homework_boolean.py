# Q1
u = input("Username: ")
p = input("Password: ")
if (u.strip()!="" and p.strip()!=""):
    print("yes")

# Q2
a=input("Number1: ")
b=input("Number2: ")
if(a==b):
    print("yes")

# Q3
n=int(input("Number: "))
if(n%2==0 and n>0):
    print("yes")

# Q4
n1=int(input("n1: "))
n2=int(input("n2: "))
n3=int(input("n3: "))
if(n1!=n2 and n1!=n3 and n2!=n3):
    print("yes")

# Q5
s1=input("s1: ")
s2=input("s2: ")
if(len(s1)==len(s2)):
    print("yes")

# Q6
num=int(input("number: "))
if(num%3==0 and num%5==0):
    print("yes")

# Q7
num1=int(input("num1: "))
num2=int(input("num2: "))
if(num1+num2>50):
    print("yes")

# Q8
number=int(input("Number 1: "))
if(number>=10 and number<=20):
    print("yes")
