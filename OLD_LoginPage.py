from tkinter import*
from tkinter import messagebox
import tkinter
import subprocess
from tkmacosx import Button
from tkinter import messagebox 

class LoginPage:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Lirary Management System")
        self.root.geometry("1280x720+150+80")
        self.root.configure(bg="#d7dae2")
        self.root.title("Library Management System")
        
        
        lblTitle=Label(text="Login",font=("times new roman",50,"bold"),fg="black",bg="#d7dae2")
        lblTitle.pack(pady=50)
        
        bordercolor=Frame(self.root,bg="black",width=800,height=400)
        bordercolor.pack()
        mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
        mainframe.pack(padx=20,pady=20)
        
        Label(mainframe,text="Username",font=("times new roman",30,"bold"),bg="#d7dae2").place(x=100,y=50)
        Label(mainframe,text="Password",font=("times new roman",30,"bold"),bg="#d7dae2").place(x=100,y=150)
        
        
        username=StringVar()
        password=StringVar()
        
        entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("times new roman",30))
        entry_username.place(x=400,y=50)
        entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("times new roman",30),show="*")
        entry_password.place(x=400,y=150)
        
        
        def login():
            user=username.get()
            code=password.get()
            if user=="Admin" and code=="12345":
                subprocess.call("/Users/aditya/Programs/Python/DBMS_Project_GUI/runGUI_Table.sh", shell=TRUE)
            
            elif user=="" and code=="":
                messagebox.showerror("Invalid","Please Enter Username and Password")
            
            elif user=="":
                messagebox.showerror("Invalid","Username is Required")
            elif code=="":
                messagebox.showerror("Invalid","Password is Required")
            elif user!="Admin" and code!="12345":
                messagebox.showerror("Invalid","Invalid Username and Password")
            elif user!="Admin":
                messagebox.showerror("Invalid","Invalid Username")
            elif code!="1234":
                messagebox.showerror("Invalid","Invalid Password")
                
            
        def reset():
            entry_username.delete(0,END)
            entry_password.delete(0,END)
            
        def Exit():
            Exit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
            if Exit>0:
                quit()
        
        Button(mainframe,text="Login",height=50,width=100,bg="#ed3833",fg="white",borderless=1,command=login).place(x=100,y=250)
        Button(mainframe,text="Reset",height=50,width=100,bg="#1089ff",fg="white",borderless=1,command=reset).place(x=300,y=250)
        Button(mainframe,text="Exit",height=50,width=100,bg="#00bd56",fg="white",borderless=1,command=Exit).place(x=500,y=250)
        
        
if __name__ == "__main__":
    root=Tk()
    obj=LoginPage(root)
    root.mainloop()