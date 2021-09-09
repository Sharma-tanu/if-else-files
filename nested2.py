balance=20000
card= input("enter the card")
language= input("enter the language")
account= input("enter the account")
password=int(input("enter the password"))
amount= int(input("enter the amount"))
receipt= input("enter the receipt")
if card=="debit card":
    if language=="enghish":
        if account== "saveing":
            if password== 123456:
                if amount > 0 and amount <=2000:
                    print("your translete is comolet now your balance is",balance-amount)
                    if receipt=="yes":
                        print ("sucsful")
                    else:
                        print("a")
                else:
                    print("b")
            else:
                print("c")
        else:
            print("account is current")
    else:
        print("hindi")
else:
    print("card is correct")                        


            
            


