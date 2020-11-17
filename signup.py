def signup(bank):
    """
    THIS FUNCTION IS FOR SIGNUP A NEW CUSTOMER IN THE BANK APP
    It will autometcally will generate new account number 
    and will append all details 
    
    """
   
    name=input("Please enter your name: " )
    balance=int(input("Please enter your inital balance:  "))
    password=input("Please enter your password")
    security_ques=input("Please enter your sequrity question in formate of ddmm ")
    if balance>=10000:
        bank['name'].append(name)
        bank['bal'].append(balance)
        bank['password'].append(password)
        bank['security_ques'].append(security_ques)
    else:
        return "Minimum amount is 10000"
    
    accno = len(bank['name'])+1000
    print("Your new accno is : ",accno)
    bank['accno'].append(accno)
    return "THANK YOU"
