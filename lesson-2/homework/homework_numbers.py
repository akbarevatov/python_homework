# Q1
flt=float(input("float: "))
print(round(flt,2))

# Q2
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
print("Smallest: ",min(n1,n2,n3))
print("Largest: ",max(n1,n2,n3))

# Q3
km=float(input("km: "))
m=km*1000
print(f"{int(m)} meters and {int((m-int(m))*100)} centimeters")

# Q4
a=int(input("number 1: "))
b=int(input("number 2: "))
print(f"division={a//b} , remainder={a%b}")

# Q5
c=int(input("celsius: "))
print(c*9/5+32)

# Q6
x=int(input("Number: "))
print(x%10)

# Q7
y=int(input("Number: "))
if(y%2==0):
    print("yes")
else:
    print("no")
