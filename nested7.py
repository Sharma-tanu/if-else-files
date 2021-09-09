num1=int(input("enter the first num1"))
num2=int(input("enter the second num2"))
symbol=input("enter a symbol")
if symbol=="+":
    print(num1+num2)
    if symbol=="-":
        print(num1-num2)
        if symbol=="*":
            print(num1*num2)
            if symbol=="%":
                print(num1%num2)
                if symbol=="/":
                    print(num1/num2)
                else:
                    print("worng opretor")
            else:
                print("worng opretor")
        else:
            print("worng opretor")
    else:
        print("worng opretor")
else:
    print("worng opretor")                                    
                        
            