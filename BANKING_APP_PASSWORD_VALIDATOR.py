
from mydatevalidator import mydatevalidator
from passvalidator import passvalidator

def login(bank):
    account=eval(input("Please Enter your account number "))
    if len(str(account)) !=4:
            print("please enter only four digit account number ")
    else:
        if account in bank['accno']:
            i=bank['accno'].index(account)
            password=input("Please enter your passsword. ")
            if password==bank['password'][i]:
                while True:
                        print("\n1.\t Credit\n2.\t Debit\n3.\t Change Password\n4.\t Check Details\n5.\t Logout")
                        choice=eval(input("please enter the choice from above:  "))
                        if choice==1:
                            credit=eval(input("please enter the amount you want to credit. "))
                            bank['bal'][i]=bank['bal'][i]+credit
                            print(f"your credit {credit} has been credited to your accout")
                            updated_balance= bank['bal'][i]+credit
                        if choice==2:
                            debit=eval(input("please enter the amount you want to debit. "))
                            bank['bal'][i]=bank['bal'][i]-debit
                            print(f"your credit {debit} has been credited to your accout")
                            updated_balance= bank['bal'][i]-debit
                        if choice==3:
                            s=input("Please Enter your security question in DDMM ")
                            from mydatevalidator import mydatevalidator
                            mydatevalidator(s):
                                if True :
                                    
                                
                            password=input("please enter the NEW password you want to change. ")                                
                            retype=input("please enter the re renter the  new password  ")
                            if password==retype:
                                passvalidator(p)
                                bank['password'][i]=password#replacing the password
                                print(f"your Password {password} has been updated into your accout")
                        if choice==4:
                            print(f"your account number is {bank['accno'][i]}")
                            print(f"your name is {bank['name'][i]}")
                            print(f"your balance is {bank['bal'][i]}")
                            print(f"your password is {bank['password'][i]}")
                            print(f"your security_ques is {bank['security_ques'][i]}")
                        if choice==5:
                            print("Thanks You, Have a nice Day ")
                            break
            else:
                 print("Please enter valid password")
        else:
            print("Please check your account number ")
    
