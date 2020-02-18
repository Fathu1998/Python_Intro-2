t=input("Enter the DNA sequence")
print(t)
RNA=''
for i in t:
    if i=='T':
            RNA=RNA+'U'
    else:
            RNA=RNA+i
    print(RNA)
    
