#Import Modules
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

from Pass import Password


class Department:

    def __init__(self,root):
        self.root = root
        self.root.title("C Student Management System")
        self.root.geometry("1350x700+0+0")

       
        title = Label(self.root,text=" Student Management System",bd = 10,
        relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        

        #Variables
        self.dept_id = StringVar()
        self.dept_name = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

       
        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)

                

        m_title = Label(Manage_Frame,text="Manage Department",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))
        m_title.grid(row = 0,columnspan=2,pady=20)

        

        lbl_dept_id = Label(Manage_Frame,text="Department ID -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_dept_id.grid(row = 1,column=0,pady=30,padx=100)

    

        txt_dept_id = Entry(Manage_Frame,textvariable=self.dept_id,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dept_id.grid(row = 2,column=0,pady=10,padx=100)

        

        lbl_name = Label(Manage_Frame,text="Department Name -",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 3,column=0,pady=30,padx=100)

    
        txt_name = Entry(Manage_Frame,textvariable=self.dept_name,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row = 4,column=0,pady=10,padx=100)

        
        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=420,width=410) 

        

        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.add_department).grid(row=0,column=0,padx=5,pady=10)

        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",
        font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",     font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        
        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)

       
        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout).grid(row=0,column=7,padx=690,pady=10)

        

        #Table Frame
        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)

        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Table = ttk.Treeview(Table_Frame,columns=("DEPT-ID","Department Name")
        ,xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)

        Y_scroll.pack(side=RIGHT,fill=Y)

        X_scroll.config(command=self.Table.xview)

        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("DEPT-ID",text="DEPT-ID")

        self.Table.heading("Department Name",text="Department Name")

            

        

        self.Table['show']="headings"

        self.Table.column("DEPT-ID",width=100)

        self.Table.column("Department Name",width=100)



        self.Table.pack(fill=BOTH,expand=1)

        self.Table.bind('<ButtonRelease 1>',self.get_fields)

        self.show_data()

        

    def add_department(self):
        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

 
            curr.execute("INSERT INTO DEPARTMENT VALUES(%s,%s)",(self.dept_id.get(),

                                                                 self.dept_name.get(),

                                                                ))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Success","Record Successfully Added")

        

    def show_data(self):
        connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
        curr = connect.cursor()

        

        curr.execute("SELECT * from department")
        rows = curr.fetchall()

        if(len(rows)!=0):
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=row)
            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            self.dept_id.set("")
            self.dept_name.set("")


    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        self.dept_id.set(row[0])
        self.dept_name.set(row[1])
   

    def update(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            

            curr.execute("UPDATE Department SET name=%s where dept_id=%s",
            (self.dept_name.get(),self.dept_id.get()))

            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Updated")

        
    def delete(self):

        if self.dept_id.get() == "" or self.dept_name.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            

            curr.execute("DELETE from DEPARTMENT where dept_id=%s",(self.dept_id.get()))


            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Deleted")
      

    def logout(self):
        from Login import Login
        self.root.destroy() 
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

        

    def pass_btn(self):
        from Pass import Password
        self.root.destroy() 
        st_root = Tk()
        st = Password(st_root)
        st_root.mainloop()
