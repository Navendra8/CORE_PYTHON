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
        print(f"YOUR TOTAL RENT IS {rent1} FOR {no_days} days")
        
    def rent_sedan(self,no_days):
        rent=100*no_days
        print(f"YOUR  RENT IS {rent} plus taxes as follows:   ")
        time.sleep(1)
        rent1=rent+(rent*20.5/100)
        print(f"YOUR TOTAL RENT IS {rent1} FOR {no_days} days")     
            
    def rent_suv(self,no_days):
        rent=1000*no_days
        print(f"YOUR RENT IS {rent} plus taxes as follows:   ")
        time.sleep(1)
        rent1=rent+(rent*20.5/100)
        print(f"YOUR TOTAL RENT IS {rent1} FOR {no_days} days")
        
class customer(Rent,Car_Rental):
    def __init__(self,days=None,):
        self.days=days
        
        
    def personal_infromation(Name,address,jobtitle):
        Name=input("Enter your Name :")
        address=input("enter your address: ")
        jobtitle=input("Enter your jobtitle")
        
        
    def rental(self):
        print(f"Enter the type of car \n1.-->sedan\n2.-->suv\n3.-->hatchback :")
        choice=int(input("Enter your choice :"))
        if choice == 1:
            day=int(input("no of days"))
            Rent.rent_sedan(self,day)
            
        if choice == 2:
            day=int(input("no of days"))
            Rent.rent_suv(self,day)
            
        if choice==3 :
            day=int(input("no of days"))
            Rent.rent_hatchback(self,day)
            
        else:
            print("Please enter a valid type of car ")

