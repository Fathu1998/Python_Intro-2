s=input("Enter the DNA sequence")
print(s)
a,c,t,g=0,0,0,0
for i in s:
    if i=="A":
        a=a+1
    elif i=="C":
        c=c+1
    elif i=="T":
        t=t+1
    elif i=="G":
        g=g+1

print("A-",a)
print("G-",g)
print("C-",c)
print("T-",t)
