from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DbHandler import *
from tkinter import filedialog


class Patient:

    def __init__(self, master):
        self.patient_var = IntVar()
        self.prescription_id_var = IntVar()
        self.root = master
        self.student_table = None
        self.textarea = None
        self.fname_var = StringVar()
        self.mname_var = StringVar()
        self.lname_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.phone_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.prescription_var = StringVar()
        self.identity_var = StringVar()
        self.choose_identity_var = StringVar()
        self.initialize()

    def initialize(self):
        self.root.title("Sale Point")
        self.root.configure(bg='white')
        root.state('zoomed')
        self.root.minsize(1200, 670)
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Patient", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # =================Product Frames=================

        F2 = LabelFrame(root, text='Patient System', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                        fg='#f5b7a6', bg='#a6b1f5')
        F2.place(x=10, y=80, width=520, height=620)

        c = conn.cursor()
        c.execute('SELECT Patient_ID FROM patient WHERE Patient_ID=(SELECT MAX(Patient_ID) FROM patient)')
        patient_id = c.fetchone()[0] + 1
        self.patient_var.set(patient_id)
        patient_title = Label(F2, text='Patient ID', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        patient_title.grid(row=0, column=0, padx=5, sticky='w', pady=8)
        patient_entry = Label(F2, width=22, font='arial 13', textvariable=self.patient_var, relief=SUNKEN, bd=1)
        patient_entry.grid(row=0, column=1, padx=5, sticky='w', pady=8)

        fname_title = Label(F2, text='First Name', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        fname_title.grid(row=1, column=0, padx=5, sticky='w', pady=8)
        fname_entry = Entry(F2, width=22, font='arial 13', textvariable=self.fname_var, relief=SUNKEN, bd=1)
        fname_entry.grid(row=1, column=1, padx=5, sticky='w', pady=8)

        mname_title = Label(F2, text='Middle Name', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        mname_title.grid(row=2, column=0, padx=5, sticky='w', pady=8)
        mname_entry = Entry(F2, width=22, font='arial 13', textvariable=self.mname_var, relief=SUNKEN, bd=1)
        mname_entry.grid(row=2, column=1, padx=5, sticky='w', pady=8)

        lname_title = Label(F2, text='Last Name', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        lname_title.grid(row=3, column=0, padx=5, sticky='w', pady=8)
        lname_entry = Entry(F2, width=22, font='arial 13 ', textvariable=self.lname_var, relief=SUNKEN, bd=1)
        lname_entry.grid(row=3, column=1, padx=5, sticky='w', pady=8)

        gender_title = Label(F2, text='Gender', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        gender_title.grid(row=4, column=0, padx=5, sticky='w', pady=8)
        gender_combo = ttk.Combobox(F2, font=('times new romon', 13), textvariable=self.gender_var, width=20,
                                    state='readonly')
        gender_combo.grid(row=4, column=1, padx=5, sticky='w', pady=8)
        gender_combo['values'] = ('Male', 'Female')
        gender_combo.current()

        address_title = Label(F2, text='Address', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        address_title.grid(row=5, column=0, padx=5, sticky='w', pady=8)
        address_entry = Entry(F2, width=22, font='arial 13', textvariable=self.address_var, relief=SUNKEN, bd=1)
        address_entry.grid(row=5, column=1, padx=5, sticky='w', pady=8)

        phone_title = Label(F2, text='Phone Number', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        phone_title.grid(row=6, column=0, padx=5, sticky='w', pady=8)
        phone_entry = Entry(F2, width=22, font='arial 13', textvariable=self.phone_var, relief=SUNKEN, bd=1)
        phone_entry.grid(row=6, column=1, padx=5, sticky='w', pady=8)

        choose_identity_title = Label(F2, text='Identity Type', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        choose_identity_title.grid(row=7, column=0, padx=5, sticky='w', pady=8)
        choose_identity_combo = ttk.Combobox(F2, font=('times new romon', 13), textvariable=self.choose_identity_var,
                                             width=20,
                                             state='readonly')
        choose_identity_combo.grid(row=7, column=1, padx=5, sticky='w', pady=8)
        choose_identity_combo['values'] = ('ID', 'Passport', 'Driving License', 'Other Official papers')
        choose_identity_combo.current()

        identity_title = Label(F2, text='Identity Image', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        identity_title.grid(row=8, column=0, padx=5, sticky='w', pady=8)
        frame1 = Frame(F2, bg='#a6b1f5')
        frame1.grid(row=8, column=1, padx=1, sticky='w', pady=8)
        identity_file_explorer = Label(frame1, width=35, font='arial 8', textvariable=self.identity_var)
        identity_file_explorer.grid(row=0, column=1, sticky='w', pady=5)
        identity_btn = Button(frame1, text='Browse', font='arial 12 bold', fg='white', width=8,
                              command=lambda: self.browseFiles(self.identity_var), bg='#c8a6f5')
        identity_btn.grid(row=0, column=0, pady=5, sticky='w', padx=5)

        PrescriptionID_title = Label(F2, text='Prescription ID', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        PrescriptionID_title.grid(row=9, column=0, padx=5, sticky='w', pady=8)
        PrescriptionID_entry = Entry(F2, width=22, font='arial 13', textvariable=self.prescription_id_var,
                                     relief=SUNKEN, bd=1)
        PrescriptionID_entry.grid(row=9, column=1, padx=5, sticky='w', pady=8)

        prescription_title = Label(F2, text='Prescription Image', font=('times new romon', 13, 'bold'), bg='#a6b1f5')
        prescription_title.grid(row=10, column=0, padx=5, sticky='w', pady=8)
        frame2 = Frame(F2, bg='#a6b1f5')
        frame2.grid(row=10, column=1, padx=1, sticky='w', pady=10)
        prescription_file_explorer = Label(frame2, width=35, font='arial 8', textvariable=self.prescription_var)
        prescription_file_explorer.grid(row=0, column=1, sticky='w', pady=5)
        prescription_btn = Button(frame2, text='Browse', font='arial 12 bold',
                                  command=lambda: self.browseFiles(self.prescription_var), bg='#c8a6f5',
                                  fg='white', width=8)
        prescription_btn.grid(row=0, column=0, pady=5, sticky='w', padx=5)

        # =========================Buttons======================
        btn_frame = Frame(F2, bd=5, relief=RIDGE)
        btn_frame.place(x=18, y=490)

        add_btn = Button(btn_frame, text='Add', font='arial 12 bold', command=self.add_patient, bg='#c8a6f5',
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

        detail_frame = LabelFrame(root, text='Patient Detail', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.place(x=560, y=80, width=790, height=620)

        search_title = Label(detail_frame, text='Search By', font=('arial', 14, 'bold'), bg='#a6b1f5')
        search_title.grid(row=0, column=0, padx=5, sticky='w', pady=10)
        search_combo = ttk.Combobox(detail_frame, textvariable=self.search_by, font=('times new romon', 13),
                                    width=15, state='readonly')
        search_combo.grid(row=0, column=1, padx=5, sticky='w', pady=10, ipadx=2)
        search_combo['values'] = ('FirstName', 'MiddleName ', 'LastName ', 'PhoneNumber', 'PrescriptionID')
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
            'ID', 'FirstName', 'MiddleName', 'LastName', 'Gender', 'Address', 'Phone_Number',
            'Identity Type', 'Physical ID', 'Prescription ID', 'Prescription Image'), xscrollcommand=scrol_x,
                                          yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('ID', text='ID')
        self.student_table.heading('FirstName', text='First Name')
        self.student_table.heading('MiddleName', text='Middle Name')
        self.student_table.heading('LastName', text='Last Name')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Phone_Number', text='Phone Number')
        self.student_table.heading('Identity Type', text='Identity Type')
        self.student_table.heading('Physical ID', text='Physical ID')
        self.student_table.heading('Prescription ID', text='Prescription ID')
        self.student_table.heading('Prescription Image', text='Prescription Image')

        self.student_table['show'] = 'headings'
        self.student_table.column('ID', width=50)
        self.student_table.column('FirstName', width=100)
        self.student_table.column('MiddleName', width=100)
        self.student_table.column('LastName', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('Address', width=100)
        self.student_table.column('Phone_Number', width=100)
        self.student_table.column('Identity Type', width=100)
        self.student_table.column('Physical ID', width=100)
        self.student_table.column('Prescription ID', width=100)
        self.student_table.column('Prescription Image', width=110)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_patient(self):

        if self.fname_var.get() == '' or self.mname_var.get() == '' or self.lname_var.get() == '':
            messagebox.showerror("Error", "All fields are required to fill")
        elif self.gender_var.get() == '' or self.address_var.get() == '':
            messagebox.showerror("Error", "All fields are required to fill")
        elif self.phone_var.get() == '' or self.choose_identity_var == '':
            messagebox.showerror("Error", "All fields are required to fill")
        elif self.prescription_var.get() == '' or self.identity_var.get() == '' or self.prescription_id_var.get() == '':
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            cur = conn.cursor()
            cur.execute(
                "Insert into Patient (FirstName,MiddleName,LastName,Gender,Address,PhoneNumber,IdentityType,"
                "Physical_ID,PrescriptionID,PrescriptionImage) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.fname_var.get(),
                 self.mname_var.get(),
                 self.lname_var.get(),
                 self.gender_var.get(),
                 self.address_var.get(),
                 self.phone_var.get(),
                 self.choose_identity_var.get(),
                 self.convertToBinaryData(self.identity_var.get()),
                 self.prescription_id_var.get(),
                 self.convertToBinaryData(self.prescription_var.get())))

            conn.commit()
            messagebox.showinfo("Success", "Record has been inserted successfully")
            cur.execute('SELECT Patient_ID FROM patient WHERE Patient_ID=(SELECT MAX(Patient_ID) FROM patient)')
            patient_id = cur.fetchone()[0] + 1
            self.patient_var.set(patient_id)
            self.fetch_data()
            self.clear()

    def fetch_data(self):
        cur = conn.cursor()
        cur.execute("select* from Patient")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                full_name = row[1] + '_' + row[2] + '_' + row[3]
                PID = row[7]
                identity_img = row[8]
                prescription_img = row[10]
                identity = full_name + "_" + PID
                self.write_file(identity_img, identity)
                self.write_file(prescription_img, full_name + "_Prescription")
                self.student_table.insert('', END, values=row)
            conn.commit()
            cur.execute('SELECT Patient_ID FROM patient WHERE Patient_ID=(SELECT MAX(Patient_ID) FROM patient)')
            patient_id = cur.fetchone()[0] + 1
            self.patient_var.set(patient_id)

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.patient_var.set(row[0])
        self.fname_var.set(row[1])
        self.mname_var.set(row[2])
        self.lname_var.set(row[3])
        self.gender_var.set(row[4])
        self.address_var.set(row[5])
        self.phone_var.set(row[6])
        self.choose_identity_var.set(row[7])
        self.prescription_id_var.set(row[9])

    def clear(self):
        self.identity_var.set('')
        self.prescription_var.set('')
        self.fname_var.set('')
        self.mname_var.set('')
        self.lname_var.set('')
        self.phone_var.set('')
        self.gender_var.set('')
        self.address_var.set('')
        self.prescription_id_var.set('')
        self.choose_identity_var.set('')

    def update(self):
        cur = conn.cursor()

        if self.identity_var.get() != '' and self.prescription_var.get() != '':
            cur.execute(
                "update patient set FirstName=%s,MiddleName=%s,LastName=%s,Gender=%s,Address=%s,PhoneNumber=%s,"
                "IdentityType=%s,Physical_ID=%s,PrescriptionImage=%s where Patient_ID=%s",
                (
                    self.fname_var.get(),
                    self.mname_var.get(),
                    self.lname_var.get(),
                    self.gender_var.get(),
                    self.address_var.get(),
                    self.phone_var.get(),
                    self.choose_identity_var.get(),
                    self.convertToBinaryData(self.identity_var.get()),
                    self.convertToBinaryData(self.prescription_var.get()),
                    self.patient_var.get()))

        elif self.prescription_var.get() == '':
            cur.execute(
                "update patient set FirstName=%s,MiddleName=%s,LastName=%s,Gender=%s,Address=%s,PhoneNumber=%s,"
                "IdentityType=%s,Physical_ID=%s where Patient_ID=%s",
                (
                    self.fname_var.get(),
                    self.mname_var.get(),
                    self.lname_var.get(),
                    self.gender_var.get(),
                    self.address_var.get(),
                    self.phone_var.get(),
                    self.choose_identity_var.get(),
                    self.convertToBinaryData(self.identity_var.get()),
                    self.patient_var.get()))

        elif self.identity_var.get() == '':
            cur.execute(
                "update patient set FirstName=%s,MiddleName=%s,LastName=%s,Gender=%s,Address=%s,PhoneNumber=%s,"
                "IdentityType=%s,PrescriptionImage=%s where Patient_ID=%s",
                (
                    self.fname_var.get(),
                    self.mname_var.get(),
                    self.lname_var.get(),
                    self.gender_var.get(),
                    self.address_var.get(),
                    self.phone_var.get(),
                    self.choose_identity_var.get(),
                    self.convertToBinaryData(self.prescription_var.get()),
                    self.patient_var.get()))
        # else:
        cur.execute("update patient set FirstName=%s,MiddleName=%s,LastName=%s,Gender=%s,Address=%s,PhoneNumber=%s,"
                    "IdentityType=%s where Patient_ID=%s",
                    (
                        self.fname_var.get(),
                        self.mname_var.get(),
                        self.lname_var.get(),
                        self.gender_var.get(),
                        self.address_var.get(),
                        self.phone_var.get(),
                        self.choose_identity_var.get(),
                        self.patient_var.get()))

        conn.commit()
        messagebox.showinfo("Success", "Record has been updated successfully")
        self.fetch_data()
        self.clear()

    def delete(self):
        cur = conn.cursor()
        cur.execute("DELETE FROM Patient WHERE Patient_ID ='%s'" % self.patient_var.get())
        conn.commit()
        messagebox.showinfo("Success", "Record has been deleted successfully")
        self.fetch_data()
        self.clear()

    def search_data(self):
        cur = conn.cursor()
        cur.execute("select* from Patient where %s" % self.search_by.get() + " LIKE '%s'" % self.search_text.get())
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()

    def browseFiles(self, label):
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("all files", "*.*"), ("Text files", "*.txt*")))
        # Change label contents
        label.set(filename)

    def convertToBinaryData(self, filename):
        if filename == '':
            return
            # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open('Image from database/' + filename + '.png', 'wb') as file:
            file.write(data)


if __name__ == '__main__':
    root = Tk()
    gui = Patient(root)
    root.mainloop()
