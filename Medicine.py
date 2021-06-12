from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DbHandler import *
from tkcalendar import DateEntry


class Medicine:

    def __init__(self, master):
        self.root = master
        self.expiry_date_var = StringVar()
        self.company_id = None
        self.production_date_var = StringVar()
        self.company_name_var = StringVar()
        self.drug_quantity_var = IntVar()
        self.drug_price_var = IntVar()
        self.drug_cost_var = IntVar()
        self.drug_code_var = StringVar()
        self.drug_type_var = StringVar()
        self.drug_dose_var = StringVar()
        self.drug_name_var = StringVar()
        self.barcode_var = StringVar()
        self.student_table = None
        self.textarea = None
        self.expiry_date = None
        self.production_date = None
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.initialize()

    def initialize(self):
        self.root.title("Medecine Mangement System")
        self.root.configure(bg='white')
        root.state('zoomed')
        self.root.minsize(1200, 670)
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Medecine Mangement System", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # =================Product Frames=================

        F2 = LabelFrame(root, text='Medecine System', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                        fg='#f5b7a6', bg='#a6b1f5')
        F2.place(x=10, y=80, width=520, height=620)

        c = conn.cursor()

        barcode_title = Label(F2, text='Barcode', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        barcode_title.grid(row=0, column=0, padx=5, sticky='w', pady=8)
        barcode_entry = Entry(F2, width=22, font='arial 13', textvariable=self.barcode_var, relief=SUNKEN, bd=1)
        barcode_entry.grid(row=0, column=1, padx=5, sticky='w', pady=8)

        drug_name_title = Label(F2, text='Medicine Name', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_name_title.grid(row=1, column=0, padx=5, sticky='w', pady=8)
        drug_name_entry = Entry(F2, width=22, font='arial 13', textvariable=self.drug_name_var, relief=SUNKEN, bd=1)
        drug_name_entry.grid(row=1, column=1, padx=5, sticky='w', pady=8)

        drug_dose_title = Label(F2, text='Dose', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_dose_title.grid(row=2, column=0, padx=5, sticky='w', pady=8)
        drug_dose_entry = Entry(F2, width=22, font='arial 13', textvariable=self.drug_dose_var, relief=SUNKEN, bd=1)
        drug_dose_entry.grid(row=2, column=1, padx=5, sticky='w', pady=8)

        drug_type_title = Label(F2, text='Type', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_type_title.grid(row=3, column=0, padx=5, sticky='w', pady=8)
        drug_type_entry = Entry(F2, width=22, font='arial 13 ', textvariable=self.drug_type_var, relief=SUNKEN, bd=1)
        drug_type_entry.grid(row=3, column=1, padx=5, sticky='w', pady=8)

        drug_code_title = Label(F2, text='Code No', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_code_title.grid(row=4, column=0, padx=5, sticky='w', pady=8)
        drug_code_entry = Entry(F2, width=22, font='arial 13 ', textvariable=self.drug_code_var, relief=SUNKEN, bd=1)
        drug_code_entry.grid(row=4, column=1, padx=5, sticky='w', pady=8)

        drug_cost_title = Label(F2, text='Cost Price', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_cost_title.grid(row=5, column=0, padx=5, sticky='w', pady=8)
        drug_cost_entry = Entry(F2, width=22, font='arial 13', textvariable=self.drug_cost_var, relief=SUNKEN, bd=1)
        drug_cost_entry.grid(row=5, column=1, padx=5, sticky='w', pady=8)

        drug_price_title = Label(F2, text='Sell price', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_price_title.grid(row=6, column=0, padx=5, sticky='w', pady=8)
        drug_price_entry = Entry(F2, width=22, font='arial 13', textvariable=self.drug_price_var, relief=SUNKEN, bd=1)
        drug_price_entry.grid(row=6, column=1, padx=5, sticky='w', pady=8)

        drug_quantity_title = Label(F2, text='Quantity', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        drug_quantity_title.grid(row=7, column=0, padx=5, sticky='w', pady=8)
        drug_quantity_entry = Entry(F2, width=22, font='arial 13', textvariable=self.drug_quantity_var, relief=SUNKEN,
                                    bd=1)
        drug_quantity_entry.grid(row=7, column=1, padx=5, sticky='w', pady=8)

        c.execute("Select CompanyName from company")
        medicine_company_title = Label(F2, text='Select Company', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        medicine_company_title.grid(row=8, column=0, padx=5, sticky='w', pady=10)
        medicine_company_combo = ttk.Combobox(F2, font=('arial', 14), width=16, state='readonly',textvariable=self.company_name_var)
        medicine_company_combo.grid(row=8, column=1, padx=5, sticky='w', pady=10,ipadx=2)
        medicine_company_combo['values'] = [j[0] for j in c.fetchall()]
        medicine_company_combo.current(1)
        medicine_company_combo.bind("<<ComboboxSelected>>", self.return_company_id)

        production_date_title = Label(F2, text='Production Date', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        production_date_title.grid(row=9, column=0, padx=5, sticky='w', pady=10)
        self.production_date = DateEntry(F2, font=('times new romon', 13), textvariable=self.production_date_var,
                                         width=20, relief=SUNKEN, date_pattern='y-mm-dd')
        self.production_date.grid(row=9, column=1, padx=5, sticky='w', pady=10)

        expiry_date_title = Label(F2, text='Expiry Date', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        expiry_date_title.grid(row=10, column=0, padx=5, sticky='w', pady=10)
        self.expiry_date = DateEntry(F2, font=('times new romon', 13), textvariable=self.expiry_date_var,
                                     width=20, relief=SUNKEN, date_pattern='y-mm-dd')
        self.expiry_date.grid(row=10, column=1, padx=5, sticky='w', pady=10)

        # =========================Buttons======================
        btn_frame = Frame(F2, bd=5, relief=RIDGE)
        btn_frame.place(x=18, y=490)

        add_btn = Button(btn_frame, text='Add', font='arial 12 bold', command=self.add_drug, bg='#c8a6f5',
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

        detail_frame = LabelFrame(root, text='Medecine Detail', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.place(x=560, y=80, width=790, height=620)

        search_title = Label(detail_frame, text='Search By', font=('arial', 14, 'bold'), bg='#a6b1f5')
        search_title.grid(row=0, column=0, padx=5, sticky='w', pady=10)
        search_combo = ttk.Combobox(detail_frame, textvariable=self.search_by, font=('times new romon', 13),
                                    width=15, state='readonly')
        search_combo.grid(row=0, column=1, padx=5, sticky='w', pady=10, ipadx=2)
        search_combo['values'] = ('Barcode', 'Name ', 'Type ', 'CodeNo', 'Dose')
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
            'Barcode', 'Name', 'Dose', 'Type', 'CodeNo', 'CostPrice', 'SellPrice', 'Quantity', 'Company_ID',
            'ProductionDate', 'ExpiryDate'), xscrollcommand=scrol_x, yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('Barcode', text='Barcode')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Dose', text='Dose')
        self.student_table.heading('Type', text='Type')
        self.student_table.heading('CodeNo', text='Code No')
        self.student_table.heading('CostPrice', text='Cost Price')
        self.student_table.heading('SellPrice', text='Sell Price')
        self.student_table.heading('Quantity', text='Quantity')
        self.student_table.heading('Company_ID', text='Company ID')
        self.student_table.heading('ProductionDate', text='Production Date')
        self.student_table.heading('ExpiryDate', text='Expiry Date')

        self.student_table['show'] = 'headings'
        self.student_table.column('Barcode', width=100)
        self.student_table.column('Name', width=100)
        self.student_table.column('Dose', width=100)
        self.student_table.column('Type', width=100)
        self.student_table.column('CodeNo', width=100)
        self.student_table.column('CostPrice', width=100)
        self.student_table.column('SellPrice', width=100)
        self.student_table.column('Quantity', width=100)
        self.student_table.column('Company_ID', width=100)
        self.student_table.column('ProductionDate', width=100)
        self.student_table.column('ExpiryDate', width=110)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_drug(self):

        if self.barcode_var.get() == '' and self.drug_code_var.get() == '' and self.company_name_var.get() == '' and self.production_date_var.get() == '' and self.expiry_date_var.get() == '' and self.drug_quantity_var.get() == '' and self.drug_dose_var == '' and self.drug_type_var.get() == '' and self.drug_price_var.get() == '' or self.drug_cost_var.get() == '' and self.drug_name_var.get():
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            cur = conn.cursor()
            cur.execute(
                "Insert into medicine (Barcode,Name,Dose,Type,CostPrice,SellPrice,Quantity,"
                "Company_ID,ProductionDate,ExpiryDate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.barcode_var.get(),
                 self.drug_name_var.get(),
                 self.drug_dose_var.get(),
                 self.drug_type_var.get(),
                 self.drug_cost_var.get(),
                 self.drug_price_var.get(),
                 self.drug_quantity_var.get(),
                 self.company_id.get(),
                 self.production_date.get_date(),
                 self.expiry_date.get_date()))

            conn.commit()
            messagebox.showinfo("Success", "Record has been inserted successfully")
            self.fetch_data()
            self.clear()

    def fetch_data(self):
        cur = conn.cursor()
        cur.execute("select* from medicine")
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
        cur = conn.cursor()
        self.company_id = row[8]
        cur.execute("select CompanyName from company where CompanyID = '%s'"%self.company_id)
        company_name = cur.fetchone()[0]

        self.barcode_var.set(row[0])
        self.drug_name_var.set(row[1])
        self.drug_dose_var.set(row[2])
        self.drug_type_var.set(row[3])
        self.drug_code_var.set(row[4])
        self.drug_cost_var.set(row[5])
        self.drug_price_var.set(row[6])
        self.drug_quantity_var.set(row[7])
        self.company_name_var.set(company_name)
        self.production_date_var.set(row[9])
        self.expiry_date_var.set(row[10])

    def clear(self):

        self.barcode_var.set('')
        self.drug_name_var.set('')
        self.drug_dose_var.set('')
        self.drug_type_var.set('')
        self.drug_code_var.set('')
        self.drug_cost_var.set('')
        self.drug_price_var.set('')
        self.drug_quantity_var.set('')
        self.production_date_var.set('')
        self.expiry_date_var.set('')

    def update(self):
        cur = conn.cursor()
        cur.execute( "update medicine set Name=%s,Dose=%s,Type=%s,CodeNo=%s,CostPrice=%s,SellPrice=%s,"
            "Quantity=%s,Company_ID=%s,ProductionDate=%s,ExpiryDate=%s where Barcode=%s",
            (self.drug_name_var.get(),
             self.drug_dose_var.get(),
             self.drug_type_var.get(),
             self.drug_code_var.get(),
             self.drug_cost_var.get(),
             self.drug_price_var.get(),
             self.drug_quantity_var.get(),
             self.company_id,
             self.production_date.get_date(),
             self.expiry_date.get_date(),
             self.barcode_var.get()))

        conn.commit()
        messagebox.showinfo("Success", "Record has been updated successfully")
        self.fetch_data()
        self.clear()

    def delete(self):
        cur = conn.cursor()
        cur.execute("DELETE FROM medicine WHERE Barcode ='%s'" % self.barcode_var.get())
        conn.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully")
        self.fetch_data()
        self.clear()

    def search_data(self):
        cur = conn.cursor()
        cur.execute("select* from medicine where %s" % self.search_by.get() + " LIKE '%s'" % self.search_text.get())
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()

    def return_company_id(self,e):
        cur = conn.cursor()
        cur.execute("select CompanyID from company where CompanyName = '%s'" % self.company_name_var)
        self.company_id = cur.fetchone()[0]

if __name__ == '__main__':
    root = Tk()
    gui = Medicine(root)
    root.mainloop()
