import time
class Car_Rental():
    hatchback=["Maruti 800","Polo"]
    sedan=["Honda City,","BMW 3 series","BMW 5 series" ]
    suv=["FORTUNER","XUV500","Rangrover"]
    def display_car(self):
        print("Car available in Hatchback are follows :   ")
        time.sleep(1)
        for hatchback in self.hatchback:
            time.sleep(1)
            print(hatchback)
        print("Car available in Sedan are follows :   ")
        time.sleep(1)
        for sedan in self.sedan:
            time.sleep(1)
            print(sedan)
            
        print("Car available in Hatchback are follows :   ")
        time.sleep(1)
        for SUV in self.suv:
            time.sleep(1)
            print(SUV)
            
class Rent(Car_Rental):
    def __init__(self,no_days=None):
        self.no_days=no_days
    
    def rent_hatchback(self,no_days):
        rent=50*no_days
        print(f"YOUR RENT IS {rent} plus taxes as follows:   ")
        time.sleep(1)
        rent1=rent+(rent*20.5/100)
        print(f"HELLO {self.name} YOUR TOTAL RENT IS {rent1} FOR {no_days} days, We'll send you copy of invoice on {self.emailaddress}")

        
    def rent_sedan(self,no_days):
        rent=100*no_days
        print(f"YOUR  RENT IS {rent} plus taxes as follows:   ")
        time.sleep(1)
        rent1=rent+(rent*20.5/100)
        print(f"HELLO {self.name} YOUR TOTAL RENT IS {rent1} FOR {no_days} days, We'll send you copy of invoice on {self.emailaddress}")

            
    def rent_suv(self,no_days):
        rent=1000*no_days
        print(f"YOUR RENT IS {rent} plus taxes as follows:   ")
        time.sleep(1)
        rent1=rent+(rent*20.5/100)
        print(f"HELLO {self.name} YOUR TOTAL RENT IS {rent1} FOR {no_days} days, We'll send you copy of invoice on {self.emailaddress}")
    
        
class customer(Rent,Car_Rental):
    def __init__(self,days=None,name=None,address=None,emailaddress=None):
        self.days=days
        self.name=input("Enter your Name :")
        self.address=input("enter your address : ")
        self.emailaddress=input("Enter your email address :")
        for i in self.emailaddress:
                if i =="@":
                    print("Correct email address ")
                    break
                else:
                    print("Enter a valid email addresses")
                    
    def rental(self):
        print(f"Enter the type of car \n1.-->sedan\n2.-->suv\n3.-->hatchback :")
        choice=int(input("Enter your choice :"))
        if choice == 1:
            day=int(input("no of days"))
            Rent.rent_sedan(self,day)
            
        elif choice == 2:
            day=int(input("no of days"))
            Rent.rent_suv(self,day)
            
        elif choice==3 :
            day=int(input("no of days"))
            Rent.rent_hatchback(self,day)
            
        else:
            print("Please enter a valid type of car ")
    


