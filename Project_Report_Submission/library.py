from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        ###Table varibles
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.pincode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbok_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

##########Labels and Buttons######################
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="#040405",fg="white",bd=10,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=8,relief=RIDGE,padx=20,bg="#040405")
        frame.place(x=0,y=130,width=1440,height=400)
        
        
        #DataFrame Left
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="#040405",bd=7,relief=RIDGE,font=("times new roman",18,"bold"))
        DataFrameLeft.place(x=0,y=5,width=750,height=350)
        
        #Account Type
        lblMember=Label(DataFrameLeft,bg="#040405",text="Member Type",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",14,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Professor","Student")
        comMember.grid(row=0,column=1)
        
        #PRN_No
        lblPRN_No=Label(DataFrameLeft,bg="#040405",text="PRN No",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",14,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)
        
        #ID No
        lblTitle=Label(DataFrameLeft,bg="#040405",text="ID No",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",14,"bold"),width=29)
        txtTitle.grid(row=2,column=1)
        
        #First Name
        lblFirstName=Label(DataFrameLeft,bg="#040405",text="First Name",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",14,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)
        
        #LastName
        lblLastName=Label(DataFrameLeft,bg="#040405",text="Last Name",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",14,"bold"),width=29)
        txtLastName.grid(row=4,column=1)
        
        #Address1
        lblAddress1=Label(DataFrameLeft,bg="#040405",text="Address1",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman",14,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)
        
        #Address2
        lblAddress2=Label(DataFrameLeft,bg="#040405",text="Address2",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("times new roman",14,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)
        
        #Pin Code
        lblPinCode=Label(DataFrameLeft,bg="#040405",text="Pin Code",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblPinCode.grid(row=7,column=0,sticky=W)
        
        txtPinCode=Entry(DataFrameLeft,textvariable=self.pincode_var,font=("times new roman",14,"bold"),width=29)
        txtPinCode.grid(row=7,column=1)
        
        #Mobile
        lblMobile=Label(DataFrameLeft,bg="#040405",text="Mobile",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",14,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
        
        # Book Id
        lblBookId=Label(DataFrameLeft,bg="#040405",text="Book Id",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",14,"bold"),width=29)
        txtBookId.grid(row=0,column=3)
        
        #Book Title
        lblBookTitle=Label(DataFrameLeft,bg="#040405",text="Book Title",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",14,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)
        
        #Author
        lblAuthor=Label(DataFrameLeft,bg="#040405",text="Author",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",14,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)
        
        #Date Borrowed
        lblDateBorrowed=Label(DataFrameLeft,bg="#040405",text="Date Borrowed",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",14,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)
        
        #Date Due
        lblDateDue=Label(DataFrameLeft,bg="#040405",text="Due Date",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",14,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        #Days on Book
        lblDaysOnBook=Label(DataFrameLeft,bg="#040405",text="Days On Book",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbok_var,font=("times new roman",14,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        #Late Return Fine
        lblLateReturnFine=Label(DataFrameLeft,bg="#040405",text="Late Return Fine",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("times new roman",14,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        
        #Date Over Due
        lblDateOverDue=Label(DataFrameLeft,bg="#040405",text="Date Over Due",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        
        txtDateOverDue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("times new roman",14,"bold"),width=29)
        txtDateOverDue.grid(row=7,column=3)
        
        #Actucal price
        lblActucalPrice=Label(DataFrameLeft,bg="#040405",text="Actucal Price",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblActucalPrice.grid(row=8,column=2,sticky=W)
        
        txtActucalPrice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("times new roman",14,"bold"),width=29)
        txtActucalPrice.grid(row=8,column=3)
        
        
        
        
        
        
        #DataFrame Right
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="#040405",bd=7,relief=RIDGE,font=("times new roman",18,"bold"))
        DataFrameRight.place(x=760,y=5,width=600,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=54,height=20,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Analog computation and simulation','Computer programming in C',
                    'Elements of parallel computing','Compiler Design',
                    'Programming in MATLAB','System software',
                    'Programming with C++','Embedded system design',
                    'Artificial intelligence','Computer system architecture',
                    'Operating Systems','Computer graphics',
                    'Data Structures and Algorithms','Python Programming']
        
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Analog computation and simulation"):
                self.bookid_var.set("ENBK111")
                self.booktitle_var.set("Analog computation Manual")
                self.author_var.set("Rajaraman, V")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 78")
            
            elif(x=="Computer programming in C"):
                self.bookid_var.set("ENBK112")
                self.booktitle_var.set("C Manual")
                self.author_var.set("Rajaraman, V")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 58")    
                
            elif(x=="Elements of parallel computing"):
                self.bookid_var.set("ENBK113")
                self.booktitle_var.set("Parallel Computing")
                self.author_var.set("Mital, K V.")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(15)
                self.latereturnfine_var.set("Rs. 35")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 68" )  
            
            elif(x=="Programming in MATLAB"):
                self.bookid_var.set("ENBK114")
                self.booktitle_var.set("MATLAB")
                self.author_var.set("Krishnamurthy, EV")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(15)
                self.latereturnfine_var.set("Rs. 25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 60" )

            elif(x=="System software"):
                self.bookid_var.set("ENBK115")
                self.booktitle_var.set("System software")
                self.author_var.set("Chattopadhyay, Santanu")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(15)
                self.latereturnfine_var.set("Rs. 00")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 60" )
            elif(x=="Compiler Design"):
                self.bookid_var.set("ENBK116")
                self.booktitle_var.set("Compiler Design")
                self.author_var.set("Chattopadhyay, Santanu")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(20)
                self.latereturnfine_var.set("Rs. 00")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 100" )    
            elif(x=="Programming with C++"):
                self.bookid_var.set("ENBK117")
                self.booktitle_var.set("C++")
                self.author_var.set("Juneja, B.L; Seth, Anita")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=5)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbok_var.set(13)
                self.latereturnfine_var.set("Rs. 12")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 100" )    
                
                
                
                
        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=35,height=20)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        
        #Button Frame
        Framebutton=Frame(self.root,bd=7,relief=RIDGE,padx=20,bg="#040405")
        Framebutton.place(x=0,y=530,width=1440,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=15,y=10)
        
        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=245,y=10)
        
        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=475,y=10)
        
        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=705,y=10)
        
        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=935,y=10)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("times new roman",16,"bold"),width=24,bg="red",fg="black")
        btnAddData.place(x=1165,y=10)
        
        #Information Frame (To show database)
        FrameDetails=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="#040405")
        FrameDetails.place(x=0,y=600,width=1440,height=200)
        
        
        Table_frame=Frame(FrameDetails, bd =3,relief=RIDGE,bg="#040405")
        Table_frame.place(x=0,y=2,width=1388,height=180)
        
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","pincode"
                                                            ,"mobile","bookid","booktitle","author","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("pincode",text="Pin Code")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Borrow Date")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Overdue Date")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("pincode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        #self.library_table.column("",width=100)
        self.fetch_data()
        
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            username="root",
            password="Mysql@123",
            database="LibraryGui")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),
                           self.prn_var.get(),
                           self.id_var.get(),
                           self.firstname_var.get(),
                           self.lastname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.pincode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.author_var.get(),
                           self.dateborrowed_var.get(),
                           self.datedue_var.get(),
                           self.daysonbok_var.get(),
                           self.latereturnfine_var.get(),
                           self.dateoverdue_var.get(),
                           self.finalprice_var.get()
                           ))
        
        
        conn.commit()
        self.fetch_data()
        conn.close()
            
        messagebox.showinfo("Success","Member has been Successfully Added")
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="LibraryGui")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row [0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.pincode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbok_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])


    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Pin Code:\t\t"+self.pincode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book Id:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Due Date:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book:\t\t"+self.daysonbok_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"Overdue Date:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Final Price:\t\t"+self.finalprice_var.get()+"\n\n")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="LibraryGui")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,PRN_No=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PinCode=%s,Mobile=%s,BookId=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,datedue=%s,dayonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_No=%s",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.pincode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbok_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        
        messagebox.showinfo("Success","Member has been Updated")
        
    
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="LibraryGui")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value= (self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been Deleted")



    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.pincode_var.set(""),
        self.bookid_var.set(""),
        self.mobile_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.datedue_var.set(""),
        self.daysonbok_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
    
    
    def iExit(self):

        iExit=tkinter.messagebox.askyesno("Library Management System","Do you wnat to Exit")
        if iExit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()