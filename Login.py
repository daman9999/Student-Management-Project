#Import Modules
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from Stu import Student
from Pass import Password



class Login:
    
    def __init__(self,root):

        self.root = root
        self.root.title("Login")
        self.root.geometry("350x350+450+200")
        self.root.resizable(0,0)

        

        self.username = StringVar()
        self.password = StringVar()

        

        title = Label(self.root,text="Login",bd = 5,relief=GROOVE,font=("Arial",30,"bold"),bg="#FFFCF9",fg="#0A090C")

        title.pack(side=TOP,fill=X)

        

        Main_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=0,y=60,width=350,height=290)

        

        lbl_username = Label(Main_Frame,text="Username :-",bg="#F0EDEE",fg="#0A090C",font=("Arial",10,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")

    

        txt_username = Entry(Main_Frame,textvariable=self.username,width = 12,font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_username.grid(row = 1,column=1,pady=45,padx=5,sticky="w")

        

        lbl_password = Label(Main_Frame,text="Password :-",bg="#F0EDEE",fg="#0A090C",font=("Arial",10,"bold"))

        lbl_password.grid(row = 2,column=0,pady=5,padx=30,sticky="w")

    

        txt_password = Entry(Main_Frame,show="*",textvariable=self.password,width = 12,font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_password.grid(row = 2,column=1,pady=5,padx=5,sticky="w")

        

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)

        

        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4",font=("Arial",10,"bold"),command=self.validate_user).grid(row=0,column=0,padx=0,pady=10)

        

    def validate_user(self):

        if self.username.get() == "" or self.password.get() == "":

            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()    
            curr.execute("SELECT * from admin")
            rows = curr.fetchall()


            for row in rows:
                print(row)
                if row[0] == self.username.get() and row[1] == self.password.get():

                    self.root.destroy() 
                    st_root = Tk()
                    st = Student(st_root)
                    st_root.mainloop()  

                else:

                    messagebox.showerror("Error","Please Make Sure That the Details are Correct")

              

             

root = Tk()
st = Login(root)
root.mainloop()