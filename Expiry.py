from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DbHandler import *
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


class Expiry:

    def __init__(self, master):
        self.root = master
        self.student_table = None
        self.initialize()

    def initialize(self):
        self.root.title("Sale Point")
        self.root.configure(bg='white')
        self.root.state('zoomed')
        self.root.minsize(700, 560)
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Expiry Drug", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # ========================Detail area================

        detail_frame = LabelFrame(root, text='Expiry Detail', relief=RIDGE, bd=10, font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.pack(fill=BOTH, pady=50, padx=100)

        # ========================Table area================

        table_frame = Frame(detail_frame, relief=RIDGE, bd=5, bg='#eeeeee')
        table_frame.pack(fill=BOTH, pady=20)

        scrol_y = Scrollbar(table_frame, orient=VERTICAL)
        scrol_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            'Barcode', 'Drug Name', 'Expiry Date', 'Quantity Remains'), xscrollcommand=scrol_x, yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('Barcode', text='Barcode')
        self.student_table.heading('Drug Name', text='Drug Name')
        self.student_table.heading('Expiry Date', text='Expiry Date')
        self.student_table.heading('Quantity Remains', text='Quantity Remains')

        self.student_table['show'] = 'headings'
        self.student_table.column('Barcode', width=20)
        self.student_table.column('Drug Name', width=50)
        self.student_table.column('Expiry Date', width=50)
        self.student_table.column('Quantity Remains', width=50)

        self.student_table.pack(fill=BOTH, expand=1)

        add_btn = Button(self.root, text='Generate Reports', font='arial 14 bold', command=self.generate_report,
                         bg='#c8a6f5',
                         fg='white', width=15)
        add_btn.pack()

        # ====================================================================================

    def generate_report(self):
        c = conn.cursor()
        c.execute("delete from expiry")
        c.execute("select Barcode,Name,ExpiryDate,Quantity from medicine where ExpiryDate < '%s'" % datetime.date(
            datetime.now()))
        rows = c.fetchall()
        drug_name = []
        drug_qunatity = []
        for Barcode, Name, ExpiryDate, Quantity in rows:
            drug_name.append(Name)
            drug_qunatity.append(Quantity)
            c.execute("Insert into expiry (Barcode,Name,ExpiryDate,Quantity) values(%s,%s,%s,%s)",
                      (Barcode, Name, ExpiryDate, Quantity))
        messagebox.showinfo("Success", "Expiry Report is successfully generated")
        self.fetch_data()
        x = np.array(drug_name)
        y = np.array(drug_qunatity)
        fig, ax = plt.subplots()
        ax.bar(x, y)
        ax.set_ylabel('Quantity')
        ax.set_xlabel('Medicine Name')
        ax.set_title('Expiry Histogram')
        plt.show()

    def fetch_data(self):
        cur = conn.cursor()
        cur.execute("select* from expiry")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()


if __name__ == '__main__':
    root = Tk()
    gui = Expiry(root)
    root.mainloop()
