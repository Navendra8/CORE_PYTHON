


bank = {'accno' : [1001,1002,1003,1004],
            'name' : ['anisha','annu','ankush','gopesh'],
            'bal' : [10000,20000,15000,30000],
            'password' : ['abcd8*','myname09%','passwd9!','admin88*'],
            'security_ques' : [1603,1704,1805,1906]
       }

from m import myforgotpass
from my import passvalidator
from my import mydatevalidator
from my import signup
from my import getdetails
from my import changepassword
from my import forgotpass







while True:
    print("\t1. Login\t2. Signup\t3. Forgot Password\t4 Exit")
    print("*"*90)
    choice=eval(input("Please Enter your choice from above "))
    if choice==1:
        account=eval(input("Please Enter your account number "))
        if len(str(account)) !=4:
            print("please enter only four digit account number ")
        else:
            if account in bank['accno']:
                i=bank['accno'].index(account)
                password=input("Please enter your passsword. ")
                if password==bank['password'][i]:
                    while True:
                            print("\t1. Credit\t2. Debit\t3. Change Password\t4. Check Details\t5. Logout")
                            print("*"*90)
                            choice=eval(input("please enter the choice from above:  "))
                            if choice==1:
                                credit=eval(input("please enter the amount you want to credit. "))
                                bank['bal'][i]=bank['bal'][i]+credit
                                print(f"your credit {credit} has been credited to your accout")
                                updated_balance= bank['bal'][i]+credit
                            if choice==2:
                                debit=eval(input("please enter the amount you want to debit. "))
                                bank['bal'][i]=bank['bal'][i]-debit
                                print(f"your credit {debit} has been debited to your accout")
                                updated_balance= bank['bal'][i]-debit
                            if choice==3:
                                password=input("please enter the NEW password you want to change. ")
                                retype=input("please enter the re renter the  new password  ")
                                passvalidator(retype) == "correct password"
                                if password==retype:
                                    bank['password'][i]=password
                                    print(f"your Password {password} has been updated into your accout")
                            if choice==4:
                                getdetails(bank)
                            if choice==5:
                                print("Thanks You ,Logged Out ")
                                break
                else:
                    print("Please enter valid password")
            else:
                print("Please check your account number ")
                
    if choice==2:
        signup(bank)
    if choice==3:
        def forgotpass(bank):
            acc=int(input("Please enter your account number "))
            i=bank['accno'].index(acc)
            sec=int(input("please enter your security question "))
            if sec == bank['security_ques'][i]:
                if bank['accno'][i]==bank['accno'][i]:
                    pas=input("please update your password ")
                    pas1=input("please update your password ")
                    if pas==pas1:
                        if passvalidator(pas) == "correct password":
                            bank['password'][i]=(pas)
                            print("Your account password has been updated")
                    else:
                        print("wrong pass")
                else:
                    print("please check your password")
            else:
                print("please check your account or security question")
        forgotpass(bank)
        
    if choice==4:
        print("Thank you for banking with us ")
        break
print("Thank you for banking with us ")



