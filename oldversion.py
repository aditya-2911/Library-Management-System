from tkinter import*
from tkinter import messagebox 
import mysql.connector

class System:
    def __init__(self,root):
        self.root=root
        self.root.title("Lirary Management System")
        self.root.geometry("1280x720+0+0")
        
        self.ndb_var=StringVar()
        self.usedb_var=StringVar()
        self.addTable_var=StringVar()
        self.attribute1_var=StringVar()
        
        lbltitle=Label(self.root,text="Lirary Management System",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        Dataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Dataframe.place(x=0,y=100,width=1250,height=570)
        
        frame=LabelFrame(Dataframe,text="Database Information",bg="powder blue",bd=2,relief=RIDGE,font=("times new roman",24,"bold"))
        frame.place(x=0,y=5,width=1200,height=450)
        
        lblnamedb=Label(frame,bg="powder blue",text="Database Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblnamedb.grid(row=1,column=0,sticky=W)
        
        txtnamedb=Entry(frame,textvariable=self.ndb_var,font=("times new roman",14,"bold"),width=35)
        txtnamedb.grid(row=1,column=1)

        
        lblusedb=Label(frame,bg="powder blue",text="Use Database Name ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblusedb.grid(row=2,column=0,sticky=W)
        
        txtusedb=Entry(frame,textvariable=self.usedb_var,font=("times new roman",14,"bold"),width=35)
        txtusedb.grid(row=2,column=1)
        
        lbladdTable=Label(frame,bg="powder blue",text="Table Name ",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbladdTable.grid(row=3,column=0,sticky=W)
        
        txtaddTable=Entry(frame,textvariable=self.addTable_var,font=("times new roman",14,"bold"),width=35)
        txtaddTable.grid(row=3,column=1)
        
        #txtattribute1=Entry(frame,textvariable=self.attribute1_var,font=("times new roman",14,"bold"),width=35)
        #txtattribute1.grid(row=3,column=1)
        
        btnAddDatabase=Button(frame,command=self.adddb,text="Add Database",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddDatabase.place(x=450,y=2)
        
        btnUseDatabase=Button(frame,command=self.useDatabase,text="Use Database",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnUseDatabase.place(x=450,y=33.5)
        
        btnaddTable=Button(frame,command=self.addTable,text="Add Table",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnaddTable.place(x=450,y=65)
        

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
        #usedbname=self.usedb_var.get()
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mysql@123",
            database=usedbname
        )
        
        tablename=self.addTable_var.get()
        mycursor = db.cursor()
        mycursor.execute("CREATE TABLE %s(name VARCHAR(25), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"%tablename)
        
        
        db.commit()
        db.close()

        messagebox.showinfo("Success","Table has been Added")
        
        """""
        def addTable(self):
            tablename=self.addTable_var.get()
            attribute1=self.attribute1_var.get()
            mycursor.execute("CREATE TABLE %s"%tablename+"(name "%attribute1+)
"""


if __name__ == "__main__":
    root=Tk()
    obj=System(root)
    root.mainloop()