#Import Modules
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox





class Password:

    def __init__(self,root):

        self.root = root
        self.root.title(" Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text=" Student Management System",bd = 10,
                relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        
        #Variables
        self.username = StringVar()
        self.old_password = StringVar()
        self.new_password = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=1250,height=600)

               
        m_title = Label(Manage_Frame,text="Change Password",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))

        m_title.grid(row = 0,columnspan=2,pady=20,padx=450)

        
        lbl_username = Label(Manage_Frame,text="Username -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_username.grid(row = 1,column=0,pady=10,padx=500)

    

        txt_dept_id = Entry(Manage_Frame,textvariable=self.username,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dept_id.grid(row = 2,column=0,pady=10,padx=500)

        

        lbl_name = Label(Manage_Frame,text="Old Password -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 3,column=0,pady=10,padx=500)

    

        txt_name = Entry(Manage_Frame,show="*",textvariable=self.old_password,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 4,column=0,pady=10,padx=500)

        

        lbl_name = Label(Manage_Frame,text="New Password -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 5,column=0,pady=10,padx=500)

    

        txt_name = Entry(Manage_Frame,show="*",textvariable=self.new_password,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 6,column=0,pady=10,padx=500)
        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=400,y=420,width=410) 

        
        chg_btn = Button(btn_frame,text="Change Password",bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),relief=GROOVE,width=30,command=self.change_pass).grid(row=0,column=0,padx=90,pady=10,ipady=4)

       
                         

    def change_pass(self):

        if self.username.get() == "" or self.old_password.get() == "" or self.new_password.get() == "":
            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            
            curr.execute("SELECT * from admin")
            rows = curr.fetchall()

            
            for row in rows:
                if row[0] == self.username.get() and row[1] == self.old_password.get():
                    connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
                    curr = connect.cursor()

                    

                    curr.execute("UPDATE ADMIN SET password=%s where username=%s",
                    (self.new_password.get(),self.username.get()))

                    connect.commit()
                    connect.close()
                    messagebox.showinfo("Success","Password Updated Successsfully")
                else:
                    messagebox.showerror("Error","Please Make Sure That the Details are Correct")

         

    def logout(self):

        self.root.destroy()
        from Login import Login 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

       
    def student_btn(self):
        from Stu import Student
        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()

       
    def employee_btn(self):
        from Emp import Employee
        self.root.destroy() 
        st_root = Tk()
        st = Employee(st_root)
        st_root.mainloop()

      
    def dept_btn(self):
        from Dept import Department
        self.root.destroy()
        st_root = Tk()
        st = Department(st_root)
        st_root.mainloop()
