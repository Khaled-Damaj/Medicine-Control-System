from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk
from datetime import *
from DbHandler import *
from datetime import *


class Sale:

    def __init__(self, master, employee_name, employee_role):
        self.root = master
        self.x = datetime.now()
        self.date_now = self.x.strftime('%d') + ',' + self.x.strftime('%B') + ',' + self.x.strftime('%Y')
        self.time_now = self.x.strftime('%X') + '  ' + self.x.strftime('%p')
        self.root = master
        self.medicine_price = IntVar()
        self.total_price = IntVar()
        self.prescription_var = StringVar()
        self.barcode_var = StringVar()
        self.medicine_name_var = StringVar()
        self.medicine_type_var = StringVar()
        self.medicine_dose_var = StringVar()
        self.employee_name = None
        self.role = None
        self.patient_name = ''
        self.quantity = IntVar()
        self.bill_no = None
        self.textarea = None
        self.generate_btn = None
        self.submit_btn = None
        self.l = []
        self.q = []
        self.name_quantity = {}
        self.medicine_dose_combo = None
        self.initialize()

    def initialize(self):
        self.root.title("Sale Point")
        self.root.configure(bg='white')
        root.state('zoomed')
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Point of Sale", bd=12, bg='#a6b1f5', fg='white',
                      font=('times new roman', 35, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        F1 = Frame(root, bg='#a6b1f5')
        F1.place(x=10, y=90, width=580, height=50)

        c = conn.cursor()
        c.execute('select Employee_Username,Role from currentuser')
        for name, role in c:
            pass
        c.execute("select Employee_Name from employee where Employee_Username = '%s'" % name)
        self.employee_name = c.fetchone()[0]
        self.role = role

        frame_employee = Frame(F1, bg='#a6b1f5')
        frame_employee.grid(row=0, column=0, sticky='w', pady=10)
        employee_title = Label(frame_employee, text='Emoloyee', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        employee_title.grid(row=0, column=0, padx=10, sticky='w')
        employee_entry = Label(frame_employee, text=self.employee_name, width=15, font='arial 13', relief=SUNKEN, bd=1)
        employee_entry.grid(row=0, column=1, padx=10, sticky='w')

        frame_role = Frame(F1, bg='#a6b1f5')
        frame_role.grid(row=0, column=1, sticky='w', pady=10)
        role_title = Label(frame_role, text='Role', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        role_title.grid(row=0, column=0, padx=10, sticky='w')
        role_entry = Label(frame_role, text=role, width=15, font='arial 13', relief=SUNKEN, bd=1)
        role_entry.grid(row=0, column=1, padx=10, sticky='w')

        # =================Product Frames=================

        F2 = LabelFrame(root, text='Sale System', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                        fg='#f5b7a6',
                        bg='#a6b1f5')
        F2.place(x=10, y=150, width=580, height=550)

        c = conn.cursor()

        c.execute("Select Barcode from medicine")
        barcode_title = Label(F2, text='Select Barcode', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        barcode_title.grid(row=0, column=0, padx=5, sticky='w', pady=10)
        barcode_combo = ttk.Combobox(F2, font=('arial', 14), width=20, state='readonly', textvariable=self.barcode_var)
        barcode_combo.grid(row=0, column=1, padx=5, sticky='w', pady=10)
        barcode_combo['values'] = [j[0] for j in c.fetchall()]
        barcode_combo.current()
        barcode_combo.bind("<<ComboboxSelected>>", self.fill_inputes)

        c.execute("Select Name from medicine")
        medicine_name_title = Label(F2, text='Select Medecine', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_name_title.grid(row=1, column=0, padx=5, sticky='w', pady=10)
        medicine_name_combo = ttk.Combobox(F2, font=('arial', 14), width=20, state='readonly',
                                           textvariable=self.medicine_name_var)
        medicine_name_combo.grid(row=1, column=1, padx=5, sticky='w', pady=10)
        medicine_name_combo['values'] = [j[0] for j in c.fetchall()]
        medicine_name_combo.current()

        c.execute("Select Type from medicine")
        medicine_type_title = Label(F2, text='Select Type', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_type_title.grid(row=2, column=0, padx=5, sticky='w', pady=10)
        medicine_type_combo = ttk.Combobox(F2, font=('arial', 14), width=20, state='readonly',
                                           textvariable=self.medicine_type_var)
        medicine_type_combo.grid(row=2, column=1, padx=5, sticky='w', pady=10)
        rows = c.fetchall()
        type = []
        for j in rows:
            if j[0] not in type:
                type.append(j[0])
        medicine_type_combo['values'] = type
        medicine_type_combo.current()

        c.execute("Select Dose from medicine")
        medicine_dose_title = Label(F2, text='Select Dose', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_dose_title.grid(row=3, column=0, padx=5, sticky='w', pady=10)
        medicine_dose_combo = ttk.Combobox(F2, font=('arial', 14), width=20, state='readonly',
                                           textvariable=self.medicine_dose_var)
        medicine_dose_combo.grid(row=3, column=1, padx=5, sticky='w', pady=10)
        medicine_dose_combo['values'] = [j[0] + ' mg' for j in c.fetchall()]
        medicine_dose_combo.current()

        c.execute("Select PrescriptionID from patient")
        medicine_dose_title = Label(F2, text='Select Prescription', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_dose_title.grid(row=4, column=0, padx=5, sticky='w', pady=10)
        self.medicine_dose_combo = ttk.Combobox(F2, font=('arial', 14), width=20, state='readonly',
                                                textvariable=self.prescription_var)
        self.medicine_dose_combo.grid(row=4, column=1, padx=5, sticky='w', pady=10)
        self.medicine_dose_combo['values'] = [j[0] for j in c.fetchall()]
        self.medicine_dose_combo.current()

        medicine_quantity_title = Label(F2, text='Quantity', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_quantity_title.grid(row=5, column=0, padx=5, sticky='w', pady=10)
        medicine_quantity_entry = Entry(F2, width=22, textvariable=self.quantity, font='arial 14', relief=SUNKEN,
                                        bd=1, )
        medicine_quantity_entry.grid(row=5, column=1, padx=5, sticky='w', pady=10)
        medicine_quantity_entry.bind("<KeyRelease>", self.OnEntryClick)

        medicine_quantity_title = Label(F2, text='Price', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_quantity_title.grid(row=6, column=0, padx=5, sticky='w', pady=10)
        medicine_quantity_entry = Entry(F2, width=22, textvariable=self.medicine_price, font='arial 14 bold',
                                        relief=SUNKEN, bd=1, state='readonly')
        medicine_quantity_entry.grid(row=6, column=1, padx=5, sticky='w', pady=10)

        medicine_total_title = Label(F2, text='Total', font=('times new romon', 14, 'bold'), bg='#a6b1f5')
        medicine_total_title.grid(row=7, column=0, padx=5, sticky='w', pady=10)
        medicine_total_entry = Entry(F2, width=22, textvariable=self.total_price, font='arial 14 bold',
                                     relief=SUNKEN, bd=1, state='readonly')
        medicine_total_entry.grid(row=7, column=1, padx=5, sticky='w', pady=10)

        c = conn.cursor()
        try:
            c.execute('SELECT Order_No FROM bill WHERE Order_No=(SELECT MAX(Order_No) FROM bill)')
            self.bill_no = c.fetchone()[0] + 1
        except:
            self.bill_no = 1
        print(self.bill_no)

        # ========================Bill area================
        F3 = Frame(root, relief=GROOVE, bd=10)
        F3.place(x=650, y=150, width=650, height=500)

        bill_title = Label(F3, text='Bill Area', font='arial 20 bold', bg='#a6b1f5', bd=7, relief=GROOVE,
                           fg='white').pack(fill=X)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack()
        self.welcome()

        # =========================Buttons======================
        btn_frame = Frame(F2, bd=5, relief=RIDGE)
        btn_frame.place(x=32, y=400)

        add_btn = Button(btn_frame, text='Add Item', font='arial 12 bold', command=self.add_item, bg='#c8a6f5',
                         fg='white', width=8)
        add_btn.grid(row=0, column=0, padx=10, pady=10)
        self.generate_btn = Button(btn_frame, text='Generate Bill', font='arial 12 bold', bg='#c8a6f5', width=10,
                                   fg='white', command=self.generate_bill, state=DISABLED)
        self.generate_btn.grid(row=0, column=2, padx=10, pady=10)
        self.submit_btn = Button(btn_frame, text='Submit Order', font='arial 12 bold', bg='#c8a6f5', width=10,
                                 fg='white', command=self.submit_order, state=DISABLED)
        self.submit_btn.grid(row=0, column=1, padx=10, pady=10)
        clear_btn = Button(btn_frame, text='Clear', font='arial 12 bold', command=self.clear, bg='#c8a6f5', width=8,
                           fg='white')
        clear_btn.grid(row=0, column=3, padx=10, pady=10)

        # =========================================================================================================

    def welcome(self):

        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\n\t\t\tSE Pharmacy")
        self.textarea.insert(END, f"\n\nBill No: {self.bill_no}")
        self.textarea.insert(END, f"\nPatient Name: {self.patient_name}")
        self.textarea.insert(END, f"\nDate: {self.date_now}")
        self.textarea.insert(END, f"\nTime: {self.time_now}")
        self.textarea.insert(END, f"\n\n==================================================")
        self.textarea.insert(END, "\nItem\t\tQTY\t\tPrice\t\tAmount")
        self.textarea.insert(END, f"\n==================================================\n")
        self.textarea.configure(font='arial 15 bold')

    def add_item(self):

        if len(self.medicine_dose_combo['values']) == 0 and self.medicine_name_var.get() == '' and self.medicine_type_var.get() == ''and self.medicine_dose_var.get() == '' and self.quantity.get() == 0 and self.prescription_var== '':
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            self.textarea.insert((14.0 + float(len(self.l) - 1)),
                                 f"{self.medicine_name_var.get()}\t\t{self.quantity.get()}\t\t{self.medicine_price.get()}\t\t{self.total_price.get()}\n")

            if self.barcode_var.get() in self.name_quantity:
                self.name_quantity[self.barcode_var.get()] += self.quantity.get()
            else:
                self.name_quantity[self.barcode_var.get()] = self.quantity.get()

            self.l.append(self.total_price.get())
            self.q.append(self.quantity.get())

            self.submit_btn.config(state=NORMAL)
            self.quantity.set(0)

    def submit_order(self):
        c = conn.cursor()
        c.execute("select Patient_ID from patient where PrescriptionID = %s" % self.prescription_var.get())
        patient_id = c.fetchone()[0]
        c.execute('select FirstName,MiddleName,LastName from patient where Patient_ID=%s' % patient_id)
        for fname, mname, lname in c.fetchall():
            self.patient_name = fname + ' ' + mname + ' ' + lname
        c.execute("select Employee_ID from employee where Employee_Name = '%s'" % self.employee_name)
        employee_id = c.fetchone()[0]
        c.execute(
            "Insert into bill (Employee_ID,Patient_ID,Total_Price,Quantity,Date) values(%s,%s,%s,%s,%s)",
            (employee_id,
             patient_id,
             self.total_price.get(),
             sum(self.l),
             datetime.now()))

        for key, value in self.name_quantity.items():
            c.execute("select Quantity from medicine where Barcode = '%s'" % key)
            quantity_in_stock = c.fetchone()[0]
            c.execute("update medicine set Quantity = %s where Barcode=%s", (quantity_in_stock - value, key))

        for key, value in self.name_quantity.items():
            c.execute("select Name,Dose,Type,SellPrice from medicine where Barcode = '%s'" % key)
            rows =c.fetchall()
            for name,dose,category,price in rows:
                pass
            c.execute(
                "Insert into historysales (Barcode,Name,Dose,Type,Quantity,EmployeeName,Patient_ID,Amount,SaleDate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (key,name,dose,category,value,self.employee_name,patient_id,price*value,datetime.now()))


        textAreaText = self.textarea.get(12.0, (12.0 + float(len(self.l))))
        self.welcome()
        self.textarea.insert(END, textAreaText)
        self.textarea.insert(END, f"==================================================\n")
        self.textarea.insert(END, f"\nTotal:  {sum(self.l)}")
        self.textarea.insert(END, f"\n\n\t\t  You have been served by:\n")
        self.textarea.insert(END, f"\t\t\t{self.employee_name}")
        self.generate_btn.config(state=NORMAL)
        self.submit_btn.config(state=DISABLED)

    def generate_bill(self):
        op = messagebox.askyesno("Save bill", "Do you want to save the Bill?")
        if op > 0:
            bill_details = self.textarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no) + ".txt", "w")
            f1.write(bill_details)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no, :{self.bill_no} Saved Successfully")
            self.clear()
        else:
            return

    def clear(self):
        c = conn.cursor()
        c.execute('SELECT Order_No FROM bill WHERE Order_No=(SELECT MAX(Order_No) FROM bill)')
        self.bill_no = c.fetchone()[0] + 1
        self.barcode_var.set('')
        self.medicine_price.set('')
        self.medicine_dose_var.set('')
        self.medicine_type_var.set('')
        self.medicine_name_var.set('')
        self.prescription_var.set('')
        self.total_price.set(0)
        self.medicine_price.set(0)
        self.quantity.set(0)
        self.welcome()
        self.l = []
        self.q = []

    def fill_inputes(self, e):
        c = conn.cursor()
        c.execute('select ExpiryDate from medicine where barcode="%s"' % self.barcode_var.get())
        expiry = c.fetchone()[0]
        c.execute('select Name,Type,Dose,SellPrice from medicine where barcode="%s"' % self.barcode_var.get())
        rows = c.fetchall()
        for name, type, dose, price in rows:
            pass
        self.medicine_name_var.set(name)
        self.medicine_dose_var.set(dose)
        self.medicine_type_var.set(type)
        self.medicine_price.set(price)
        if expiry < datetime.date(datetime.now()):
            messagebox.showwarning("Error", "Out of date")
            self.clear()

    def OnEntryClick(self, e):
        c = conn.cursor()
        c.execute('select quantity from medicine where barcode="%s"' % self.barcode_var.get())
        row = c.fetchone()[0]
        if self.quantity.get() <= row:
            self.total_price.set(self.medicine_price.get() * float(self.quantity.get()))
        else:
            msg = 'The stock contain only ' + str(row)
            messagebox.showerror('Error', msg)
            self.quantity.set('')


if __name__ == '__main__':
    root = Tk()
    gui = Sale(root, 'Khaled Damaj', 'Admin')
    root.mainloop()
