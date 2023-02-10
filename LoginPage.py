import subprocess
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image
from tkmacosx import Button


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('LIBRARY MANAGEMENT SYSTEM')

        # ============================background image============================
        self.bg_frame = Image.open('/Users/aditya/Programs/Python/DBMS_Project_GUI/LoginPage/images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================

        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('/Users/aditya/Programs/Python/DBMS_Project_GUI/LoginPage/images/vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('/Users/aditya/Programs/Python/DBMS_Project_GUI/LoginPage/images/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=663, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        username=StringVar()
        password=StringVar()
        
        
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame,textvariable=username, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('/Users/aditya/Programs/Python/DBMS_Project_GUI/LoginPage/images/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 1, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame,textvariable=password, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 14, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('/Users/aditya/Programs/Python/DBMS_Project_GUI/LoginPage/images/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        
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

        Button(self.lgn_frame,text="Login",height=50,width=100,bg="#ed3833",fg="white",borderless=1,command=login).place(x=570,y=470)
#==================================================================================================================================================================

        def Exit():
            Exit=tkinter.messagebox.askyesno("Library Management System","Do you wnat to Exit")
            if Exit>0:
                quit()
                    
        Button(self.lgn_frame,text="Exit",height=50,width=100,bg="#ed3833",fg="white",borderless=1,command=Exit).place(x=750,y=470)
        
        
        
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()