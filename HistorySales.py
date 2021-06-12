from tkinter import *
from tkinter import ttk
from DbHandler import *


class HistorySales:

    def __init__(self, master):
        self.root = master
        self.student_table = None
        self.initialize()

    def initialize(self):
        self.root.title("History Sales")
        self.root.configure(bg='white')
        self.root.state('zoomed')
        self.root.minsize(900, 560)
        self.display()

    def display(self):
        # =================Title=================
        title = Label(root, pady=2, text="History Sales", bd=10, bg='#a6b1f5', fg='white',
                      font=('times new roman', 30, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        # ========================Detail area================

        detail_frame = LabelFrame(root, text='History Sales Detail', relief=RIDGE, bd=10,
                                  font=('times new romon', 20, 'bold'),
                                  fg='#f5b7a6', bg='#a6b1f5')
        detail_frame.pack(fill=BOTH, pady=50, padx=100)

        # ========================Table area================

        table_frame = Frame(detail_frame, relief=RIDGE, bd=5, bg='#eeeeee')
        table_frame.pack(fill=BOTH, pady=20)

        scrol_y = Scrollbar(table_frame, orient=VERTICAL)
        scrol_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            'Sales_ID', 'Barcode', 'Name', 'Dose', 'Type', 'Quantity', 'Employee_Name', 'Patient_ID', 'Amount',
            'SaleDate'), xscrollcommand=scrol_x, yscrollcommand=scrol_y)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_y.config(command=self.student_table.yview)
        scrol_x.config(command=self.student_table.xview)

        self.student_table.heading('Sales_ID', text='Sales_ID')
        self.student_table.heading('Barcode', text='Barcode')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Dose', text='Dose')
        self.student_table.heading('Type', text='Type')
        self.student_table.heading('Quantity', text='Quantity')
        self.student_table.heading('Employee_Name', text='Employee Name')
        self.student_table.heading('Patient_ID', text='Patient_ID')
        self.student_table.heading('Amount', text='Amount')
        self.student_table.heading('SaleDate', text='SaleDate')

        self.student_table['show'] = 'headings'
        self.student_table.column('Sales_ID', width=20)
        self.student_table.column('Barcode', width=50)
        self.student_table.column('Name', width=50)
        self.student_table.column('Dose', width=10)
        self.student_table.column('Type', width=20)
        self.student_table.column('Quantity', width=10)
        self.student_table.column('Employee_Name', width=50)
        self.student_table.column('Patient_ID', width=10)
        self.student_table.column('Amount', width=50)
        self.student_table.column('SaleDate', width=50)

        self.student_table.pack(fill=BOTH, expand=1)

        add_btn = Button(self.root, text='Generate Reports', font='arial 14 bold', command=self.generate_report,
                         bg='#c8a6f5',
                         fg='white', width=15)
        add_btn.pack()

        # ====================================================================================

    def generate_report(self):
        self.fetch_data()

    def fetch_data(self):
        cur = conn.cursor()
        cur.execute("select* from historysales")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()


if __name__ == '__main__':
    root = Tk()
    gui = HistorySales(root)
    root.mainloop()
