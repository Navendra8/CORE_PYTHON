

import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from random import randint

root = tk.Tk()  #create a root window or main window
root.title("Desktop")
root.iconbitmap("python_icon.ico")
root.configure(bg="black")


width = int(root.winfo_screenwidth()/2)
height = int(root.winfo_screenheight()/2)
root.wm_minsize(width,height)  #(width,height)
root.resizable(0,0)  #cannot resize height or width it will be same always

class Guessgame:
    def __init__(self,master):
        self.master = master
        self.f1 = tk.Frame(master,bg="gray")
        self.f1.pack(ipadx=width/2,ipady=height/2)
        self.l1 = tk.Label(self.f1,text="Welcome to guess game",font=("cursive",25,"bold"),fg="red",bg="black")
        self.l1.pack()

        self.l2 = tk.Label(self.f1,text="Guess any number between 1 to 100",font=("cursive",15),fg="white",bg="black")
        self.l2.pack(pady=(30,0))
        
        self.l3 = tk.Label(self.f1,text="START",font=("cursive",15),fg="white",bg="black")
        self.l3.pack(pady=(30,0))

        self.e1 = tk.Entry(self.f1,font=(None,24),fg="blue")
        self.e1.pack(fill="x",pady=(30,0))

        self.b1 = tk.Button(self.f1,text="SUBMIT",height=1,width=7,bg="#123456",fg="white",command=self.checkvalue,font=("cursive",20,"italic"))
        self.b1.pack(ipady=3,ipadx=3)
        
        self.i = 0
        self.num = randint(1,100)

        
    def check(self,ch):
        if self.num == ch:
            messagebox.showinfo("INFO",f"YOU WON AFTER {self.i} GUESSES")
            self.b1['state'] = "disabled"
            self.i = 0
        elif self.num<ch:
            self.l3.configure(text="THINK LESS")
        elif self.num>ch:
            self.l3.configure(text="THINK HIGH")
    def checkvalue(self):
        ch = int(self.e1.get())
        print(self.num)
        if self.i<5:
            self.check(ch)
            self.i += 1
        else:
            messagebox.showerror("ERROR","YOU LOSS")
            self.i = 0
            self.b1['state'] = "disabled"

obj = Guessgame(root)
root.mainloop()
