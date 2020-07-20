from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        # window name
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        # top label , bg = background color, fg = text color, bd = border
        title = Label(self.root, text = "Student Management System",  bd = 8, relief = GROOVE, font = ("times new roman", 40, "bold"), bg = "white", fg = "black")
        title.pack(side = TOP, fill = X)   

        #variables name for entry
        self.Roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.branch_var = StringVar()
        self.searchby_var = StringVar()
        self.identity_var = StringVar()

   # left frame(entry section)
        leftframe = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        leftframe.place(x = 110, y = 100, width = 550, height = 800)
        
        # left frame title
        lefttitle = Label(leftframe, text = "Manage Students",bg = "white", font = ("times new roman", 28, "bold"))
        lefttitle.grid(row = 0, columnspan=2, pady=20)

         # roll number
        lbl_roll = Label(leftframe, text = "Roll Number",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_roll.grid(row = 1, column = 0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(leftframe, textvariable = self.Roll_no_var, bg = "white", font = ("times new roman", 20, "bold"), bd = 5, relief=GROOVE)
        txt_roll.grid(row = 1, column = 1, pady=10, padx=20, sticky="w")

        # name
        lbl_name = Label(leftframe, text = "Name",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_name.grid(row = 2, column = 0, pady=10, padx=20, sticky="w")

        txt_name = Entry(leftframe, textvariable = self.name_var, bg = "white", font = ("times new roman", 20, "bold"), bd = 6, relief=GROOVE)
        txt_name.grid(row = 2, column = 1, pady=10, padx=20, sticky="w")
        
        # email
        lbl_email = Label(leftframe, text = "Email id",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_email.grid(row = 3, column = 0, pady=10, padx=20, sticky="w")

        txt_email = Entry(leftframe, textvariable = self.email_var, bg = "white", font = ("times new roman", 20, "bold"), bd = 5, relief=GROOVE)
        txt_email.grid(row = 3, column = 1, pady=10, padx=20, sticky="w")
       
        #gender using combobox
        lbl_sex = Label(leftframe, text = "Sex",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_sex.grid(row = 4, column = 0, pady=10, padx=20, sticky="w")

        combo_sex = ttk.Combobox(leftframe, textvariable = self.gender_var, font=("times new roman",20,"bold"), state="WHITE")
        combo_sex['values'] = ("male", "female", "other")
        combo_sex.grid(row = 4, column = 1, pady=10, padx=20, sticky="w")

       #contact
        lbl_contact = Label(leftframe, text = "Contact",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_contact.grid(row = 5, column = 0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(leftframe, textvariable = self.contact_var, bg = "white", font = ("times new roman", 20, "bold"), bd = 5, relief=GROOVE)
        txt_contact.grid(row = 5, column = 1, pady=10, padx=20, sticky="w")

       #DOB
        lbl_dob = Label(leftframe, text = "DOB",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_dob.grid(row = 6, column = 0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(leftframe,bg = "white", textvariable = self.dob_var, font = ("times new roman", 20, "bold"), bd = 5, relief=GROOVE)
        txt_dob.grid(row = 6, column = 1, pady=10, padx=20, sticky="w")

      #branch Text
        lbl_branch = Label(leftframe, text = "Branch",bg = "white", font = ("times new roman", 20, "bold"))
        lbl_branch.grid(row = 7, column = 0, pady=10, padx=20, sticky="w")

        combo_branch = ttk.Combobox(leftframe, textvariable = self.branch_var, font=("times new roman",20,"bold"), state="WHITE")
        combo_branch['values'] = ("Computer Science", "Information Technology", "Electronics")
        combo_branch.grid(row = 7, column = 1, pady=10, padx=20, sticky="w")
     
      #buttons
        addbtn = Button(leftframe, text = "Add", width=15, command = self.add_students).grid(row = 10, column = 0, padx=10,pady=10)
        updatebtn = Button(leftframe, text = "Update", width=15, command = self.update).grid(row = 10, column = 1, padx=10,pady=10)
        deletebtn = Button(leftframe, text = "Delete", width=15, command = self.delete).grid(row = 11, column = 0, padx=10,pady=10)
        clearbtn = Button(leftframe, text = "Clear", width=15, command = self.clear).grid(row = 11, column = 1, padx=10,pady=10)
       
   


   # right frame(detail section)
        rightframe = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        rightframe.place(x = 730, y = 100, width = 1050, height = 800)

     # search by
        lbl_seach = Label(rightframe, text = "Search By", bg = "white", font = ("times new roman", 20, "bold"))
        lbl_seach.grid(row = 0, column = 0, pady=10, padx=20, sticky="w")
        
        # combo_search   
        combo_search = ttk.Combobox(rightframe, textvariable = self.searchby_var, font=("times new roman",15,"bold"), state="WHITE")
        combo_search['values'] = ("Roll_number", "Name", "Contact")
        combo_search.grid(row = 0, column = 1, pady=10, padx=20, sticky="w")
        
        # text_search
        txt_search = Entry(rightframe, textvariable = self.identity_var, bg = "white", font = ("times new roman", 20, "bold"), bd = 5, relief=GROOVE)
        txt_search.grid(row = 0, column = 2, pady=10, padx=20, sticky="w")
        
        # buttons , search, showall
        searchbtn = Button(rightframe, text = "Search", width=12, command = self.searchby).grid(row = 0, column = 3, padx=10,pady=10)
        showallbtn = Button(rightframe, text = "Show all", width=12, command = self.fetch_data).grid(row = 0, column = 4, padx=10,pady=10)

    
    # Table Frame
        tableframe = Frame(rightframe, bd = 4, relief = RIDGE, bg = "white")
        tableframe.place(x = 15, y = 80, width = 1010, height = 690)

        scroll_x = Scrollbar(tableframe, orient = HORIZONTAL)
        scroll_y = Scrollbar(tableframe, orient = VERTICAL)
        self.studenttable = ttk.Treeview(tableframe, columns = ("Roll Number", "Name", "Email", "Sex", "Contact", "DOB", "Branch"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set )
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.studenttable.xview)
        scroll_y.config(command = self.studenttable.yview)
        self.studenttable.heading("Roll Number", text = "Roll No")
        self.studenttable.heading("Name", text = "Name")
        self.studenttable.heading("Email", text = "Email")
        self.studenttable.heading("Sex", text = "Sex")
        self.studenttable.heading("Contact", text = "Contact")
        self.studenttable.heading("DOB", text = "DOB")
        self.studenttable.heading("Branch", text = "Branch")
        self.studenttable['show'] = 'headings'
        self.studenttable.column("Roll Number", width = 140)
        self.studenttable.column("Name", width = 300)
        self.studenttable.column("Email", width = 200)
        self.studenttable.column("Sex", width = 140)
        self.studenttable.column("Contact", width = 140)
        self.studenttable.column("DOB", width = 140)
        self.studenttable.column("Branch", width = 140)
        
        self.studenttable.pack(fill = BOTH, expand = 1)
        # fetch data to table
        self.fetch_data()
        # bind cursor
        self.studenttable.bind("<ButtonRelease-1>", self.get_cursor)

 # connections for entry section
        #add button connection
    def add_students(self):
          if self.Roll_no_var.get() == "" or self.name_var.get() == "" or self.contact_var.get() == "" or self.gender_var.get() == "" or self.dob_var.get() == "" or self.branch_var.get() == "" or self.email_var.get() == "":
            messagebox.showerror("Error", "All Fields are required")
          else:
            con = pymysql.connect(host = "localhost", user = "root", password = "password", database = "stm")
            cur = con.cursor()
            cur.execute("insert into Students_info values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_no_var.get(), 
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.branch_var.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

        # fetch data to rightframe table
    def fetch_data(self):
         con = pymysql.connect(host = "localhost", user = "root", password = "password", database = "stm")
         cur = con.cursor()
         cur.execute("select * from Students_info")
         rows = cur.fetchall()
         if len(rows) != 0:
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
               self.studenttable.insert('',END,values=row)
            con.commit()
         con.close()
        
        # clear entry inleft frame
    def clear(self):
      self.Roll_no_var.set("")
      self.name_var.set("")
      self.email_var.set("")
      self.gender_var.set("")
      self.contact_var.set("")
      self.dob_var.set("")
      self.branch_var.set("")
        
        # fetch a row table rightframe table to entry section
    def get_cursor(self, ev):
      cursor_row = self.studenttable.focus()
      contents = self.studenttable.item(cursor_row)
      row = contents['values']
      self.Roll_no_var.set(row[0])
      self.name_var.set(row[1])
      self.email_var.set(row[2])
      self.gender_var.set(row[3])
      self.contact_var.set(row[4])
      self.dob_var.set(row[5])
      self.branch_var.set(row[6])
    
       # update students info
    def update(self):
      con = pymysql.connect(host = "localhost", user = "root", password = "password", database = "stm")
      cur = con.cursor()
      cur.execute("update Students_info set Name = %s, Email = %s, Sex = %s, Contact = %s, DOB = %s, Branch = %s where Roll_Number = %s",
      (
          self.name_var.get(),
          self.email_var.get(),
          self.gender_var.get(),
          self.contact_var.get(),
          self.dob_var.get(),
          self.branch_var.get(),
          self.Roll_no_var.get()
          ))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()

      #delete student
    def delete(self):
      con = pymysql.connect(host = "localhost", user = "root", password = "password", database = "stm")
      cur = con.cursor()
      cur.execute("delete from Students_info where Roll_number = %s", self.Roll_no_var.get())
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()

      # search student 
    def searchby(self):
      con = pymysql.connect(host = "localhost", user = "root", password = "password", database = "stm")
      cur = con.cursor()
      cur.execute("select * from Students_info where " + self.searchby_var.get() + " = " + self.identity_var.get())
      rows = cur.fetchall()
      if len(rows) != 0:
        self.studenttable.delete(*self.studenttable.get_children())
        for row in rows:
            self.studenttable.insert('',END,values=row)
        con.commit()
      con.close()

root = Tk()
ob = Student(root)
root.mainloop()
