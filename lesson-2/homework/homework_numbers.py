# Q1
flt=float(input("float: "))
print(round(flt,2))

# Q2
n1 = input("n1: ")
n2 = input("n2: ")
n3 = input("n3: ")
print("Smallest: ",min(n1,n2,n3))
print("Largest: ",max(n1,n2,n3))

# Q3
km=float(input("km: "))
m=km*1000
print(f"{int(m)} meters and {int((m-int(m))*100)} centimeters")