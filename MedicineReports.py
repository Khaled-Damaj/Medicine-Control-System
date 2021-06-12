from tkinter import *
from tkinter import ttk
from DbHandler import *
import matplotlib.pyplot as plt
import numpy as np

class MedicineReport:

    def __init__(self, master):
        self.root = master
        self.student_table = None
        self.drug_quantity_var = IntVar()
        self.drug_name_var = StringVar()
        self.barcode_var = StringVar()
        self.initialize()

    def initialize(self):
        self.root.title("Medicine Reports")
        self.root.configure(bg='white')
        self.root.state('zoomed')
        self.root.minsize(900, 560)
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="Medicine Reports", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # ========================Detail area================

        detail_frame = LabelFrame(root, text='Medicine Reports Detail', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.pack(fill=BOTH, pady=50, padx=100)

        # ========================Table area================

        table_frame = Frame(detail_frame, relief=RIDGE, bd=5, bg='#eeeeee')
        table_frame.pack(fill=BOTH, pady=20)

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

        add_btn = Button(self.root, text='Generate Reports', font='arial 14 bold', command=self.generate_report,
                         bg='#c8a6f5',
                         fg='white', width=15)
        add_btn.pack()

        # ====================================================================================

    def generate_report(self):
        c = conn.cursor()
        c.execute("select Name,Quantity from medicine")
        rows = c.fetchall()
        drug_name = []
        drug_qunatity = []
        for Name,Quantity in rows:
            drug_name.append(Name)
            drug_qunatity.append(Quantity)

        print(drug_name,drug_qunatity)

        y = np.array(drug_qunatity)
        mylabels = drug_name

        plt.pie(y, labels=mylabels)
        plt.legend()
        plt.show()
        self.fetch_data()

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
        self.barcode_var.set(row[0])
        self.drug_name_var.set(row[1])
        self.drug_quantity_var.set(row[7])


if __name__ == '__main__':
    root = Tk()
    gui = MedicineReport(root)
    root.mainloop()
