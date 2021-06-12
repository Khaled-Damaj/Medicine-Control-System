from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DbHandler import *
from tkinter import filedialog


class Company:

    def __init__(self, master):
        self.company_id_var = IntVar()
        self.root = master
        self.student_table = None
        self.textarea = None
        self.company_name_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.phone_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.initialize()

    def initialize(self):
        self.root.title("Sale Point")
        self.root.configure(bg='white')
        root.state('zoomed')
        self.display()

    def display(self, companyname=None, company_id=None):
        # =================Title=================
        title = Label(root, pady=2, text="Patient", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # =================Product Frames=================

        F2 = LabelFrame(root, text='Company System', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                        fg='#f5b7a6', bg='#a6b1f5')
        F2.place(x=10, y=80, width=520, height=520)

        companyname_title = Label(F2, text='Company Name', font=('times new romon', 15, 'bold'), bg='#a6b1f5')
        companyname_title.grid(row=0, column=0, padx=5, sticky='w', pady=20)
        companyname_entry = Entry(F2, width=22, font='arial 15', textvariable=self.company_name_var , relief=SUNKEN, bd=1)
        companyname_entry.grid(row=0, column=1, padx=5, sticky='w', pady=20)

        company_email_title = Label(F2, text='Email', font=('times new romon', 15, 'bold'), bg='#a6b1f5')
        company_email_title.grid(row=1, column=0, padx=5, sticky='w', pady=20)
        company_email_entry = Entry(F2, width=22, font='arial 15', textvariable=self.email_var, relief=SUNKEN, bd=1)
        company_email_entry.grid(row=1, column=1, padx=5, sticky='w', pady=20)

        company_email_address_title = Label(F2, text='Address', font=('times new romon', 15, 'bold'), bg='#a6b1f5')
        company_email_address_title.grid(row=2, column=0, padx=5, sticky='w', pady=20)
        company_email_address_entry = Entry(F2, width=22, font='arial 15', textvariable=self.address_var, relief=SUNKEN, bd=1)
        company_email_address_entry.grid(row=2, column=1, padx=5, sticky='w', pady=20)

        company_phone_title = Label(F2, text='Phone Number', font=('times new romon', 15, 'bold'), bg='#a6b1f5')
        company_phone_title.grid(row=3, column=0, padx=5, sticky='w', pady=20)
        company_phone_entry = Entry(F2, width=22, font='arial 15', textvariable=self.phone_var, relief=SUNKEN, bd=1)
        company_phone_entry.grid(row=3, column=1, padx=5, sticky='w', pady=20)

        # =========================Buttons======================
        btn_frame = Frame(F2, bd=5, relief=RIDGE)
        btn_frame.place(x=25, y=330)

        add_btn = Button(btn_frame, text='Add', font='arial 12 bold',command=self.add_company,bg='#c8a6f5',
                         fg='white', width=8)
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

        # ========================Detail area================

        detail_frame = LabelFrame(root, text='Company Detail', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.place(x=560, y=80, width=790, height=620)

        search_title = Label(detail_frame, text='Search By', font=('arial', 14, 'bold'), bg='#a6b1f5')
        search_title.grid(row=0, column=0, padx=5, sticky='w', pady=10)
        search_combo = ttk.Combobox(detail_frame, textvariable=self.search_by, font=('times new romon', 13),
                                    width=15, state='readonly')
        search_combo.grid(row=0, column=1, padx=5, sticky='w', pady=10, ipadx=2)
        search_combo['values'] = ('CompanyName', 'Email ', 'Address', 'PhoneNumber')
        search_combo.current()

        search_entry = Entry(detail_frame, textvariable=self.search_text, width=15, font='arial 14', relief=SUNKEN,
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
            'ID', 'CompanyName', 'Email', 'Address', 'Phone_Number',), xscrollcommand=scrol_x,
                                          yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('ID', text='ID')
        self.student_table.heading('CompanyName', text='Company Name')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Phone_Number', text='Phone Number')

        self.student_table['show'] = 'headings'
        self.student_table.column('ID', width=10)
        self.student_table.column('CompanyName', width=50)
        self.student_table.column('Email', width=100)
        self.student_table.column('Address', width=50)
        self.student_table.column('Phone_Number', width=50)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        #====================================================================================

    def add_company(self):

        if self.company_name_var.get() == '' or self.address_var.get()=='':
            messagebox.showerror("Error", "All fields are required to fill")
        elif self.phone_var.get() == '' or self.email_var == '':
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            cur = conn.cursor()
            cur.execute(
                "Insert into Company (CompanyName,Email,Address,PhoneNumber) values(%s,%s,%s,%s)",
                (self.company_name_var.get(),
                 self.email_var.get(),
                 self.address_var.get(),
                 self.phone_var.get()))

            conn.commit()
            messagebox.showinfo("Success", "Record has been inserted successfully")
            self.fetch_data()
            self.clear()

    def fetch_data(self, company_id=None):
        cur = conn.cursor()
        cur.execute("select* from Company")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.company_id_var=row[0]
        self.company_name_var.set(row[1])
        self.email_var.set(row[2])
        self.address_var.set(row[3])
        self.phone_var.set(row[4])

    def clear(self):
        self.company_name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.address_var.set('')

    def update(self):
        cur = conn.cursor()
        cur.execute("update company set CompanyName=%s,Email=%s,Address=%s,PhoneNumber=%s where Company_ID=%s",
            (   self.company_name_var.get(),
                self.email_var.get(),
                self.address_var.get(),
                self.phone_var.get(),
                self.company_id_var))

        conn.commit()
        messagebox.showinfo("Success", "Record has been updated successfully")
        self.fetch_data()
        self.clear()

    def delete(self):
        cur = conn.cursor()
        cur.execute("DELETE FROM company WHERE Company_ID ='%s'" % self.company_id_var.get())
        conn.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully")
        self.fetch_data()
        self.clear()

    def search_data(self):
        cur = conn.cursor()
        cur.execute("select* from company where %s" % self.search_by.get() + " LIKE '%s'" % self.search_text.get())
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()


if __name__ == '__main__':
    root = Tk()
    gui = Company(root)
    root.mainloop()