x=int(input("enter first side="))
y=int(input("enter second side="))
z=int(input("enter third side="))
if(x==y==z):
    print("equivalent triangle")
elif(x==y<z or y==z<x or z==x<y or x==y>z or y==z>x or z==x>y):
    print("isolation triangle")
else:
    print("scalen triangle")