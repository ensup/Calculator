e="n"
print('*This Calculator is only for addition*')
if e=='N':
    e='n'
while e=='n':
    f=int(input("Type first number:"))
    l=int(input("Type second number:"))
    a=f+l
    print(a)
    e=input("Do You want to exit?[Y,N]")
    if e=='N':
        e='n'
    

