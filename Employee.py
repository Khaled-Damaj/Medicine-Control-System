from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from DbHandler import *

class Employee:

    def __init__(self, master):
        self.root = master
        self.student_table = None
        self.textarea = None
        self.employee_id_var = IntVar()
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.date_entry_var = StringVar()
        self.date_of_birth_var = StringVar()
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.salary_var = StringVar()
        self.address_var = StringVar()
        self.phone_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.date_of_birth = None
        self.date_entry = None
        self.initialize()

    def initialize(self):
        self.root.title("Employee Mangement System")
        self.root.configure(bg='white')
        root.state('zoomed')
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Employee", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # =================Product Frames=================

        F2 = LabelFrame(root, text='Employee System', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                        fg='#f5b7a6', bg='#a6b1f5')
        F2.place(x=10, y=80, width=520, height=620)

        role_title = Label(F2, text='Role', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        role_title.grid(row=1, column=0, padx=5, sticky='w', pady=10)
        role_combo = ttk.Combobox(F2, font=('times new romon', 13), textvariable=self.roll_var, width=20,
                                  state='readonly')
        role_combo.grid(row=1, column=1, padx=5, sticky='w', pady=10)
        role_combo['values'] = ('Admin', 'Employee')
        role_combo.current()

        name_title = Label(F2, text='Name', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        name_title.grid(row=2, column=0, padx=5, sticky='w', pady=10)
        name_entry = Entry(F2, width=22, font='arial 13', textvariable=self.name_var, relief=SUNKEN, bd=1)
        name_entry.grid(row=2, column=1, padx=5, sticky='w', pady=10)

        email_title = Label(F2, text='Email', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        email_title.grid(row=3, column=0, padx=5, sticky='w', pady=10)
        email_entry = Entry(F2, width=22, font='arial 13 ', textvariable=self.email_var, relief=SUNKEN, bd=1)
        email_entry.grid(row=3, column=1, padx=5, sticky='w', pady=10)

        gender_title = Label(F2, text='Gender', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        gender_title.grid(row=4, column=0, padx=5, sticky='w', pady=10)
        gender_combo = ttk.Combobox(F2, font=('times new romon', 13), textvariable=self.gender_var, width=20,
                                    state='readonly')
        gender_combo.grid(row=4, column=1, padx=5, sticky='w', pady=10)
        gender_combo['values'] = ('Male', 'Female')
        gender_combo.current()

        date_title = Label(F2, text='Date Entry', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        date_title.grid(row=5, column=0, padx=5, sticky='w', pady=10)
        self.date_entry = DateEntry(F2, font=('times new romon', 13),textvariable=self.date_entry_var,
                                    width=20, relief=SUNKEN,date_pattern='y-mm-dd')
        self.date_entry.grid(row=5, column=1, padx=5, sticky='w', pady=10)

        date_of_birth_title = Label(F2, text='D.O.B', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        date_of_birth_title.grid(row=6, column=0, padx=5, sticky='w', pady=10)
        self.date_of_birth = DateEntry(F2, font=('times new romon', 13),textvariable=self.date_of_birth_var,
                                           width=20,relief=SUNKEN,date_pattern='y-mm-dd')
        self.date_of_birth.grid(row=6, column=1, padx=5, sticky='w', pady=10)

        username_title = Label(F2, text='Username', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        username_title.grid(row=7, column=0, padx=5, sticky='w', pady=10)
        username_entry = Entry(F2, width=22, font='arial 13', textvariable=self.username_var, relief=SUNKEN, bd=1)
        username_entry.grid(row=7, column=1, padx=5, sticky='w', pady=10)

        password_title = Label(F2, text='Password', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        password_title.grid(row=8, column=0, padx=5, sticky='w', pady=10)
        password_entry = Entry(F2, width=22, font='arial 13', textvariable=self.password_var, relief=SUNKEN, bd=1,
                               show='*')
        password_entry.grid(row=8, column=1, padx=5, sticky='w', pady=10)

        salary_title = Label(F2, text='Salary', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        salary_title.grid(row=9, column=0, padx=5, sticky='w', pady=10)
        salary_entry = Entry(F2, width=22, font='arial 13', textvariable=self.salary_var, relief=SUNKEN, bd=1)
        salary_entry.grid(row=9, column=1, padx=5, sticky='w', pady=10)

        address_title = Label(F2, text='Address', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        address_title.grid(row=10, column=0, padx=5, sticky='w', pady=10)
        address_entry = Entry(F2, width=22, font='arial 13', textvariable=self.address_var, relief=SUNKEN, bd=1)
        address_entry.grid(row=10, column=1, padx=5, sticky='w', pady=10)

        phone_title = Label(F2, text='Phone', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        phone_title.grid(row=11, column=0, padx=5, sticky='w', pady=10)
        phone_entry = Entry(F2, width=22, font='arial 13', textvariable=self.phone_var, relief=SUNKEN, bd=1)
        phone_entry.grid(row=11, column=1, padx=5, sticky='w', pady=10)

        # =========================Buttons======================
        btn_frame = Frame(F2, bd=5, relief=RIDGE)
        btn_frame.place(x=18, y=510)

        add_btn = Button(btn_frame, text='Add', font='arial 12 bold', command=self.add_employee, bg='#c8a6f5',
                         fg='white',
                         width=8)
        add_btn.grid(row=0, column=0, padx=10, pady=10)
        update_btn = Button(btn_frame, text='Update', font='arial 12 bold', bg='#c8a6f5', width=8,
                            fg='white', command=self.update)
        update_btn.grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text='Delete', font='arial 12 bold', bg='#c8a6f5', width=8,
                            fg='white', command=self.delete)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame, text='Clear', font='arial 12 bold', command=self.clear, bg='#c8a6f5', width=8,
                           fg='white')
        clear_btn.grid(row=0, column=3, padx=10, pady=10)
        #

        # ========================Detail area================

        detail_frame = LabelFrame(root, text='Employee System', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.place(x=560, y=80, width=790, height=620)

        search_title = Label(detail_frame, text='Search By', font=('times new romon', 15, 'bold'), bg='#a6b1f5')
        search_title.grid(row=0, column=0, padx=5, sticky='w', pady=10)
        search_combo = ttk.Combobox(detail_frame, textvariable=self.search_by, font=('times new romon', 14),
                                    width=15, state='readonly')
        search_combo.grid(row=0, column=1, padx=5, sticky='w', pady=10, ipadx=2)
        search_combo['values'] = ('Role_Name', 'Employee_Name', 'Phone_Number', 'Email')
        search_combo.current()

        search_entry = Entry(detail_frame, textvariable=self.search_text, width=15, font='arial 15', relief=SUNKEN,
                             bd=1)
        search_entry.grid(row=0, column=2, padx=5, sticky='w', pady=10)

        search_btn = Button(detail_frame, text='Search', font='arial 12 bold', bg='#c8a6f5',
                            width=8, fg='white', command=self.search_data)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(detail_frame, text='Show All', font='arial 12 bold', bg='#c8a6f5',
                             width=8, fg='white', command=self.fetch_data)
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        # ========================Table area================

        table_frame = Frame(detail_frame, relief=RIDGE, bd=5, bg='#eeeeee')
        table_frame.place(x=10, y=65, width=750, height=500)

        scrol_y = Scrollbar(table_frame, orient=VERTICAL)
        scrol_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            'ID', 'Employee_Name', 'Role', 'Username', 'Password', 'Gender', 'Email', 'Address', 'Phone_Number',
            'Salary', 'Date of Birth', 'Joining Date'), xscrollcommand=scrol_x, yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('ID', text='ID')
        self.student_table.heading('Employee_Name', text='Employee_Name')
        self.student_table.heading('Role', text='Role')
        self.student_table.heading('Username', text='Username')
        self.student_table.heading('Password', text='Password')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Phone_Number', text='Phone_Number')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Date of Birth', text='Date of Birth')
        self.student_table.heading('Joining Date', text='Joining Date')
        self.student_table.heading('Salary', text='Salary')

        self.student_table['show'] = 'headings'
        self.student_table.column('ID', width=50)
        self.student_table.column('Employee_Name', width=100)
        self.student_table.column('Role', width=100)
        self.student_table.column('Username', width=100)
        self.student_table.column('Password', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Phone_Number', width=100)
        self.student_table.column('Address', width=100)
        self.student_table.column('Email', width=200)
        self.student_table.column('Date of Birth', width=100)
        self.student_table.column('Joining Date', width=100)
        self.student_table.column('Salary', width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_employee(self):

        if self.name_var.get() == '' and self.roll_var.get() == '' and self.username_var.get() == '' and self.gender_var.get() == '' and self.email_var.get() == '' and self.address_var.get() == '' and self.phone_var.get() == '' and self.salary_var.get() == '' and self.date_of_birth_varget() == '' and self.date_entry_var.get() == '' and self.password_var.get() == '':
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            cur = conn.cursor()
            cur.execute(
                "Insert into Employee (Employee_Name,Role_Name,Employee_Username,Employee_Password,Gender,Email,Address,Phone_Number,Salary,DOB,"
                "Joining_Date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.name_var.get(),
                                                                           self.roll_var.get(),
                                                                           self.username_var.get(),
                                                                           self.password_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.email_var.get(),
                                                                           self.address_var.get(),
                                                                           self.phone_var.get(),
                                                                           self.salary_var.get(),
                                                                           self.date_of_birth.get_date(),
                                                                           self.date_entry.get_date()))

            conn.commit()
            messagebox.showinfo("Success", "Record has been inserted successfully")
            cur.execute(
                "Insert into Login (Role_Name,Employee_Username,Employee_Password) values(%s,%s,%s)", (
                    self.roll_var.get(),
                    self.username_var.get(),
                    self.password_var.get()))
            self.fetch_data()

            self.clear()

    def fetch_data(self):
        cur = conn.cursor()
        cur.execute("select* from Employee")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()
            print()

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.employee_id_var.set([row[0]])
        self.name_var.set(row[1])
        self.roll_var.set(row[2])
        self.username_var.set(row[3])
        self.password_var.set(row[4])
        self.gender_var.set(row[5])
        self.email_var.set(row[6])
        self.address_var.set(row[7])
        self.phone_var.set(row[8])
        self.salary_var.set(row[9])
        self.date_of_birth_var.set(row[10])
        self.date_entry_var.set(row[11])

    def clear(self):
        self.name_var.set('')
        self.gender_var.set('')
        self.date_entry_var.set('')
        self.date_of_birth_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.password_var.set('')
        self.address_var.set('')
        self.username_var.set('')
        self.salary_var.set('')
        self.roll_var.set('')

    def update(self):
        cur = conn.cursor()
        cur.execute(
            "update Employee set Employee_Name=%s,Role_Name=%s,Employee_Password=%s,Gender=%s,Email=%s,Address=%s,Phone_Number=%s,Salary=%s,"
            "DOB=%s,Joining_Date=%s where Employee_ID=%s and Employee_Username=%s ",
            (self.name_var.get(),
             self.roll_var.get(),
             self.password_var.get(),
             self.gender_var.get(),
             self.email_var.get(),
             self.address_var.get(),
             self.phone_var.get(),
             self.salary_var.get(),
             self.date_of_birth.get_date(),
             self.date_entry.get_date(),
             self.employee_id_var.get(),
             self.username_var.get()))

        conn.commit()
        messagebox.showinfo("Success", "Record has been updated successfully")
        self.fetch_data()
        self.clear()

    def delete(self):
        cur = conn.cursor()
        cur.execute("DELETE FROM Employee WHERE where Employee_ID=%s and Employee_Username=%s ",
            (self.employee_id_var.get(),
             self.username_var.get()))
        conn.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully")
        self.fetch_data()

    def search_data(self):
        cur = conn.cursor()
        cur.execute("select* from Employee where %s" % self.search_by.get() + " LIKE '%s'" % self.search_text.get())
        rows = cur.fetchall()
        print(rows)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()


if __name__ == '__main__':
    root = Tk()
    gui = Employee(root)
    root.mainloop()
