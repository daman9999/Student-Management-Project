#Import Modules
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from Emp import Employee




class Student:
    
    def __init__(self,root):
        self.root = root
        self.root.title(" Student Management System")
        self.root.geometry("1350x700+0+0")

        

        title = Label(self.root,text=" Student Management System"
        ,bd = 10,relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")

        title.pack(side=TOP,fill=X)

        

        #Variables
        self.roll_no = StringVar()
        self.name = StringVar()
        self.email_id = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.address = StringVar()

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        manage_employee_btn = Button(Dash_Frame,bg="#00A1E4",fg="#F0EDEE",text="Employee",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        department_btn = Button(Dash_Frame,text="Department",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)

                

        m_title = Label(Manage_Frame,text="Manage Student",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold","italic"))
        m_title.grid(row = 0,columnspan=2,pady=20)

        

        lbl_roll = Label(Manage_Frame,text="Roll No.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_roll.grid(row = 1,column=0,pady=10,padx=20,sticky="w")

    

        txt_Roll = Entry(Manage_Frame,textvariable=self.roll_no,font=("Arial",15,"bold"),
        bd=5,relief=GROOVE)
        txt_Roll.grid(row = 1,column=1,pady=10,padx=20,sticky="w")

        

        lbl_name = Label(Manage_Frame,text="Name.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_name.grid(row = 2,column=0,pady=10,padx=20,sticky="w")

    

        txt_name = Entry(Manage_Frame,textvariable=self.name,font=("Arial",15,"bold"),
        bd=5,relief=GROOVE)
        txt_name.grid(row = 2,column=1,pady=10,padx=20,sticky="w")

        

        lbl_email = Label(Manage_Frame,text="Email-ID.",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_email.grid(row = 3,column=0,pady=10,padx=20,sticky="w")

    

        txt_email = Entry(Manage_Frame,textvariable=self.email_id,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row = 3,column=1,pady=10,padx=20,sticky="w")

        

        lbl_gender = Label(Manage_Frame,text="Gender",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_gender.grid(row = 4,column=0,pady=10,padx=20,sticky="w")

        

        gender_box = ttk.Combobox(Manage_Frame,textvariable=self.gender,
        font=("Arial",13,"bold"),state="readonly")

        gender_box['values'] = ("Male","Female","Other")
        gender_box.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        

        lbl_contact = Label(Manage_Frame,text="Contact",bg="#F0EDEE",fg="black", 
        font=("Arial",15,"bold"))
        lbl_contact.grid(row = 5,column=0,pady=10,padx=20,sticky="w")

    

        txt_contact = Entry(Manage_Frame,textvariable=self.contact,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row = 5,column=1,pady=10,padx=20,sticky="w")

        

        lbl_DOB = Label(Manage_Frame,text="D.O.B",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_DOB.grid(row = 6,column=0,pady=10,padx=20,sticky="w")

    

        self.txt_DOB = Entry(Manage_Frame,textvariable=self.dob,font=("Arial",15,"bold")
        ,bd=5,relief=GROOVE)
        self.txt_DOB.grid(row = 6,column=1,pady=10,padx=20,sticky="w")

        

        

        lbl_address = Label(Manage_Frame,text="Address",bg="#F0EDEE",fg="black",
        font=("Arial",15,"bold"))
        lbl_address.grid(row = 7,column=0,pady=10,padx=20,sticky="w")

    

        self.txt_address = Text(Manage_Frame,bd=2,relief=RIDGE,width =30,height=4)
        self.txt_address.grid(row = 7,column=1,pady=10,padx=20,sticky="w")

        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=520,width=410) 

        

        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)

        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)

        

        lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        font=("Arial",18,"bold"))
        lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        font=("Arial",13,"bold"),state="readonly")

        search_box['values'] = ("Roll_No","SName","Contact_No")
        search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,font=("Arial",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        search_btn = Button(Detail_Frame,text="Search",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        show_all_btn = Button(Detail_Frame,text="Show All",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Roll-No","Name","Email-ID",
        "Gender","D.O.B","Address","Contact No"),xscrollcommand=X_scroll.set,
        yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Roll-No",text="Roll-No")
        self.Table.heading("Name",text="Name")
        self.Table.heading("Email-ID",text="Email-ID")
        self.Table.heading("Gender",text="Gender")
        self.Table.heading("Contact No",text="Contact No")
        self.Table.heading("D.O.B",text="D.O.B")
        self.Table.heading("Address",text="Address")

        

        self.Table['show']="headings"
        self.Table.column("Roll-No",width=100)
        self.Table.column("Name",width=100)
        self.Table.column("Email-ID",width=100)
        self.Table.column("Gender",width=100)
        self.Table.column("Contact No",width=100)
        self.Table.column("D.O.B",width=100)
        self.Table.column("Address",width=150)

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        self.txt_DOB.bind("<FocusIn>", self.foc_in)
        self.txt_DOB.bind("<FocusOut>", self.foc_out)


        self.put_placeholder()
        self.show_data()

        

    def add_student(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            

            curr.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.roll_no.get(), self.name.get(), self.email_id.get(), self.gender.get(),self.dob.get(), self.txt_address.get('1.0',END), self.contact.get() ))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
        curr = connect.cursor()

        

        curr.execute("SELECT * from student")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=row)

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == ""  or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields Empty")

        else:

            self.roll_no.set("")
            self.name.set("")
            self.email_id.set("")
            self.gender.set("")
            self.contact.set("")
            self.dob.set("")
            self.txt_address.delete("1.0",END)

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        

        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.email_id.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[6])
        self.dob.set(row[4])

        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[5])

        

    def update(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == ""  or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            

            curr.execute('''UPDATE STUDENT SET Sname=%s,email_id=%s,gender=%s,dob=%s,address=%s,contact_no=%s where roll_no=%s",(self.name.get(),

                                                         self.email_id.get(),

                                                         self.gender.get(),

                                                         self.dob.get(),

                                                         self.txt_address.get('1.0',END),

                                                         self.contact.get(),

                                                         self.roll_no.get()

                                                        )''')

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == ""  or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:
            
            connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
            curr = connect.cursor()

            

            curr.execute("DELETE from STUDENT where roll_no=%s",(self.roll_no.get()))

                                                                             

            

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:
            
           connect = pymysql.connect(host="localhost",user="root",password="",database="Student_Management")
           curr = connect.cursor()
           
           curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                        " LIKE '%"+str(self.search_field.get())+"%'")
          
           print( curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                        " LIKE '%"+str(self.search_field.get())+"%'"))
          
           rows = curr.fetchall()
           if(len(rows)!=0):
           
               self.Table.delete(*self.Table.get_children())
               for row in rows:
                   self.Table.insert('',END,values=row)
               connect.commit()
           connect.close()
 

               

        


            

    def put_placeholder(self):

        self.txt_DOB.insert(0,"DD-MM-YYYY")

        self.txt_DOB['fg'] = "grey"


    def foc_in(self,event):

        if self.txt_DOB['fg'] == "grey":

            self.txt_DOB.delete('0', 'end')
            self.txt_DOB['fg'] = "grey"


    def foc_out(self, event):

        if not self.txt_DOB.get():
            self.txt_DOB.put_placeholder()

            

    def logout(self):
        from Login import Login
        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
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

        

    def pass_btn(self):
        from Pass import Password
        self.root.destroy() 

        st_root = Tk()
        st = Password(st_root)
        st_root.mainloop()
