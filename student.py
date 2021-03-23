from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("1350x800+0+0")
        title=Label(self.root,text="student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #=========all variables========
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #==========manage frame===========
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=100,width=450,height=700)

        m_title = Label(manage_frame, text="manage students",
                      font=("times new roman", 30, "bold"), bg="crimson", fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(manage_frame, text="roll no.",
                        font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_roll.grid(row=1, column=0,padx=10, pady=20,sticky="w")

        txt_roll=Entry(manage_frame,textvariable=self.roll_no_var,font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1,padx=10, pady=20,sticky="w")

        lbl_name = Label(manage_frame, text="name",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, padx=10, pady=20, sticky="w")

        txt_name = Entry(manage_frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=10, pady=20, sticky="w")

        lbl_email = Label(manage_frame, text="email",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_email.grid(row=3, column=0, padx=10, pady=20, sticky="w")

        txt_email = Entry(manage_frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=10, pady=20, sticky="w")

        lbl_gender = Label(manage_frame, text="gender",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_gender.grid(row=4, column=0, padx=10, pady=20, sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,
                         font=("times new roman", 13, "bold"),state="readonly")
        combo_gender['values']=("male","female","others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(manage_frame, text="contact",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_contact.grid(row=5, column=0, padx=10, pady=20, sticky="w")

        txt_contact = Entry(manage_frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, padx=10, pady=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B.",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_dob.grid(row=6, column=0, padx=10, pady=20, sticky="w")

        txt_dob = Entry(manage_frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=10, pady=20, sticky="w")

        lbl_address = Label(manage_frame, text="address",
                         font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_address.grid(row=7, column=0, padx=10, pady=20, sticky="w")

        self.txt_address=Text(manage_frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #=========button frame======
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_frame.place(x=10, y=632, width=430)

        addbtn=Button(btn_frame,text="add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame, text="update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



        #=========detail_frame=============
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=100,width=800,height=700)

        lbl_search = Label(detail_frame, text="search by",
                            font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        lbl_search.grid(row=0, column=0, padx=10, pady=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame,textvariable=self.search_by,
                                    font=("times new roman", 13, "bold"),width=10, state="readonly")
        combo_search['values'] = ("roll_no", "name", "contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(detail_frame,width=20,textvariable=self.search_txt, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=10, pady=20, sticky="w")

        searchbtn = Button(detail_frame, text="search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(detail_frame, text="show all", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        #=========table frame=========
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="roll")
        self.student_table.heading("name", text="name")
        self.student_table.heading("email", text="email")
        self.student_table.heading("gender", text="gender")
        self.student_table.heading("contact", text="contact")
        self.student_table.heading("dob", text="dob")
        self.student_table.heading("address", text="address")
        self.student_table['show']='headings'
        self.student_table.column("roll")
        self.student_table.column("name")
        self.student_table.column("email")
        self.student_table.column("gender")
        self.student_table.column("contact")
        self.student_table.column("dob")
        self.student_table.column("address")
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("error","all feilds are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                             self.name_var.get(),
                                                                             self.email_var.get(),
                                                                             self.gender_var.get(),
                                                                             self.contact_var.get(),
                                                                             self.dob_var.get(),
                                                                             self.txt_address.get('1.0',END)
                                                                             ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","record has been inserted successfully")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        print(row)
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                                                                         (self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_address.get('1.0', END),
                                                                          self.roll_no_var.get()
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=student(root)
root.mainloop()