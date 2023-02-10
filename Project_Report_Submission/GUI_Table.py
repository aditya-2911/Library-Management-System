
from tkinter import*
from tkinter import messagebox
import subprocess
import mysql.connector
import tkinter
from tkmacosx import Button



class System:
    def __init__(self,root):
        self.root=root
        self.root.title("Lirary Management System")
        self.root.geometry("1280x720+0+0")
        
        self.ndb_var=StringVar()
        self.usedb_var=StringVar()
        self.addTable_var=StringVar()
        self.addAttribute_var=StringVar()
        self.addDomain_var=StringVar()
        self.addConsraints_var=StringVar()
        
        
        lbltitle=Label(self.root,text="Lirary Management System",bg="#040405",fg="white",bd=10,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        Dataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#040405")
        Dataframe.place(x=0,y=100,width=1250,height=570)
        
        frame=LabelFrame(Dataframe,text="Database Information",bg="#040405",bd=2,relief=RIDGE,font=("times new roman",24,"bold"))
        frame.place(x=0,y=5,width=1200,height=450)
        
        
        
        lblnamedb=Label(frame,bg="#040405",text="Database Name",font=("times new roman",16,"bold"),padx=2,pady=6)
        lblnamedb.grid(row=1,column=0,sticky=W)
        
        txtnamedb=Entry(frame,textvariable=self.ndb_var,font=("times new roman",16,"bold"),width=35)
        txtnamedb.grid(row=1,column=1)

        
        lblusedb=Label(frame,bg="#040405",text="Use Database Name ",font=("times new roman",16,"bold"),padx=2,pady=6)
        lblusedb.grid(row=2,column=0,sticky=W)
        
        txtusedb=Entry(frame,textvariable=self.usedb_var,font=("times new roman",16,"bold"),width=35)
        txtusedb.grid(row=2,column=1)
        
        lbladdTable=Label(frame,bg="#040405",text="Table Name ",font=("times new roman",16,"bold"),padx=2,pady=6)
        lbladdTable.grid(row=3,column=0,sticky=W)
        
        txtaddTable=Entry(frame,textvariable=self.addTable_var,font=("times new roman",16,"bold"),width=35)
        txtaddTable.grid(row=3,column=1)
        
        lbladdAttribute=Label(frame,bg="#040405",text="Attribute",font=("times new roman",16,"bold"),padx=2,pady=6)
        lbladdAttribute.grid(row=4,column=0,sticky=W)
        
        txtaddAttribute=Entry(frame,textvariable=self.addAttribute_var,font=("times new roman",16,"bold"),width=35)
        txtaddAttribute.grid(row=4,column=1)
        
        lbladdDomain=Label(frame,bg="#040405",text="Domain",font=("times new roman",16,"bold"),padx=2,pady=6)
        lbladdDomain.grid(row=5,column=0,sticky=W)
        
        txtaddDomain=Entry(frame,textvariable=self.addDomain_var,font=("times new roman",16,"bold"),width=35)
        txtaddDomain.grid(row=5,column=1)
        
        lbladdConsraints=Label(frame,bg="#040405",text="Contraints",font=("times new roman",16,"bold"),padx=2,pady=6)
        lbladdConsraints.grid(row=6,column=0,sticky=W)
        
        txtaddConsraints=Entry(frame,textvariable=self.addConsraints_var,font=("times new roman",16,"bold"),width=35)
        txtaddConsraints.grid(row=6,column=1)

        btnAddDatabase=Button(frame,command=self.adddb,text="Add Database",font=("times new roman",16,"bold"),height=25,width=150,bg="#1089ff",fg="white",borderless=1)
        btnAddDatabase.place(x=450,y=3)
        
        btnUseDatabase=Button(frame,command=self.useDatabase,text="Use Database",font=("times new roman",16,"bold"),height=25,width=150,bg="#1089ff",fg="white",borderless=1)
        btnUseDatabase.place(x=450,y=37.5)
        
        btnaddTable=Button(frame,command=self.addTable,text="Add Table",font=("times new roman",16,"bold"),height=25,width=150,bg="#1089ff",fg="white",borderless=1)
        btnaddTable.place(x=450,y=75)
        
        btnaddAttribute=Button(frame,command=self.AlterTable,text="Add New Attribute",font=("times new roman",16,"bold"),height=25,width=150,bg="#1089ff",fg="white",borderless=1)
        btnaddAttribute.place(x=450,y=105.5)

        btnReset=Button(frame,command=self.reset,text="Reset",font=("times new roman",16,"bold"),height=25,width=150,bg="#ed3833",fg="white",borderless=1)
        btnReset.place(x=450,y=174.5)
        
        
        usedbname=self.usedb_var.get()
        #-------------------------Bottom Frame-----------------------------------------------------------------------------------------------------------
        Dataframe1=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="#040405")
        Dataframe1.place(x=30,y=580,width=1200,height=60)
        
        btnResetall=Button(Dataframe1,command=self.resetall,text="Reset All",font=("times new roman",16,"bold"),height=25,width=150,bg="#ed3833",fg="white",borderless=1)
        #btnResetall.grid(row=0,column=1)
        btnResetall.place(x=100,y=7)
        
        btnSave=Button(Dataframe1,command=self.save,text="Save and Proceed",font=("times new roman",16,"bold"),height=25,width=150,bg="#ed3833",fg="white",borderless=1)
        btnSave.place(x=500,y=7)
        
        btnExit=Button(Dataframe1,command=self.Exit,text="Exit",font=("times new roman",16,"bold"),height=25,width=150,bg="#ed3833",fg="white",borderless=1)
        btnExit.place(x=800,y=7)
        
        
        
    def adddb(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mysql@123"
        )

        mycursor = db.cursor()

        dbname=self.ndb_var.get()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS %s" %dbname)
        
        db.commit()
        db.close()

        messagebox.showinfo("Success","Database has been Added")


    def useDatabase(self):
        global usedbname
        usedbname=self.usedb_var.get()
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mysql@123",
            database=usedbname
        )
        
        
        db.commit()
        db.close()

        messagebox.showinfo("Success","Database Changed")
    
    def addTable(self):
        global tablename
        global attribute
        global domain
        global contraints
        
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mysql@123",
            database=usedbname
        )
        
        tablename=self.addTable_var.get()
        attribute=self.addAttribute_var.get()
        domain=self.addDomain_var.get()
        contraints=self.addConsraints_var.get()
        
        mycursor = db.cursor()
        
        if contraints=="":
            mycursor.execute("CREATE TABLE %s"%tablename+"(%s"%attribute+" "+"%s)"%domain)
        else:
            mycursor.execute("CREATE TABLE %s"%tablename+"(%s"%attribute+" "+"%s,"%domain+" "+"%s)"%contraints)
        
        db.commit()
        db.close()

        messagebox.showinfo("Success","Table has been Added")
    
    
    def AlterTable(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mysql@123",
            database=usedbname
        )
        tablename=self.addTable_var.get()
        attribute=self.addAttribute_var.get()
        domain=self.addDomain_var.get()
        contraints=self.addConsraints_var.get()
        mycursor = db.cursor()
        
        mycursor.execute("ALTER TABLE %s "%tablename+"ADD COLUMN %s"%attribute+" "+"%s"%domain)
        
            
        db.commit()
        db.close()

        messagebox.showinfo("Success","Table has been Altered")
    
    
    def save(self):
            subprocess.call("/Users/aditya/Programs/Python/DBMS_Project_GUI/runLibrary.sh", shell=TRUE)
        
        
    def reset(self):
        self.addAttribute_var.set(""),
        self.addDomain_var.set(""),
        self.addConsraints_var.set("")

    def resetall(self):
        self.ndb_var.set(""),
        self.usedb_var.set(""),
        self.addTable_var.set(""),
        self.addAttribute_var.set(""),
        self.addDomain_var.set(""),
        self.addConsraints_var.set("")
        
    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if Exit>0:
            self.root.destroy()
            return    
        

if __name__ == "__main__":
    root=Tk()
    obj=System(root)
    root.mainloop()