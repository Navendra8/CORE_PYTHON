

bank = {'accno' : [1001,1002,1003,1004],
            'name' : ['anisha','annu','ankush','gopesh'],
            'bal' : [10000,20000,15000,30000],
            'password' : ['abcd8*','myname09%','passwd9!','admin88*'],
            'security_ques' : [1603,1704,1805,1906]
       }



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
                                print(f"your credit {debit} has been credited to your accout")
                                updated_balance= bank['bal'][i]-debit
                            if choice==3:
                                password=input("please enter the NEW password you want to change. ")
                                retype=input("please enter the re renter the  new password  ")
                                if password==retype:
                                    bank['password'][i]=password#replacing the password
                                    print(f"your Password {password} has been updated into your accout")
                            if choice==4:
                                print(f"your account number is {bank['accno'][i]}")
                                print(f"your name is {bank['name'][i]}")
                                print(f"your balance is {bank['bal'][i]}")
                                print(f"your password is {bank['password'][i]}")
                                print(f"your security_ques is {bank['security_ques'][i]}")
                            if choice==5:
                                print("Thanks You ,Logged Out ")
                                break
                else:
                    print("Please enter valid password")
            else:
                print("Please check your account number ")
                
    if choice==2:
        i=bank['accno'].index(account)
        p=len(bank['accno'])
        x=p+1001
        ac_num=bank['accno'].append(x)
        a=input("Please Enter your name :")
        bank['name'].append(a)
        b=eval(input("Please Enter your initial amount: "))
        if b<=10000:
            print("Error: Minimum Amount should be 10,000")
        bank['bal'].append(b)
        c=input("Please Enter your password: ")
        bank['password'].append(c)
        d=input("Please Enter your security question: ")
        bank['security_ques'].append(d)
    if choice==3:
        while True:
            account=eval(input("Please Enter your account number "))
            if len(str(account)) !=4:
                print("please enter only four digit account number ") 
            else:
                if account in bank['accno']:
                    i=bank['accno'].index(account)
                    ques=int(input("Please enter your securtiy question in DDMM "))
                    if ques==bank['security_ques'][i]:
                        passw=input("Enter your new password  ")
                        passw1=input("Confirm your new password  ")
                        if passw==passw1:
                            bank['password'][i]=passw1
                            print("Your password has been successfully changed ")
                        else:
                            print("Password doesnt match")

                    else:
                        ques=int(input("Please enter your securtiy question in DDMM "))
                else:
                    account=eval(input("Please Enter your account number "))
    if choice==4:
        print("Thank you for banking with us ")
        break
print("Thank you for banking with us ")



