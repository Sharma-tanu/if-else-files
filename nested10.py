a=int(input("enter the physics number"))
b=int(input("enter the chemistry number"))
c=int(input("enter the mathematics number"))
d=int(input("enter the biology number"))
e=int(input("enter the computer number"))
total=a+b+c+d+e
percentage=(total/500*100)
print("total marks=",total,"percentage",percentage)
if(percentage>=90):
    print("you have got grade A")
    if(percentage>=80):
        print("you have got grade B")
        if(percentage>=70):
            print("you have got grade C")
            if(percentage>=60):
                print("you have got grade D")
                if(percentage>=40):
                    print("you have got grade E")
                else:
                    print("you have got grade F")
            else:
                print("you have got grade F")
        else:
            print("you have got grade F")
    else:
        print("you have got grade F")
else:
    print("you have got grade F")                                    