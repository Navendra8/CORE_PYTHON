

## password should not match name or common name 
import getpass

print("*"*70)
print("*"*70)
print("Welcome".center(70))
print("*"*70)
print("*"*70)
name=input("\nEnter you name : ").title()
dob=getpass.getpass("Enter your date of birth ")
sp=["!","@","%","*","£","#","?"]
city=input("Enter your city name :")
#password=getpass.getpass("Enter your pass password :")
s=0
a=0
d=0
chance=0
while chance<=5:
    password=getpass.getpass("Enter your pass password :")
    if password==name:
        print("your password should not match your name ")
        continue
    elif password==dob:
        print("Your password should not match your dob")
        continue
    elif password!=dob and password!=name:
        for i in password:
            if  i in sp:
                s+=1
            elif i.isalpha():
                a+=1
            elif i in "1234567890":
                d+=1
        if i==0 or a==0 or d==0:
            print("wrong pin")
            print(password)
        else:
            print("correct pin")
            print(password)
            break
    chance+=1
    print(f"your remaining chance is {5-chance}")    
    print("You Enter your date of birth is :",dob)
    print("Your password is ",password)
    print(f"Your name is ",name)
        
else:
    print("Not Right")
            
            


