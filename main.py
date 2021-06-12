from tkinter import *
from tkinter import messagebox
from time import strftime
from DbHandler import *
from datetime import datetime
from tkinter import filedialog
import os
from datetime import *

def browseFiles(label):
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("all files", "*.*"), ("Text files", "*.txt*")))
    # Change label contents
    label.set(filename)


def convertToBinaryData(filename):
    if filename == '':
        return
        # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open('Image from database/' + filename + '.png', 'wb') as file:
        file.write(data)


class MainWindow:
    def __init__(self, master):
        self.root = master
        self.frame = Frame(self.root, bg='white')
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.initialize()

    def initialize(self):
        self.root.title("Pharmacy Management System")
        self.root.geometry('700x500')
        self.root.configure(bg='white')
        Label(self.frame, text="Medicine Control System", font="Arial 30 bold", bg='white').grid(row=0, column=0,
                                                                                                 columnspan=2, pady=10)
        self.frame.pack(pady=30)
        self.display_registriation()

    def display_registriation(self):
        frame = Frame(self.frame, width=500, height=200, relief='ridge', bd=10, bg='#a6b1f5')
        frame.grid(row=1, column=0, pady=20, padx=100)
        usernamelabel = Label(frame, text='Username', font="Arial 15 bold", bg='#a6b1f5')
        usernamelabel.grid(row=0, column=0, pady=15, padx=10)
        self.username = Entry(frame, textvariable=self.username_var, font="Arial 15 bold", bd=2)
        self.username.grid(row=0, column=1, padx=25)
        passwordlabel = Label(frame, text='Password', font="Arial 15 bold", bg='#a6b1f5')
        passwordlabel.grid(row=1, column=0, pady=20, padx=10)
        self.password = Entry(frame, textvariable=self.password_var, font="Arial 15 bold", bd=2, show='*')
        self.password.grid(row=1, column=1, padx=25)
        self.btnlogin = Button(frame, text='Login', font="Arial 15 bold", command=self.login, bg='#c8a6f5', fg='white',
                               width=10)
        self.btnlogin.grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        if len(self.username.get()) == 0:
            messagebox.showerror('Warning', 'Please enter your name')
            return
        if len(self.password.get()) == 0:
            messagebox.showerror('Warning', 'Please enter your password')
            return
        c = conn.cursor()
        username = self.username_var.get()
        password = self.password_var.get()
        login = False
        c.execute('Select Role_Name,Employee_Username,Employee_Password from login')
        for role, user, pwd in c:
            if username == user and password == pwd:
                login = True
        if login:
            c.execute("Select Employee_ID from employee where Employee_Username = '%s'" % username)
            id = c.fetchone()[0]
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_obj = datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
            c.execute("insert into session (Employee_ID,Date_login) values(%s,%s)", (id, date_obj))
            c.execute("insert into currentuser (Employee_Username,Role) values(%s,%s)", (username, role))
            self.root.destroy()
            root = Tk()
            Dashbord(root, username, date_obj)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Password or Username is incorrect. Try Again!")


class Dashbord:

    def __init__(self, master, username, date_now):
        self.username = username
        self.date_now = date_now
        self.name = None
        self.role = None
        self.root = master
        self.time_now = None
        self.user_image = PhotoImage(file='./Images/user-icon-vector.png')
        self.medicine_image = PhotoImage(file="./Images/medicine.png")
        self.employee_image = PhotoImage(file="./Images/employee.png")
        self.company_image = PhotoImage(file="./Images/company.png")
        self.report_image = PhotoImage(file="./Images/report.png")
        self.saleshistory_image = PhotoImage(file="Images/saleshistory.png")
        self.patient_image = PhotoImage(file="./Images/patient.png")
        self.quit_image = PhotoImage(file="Images/Quit.png")
        self.sale_image = PhotoImage(file="Images/shopping-cart.png")
        self.medecinereport_image = PhotoImage(file="Images/medecine-report.png")
        self.initialize()

    def initialize(self):
        self.root.title("Pharmacy Management System")
        self.root.configure(bg='white')
        self.root.state('zoomed')
        self.root.minsize(1135, 630)
        self.display()

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.time_now.config(text=string)
        self.time_now.after(1000, self.time)

    def display(self):

        c = conn.cursor()
        c.execute(
            "Select Employee_Name,Role_Name from employee where Employee_Username = '%s'" % self.username)
        for name, role in c:
            pass

        title = Label(self.root, pady=2, text="Welcome to SE Pharmacy", bd=12, bg='#a6b1f5', fg='white',
                      font=('times new roman', 35, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        F1 = Frame(self.root, bg='white')
        F1.pack(fill=X)

        top_left_Frame = Frame(F1, bg='white')
        top_left_Frame.pack(side='left', fill=X, padx=50)

        Label(top_left_Frame, image=self.user_image, bg='white').grid(row=0, column=0)
        Label(top_left_Frame, text=name, bg='white', font=('serif', 14, 'bold')).grid(row=1, column=0)
        Label(top_left_Frame, text=role, bg='white', font=('serif', 14, 'bold')).grid(row=2, column=0)

        top_right_Frame = Frame(F1)
        top_right_Frame.pack(side='right', fill=X, padx=50)

        logout_button = Button(top_right_Frame, text="Logout", width=10, font=('serif', 14, 'bold'), bg='#a6b1f5',
                               fg='white', command=self.logout)
        logout_button.grid(row=0, column=0)

        top_center_Frame = Frame(F1)
        top_center_Frame.pack(side='right', fill=X, padx=200)

        x = datetime.now()
        date_now = x.strftime('%d') + ' ,' + x.strftime('%B') + ' ,' + x.strftime('%Y')
        time_now = x.strftime('%X') + '  ' + x.strftime('%p')

        Label(top_center_Frame, text=date_now + " , ", bg='white', font=('Arial', 14, 'bold')).grid(row=0, column=0)
        self.time_now = Label(top_center_Frame, bg='white', font=('Arial', 14, 'bold'))
        self.time_now.grid(row=0, column=1, sticky='w')
        self.time()

        Mainframe = Frame(self.root, bg='white')
        Mainframe.pack(pady=50)

        medecine_button = Button(Mainframe, text="   Medicine          ", compound=LEFT, image=self.medicine_image,
                                 width=300, font=('serif', 20, 'bold'), command=self.medecine)
        medecine_button.grid(row=0, column=0, padx=30)
        sale_button = Button(Mainframe, text="    Sale                    ", compound=LEFT,
                             image=self.sale_image,
                             font=('serif', 20, 'bold'), width=300, command=self.sale)
        sale_button.grid(row=0, column=1)
        patient_button = Button(Mainframe, text="   Patient              ", compound=LEFT,
                                image=self.patient_image, font=('serif', 20, 'bold'), width=300,
                                command=self.patient)
        patient_button.grid(row=0, column=2)
        saleshistory_button = Button(Mainframe, text="   Sales History   ", compound=LEFT,
                                     image=self.saleshistory_image, font=('serif', 20, 'bold'), width=300,
                                     command=self.history_sales)
        saleshistory_button.grid(row=1, column=0, pady=30, padx=10)
        employee_button = Button(Mainframe, text="   Employee         ", compound=LEFT,
                                 image=self.employee_image,
                                 font=('serif', 20, 'bold'), width=300, command=self.employee)
        employee_button.grid(row=1, column=1)
        company_button = Button(Mainframe, text="   Company          ", compound=LEFT,
                                image=self.company_image,
                                font=('serif', 20, 'bold'), width=300, command=self.company)
        company_button.grid(row=1, column=2, padx=30)
        reports_button = Button(Mainframe, text="    Expiry Drug     ", compound=LEFT,
                                image=self.report_image,
                                font=('serif', 20, 'bold'), width=300, command=self.expiry_reports)
        reports_button.grid(row=2, column=0)
        medecinereports_button = Button(Mainframe, text="   Drug Reports    ", compound=LEFT,
                                        image=self.medecinereport_image, font=('serif', 20, 'bold'), width=300,
                                        command=self.medecine_reports)
        medecinereports_button.grid(row=2, column=1)
        suplliers_button = Button(Mainframe, text="    Quit        ", compound=LEFT,image=self.quit_image,
                                  font=('serif', 20, 'bold'), width=300, command=self.quit)
        suplliers_button.grid(row=2, column=2)

        if role == 'Employee':
            medecine_button.config(state=DISABLED)
            company_button.config(state=DISABLED)
            saleshistory_button.config(state=DISABLED)
            employee_button.config(state=DISABLED)
            reports_button.config(state=DISABLED)
            medecinereports_button.config(state=DISABLED)

    def medecine(self):
        os.system('Medicine.py')

    def sale(self):
        os.system('Sale.py')

    def patient(self):
        os.system('Patient.py')

    def employee(self):
        os.system('Employee.py')

    def history_sales(self):
        os.system('HistorySales.py')

    def company(self):
        os.system('Company.py')

    def expiry_reports(self):
        os.system('Expiry.py')

    def quit(self):
        op = messagebox.askyesno("Quit", "Do you want to quit?")
        if op > 0:
            c = conn.cursor()
            c.execute("update session set Date_logout=%s where Date_login=%s", (datetime.now(), self.date_now))
            c.execute("delete from currentuser where Employee_Username ='%s'" % self.username)
            self.root.destroy()
        else:
            return

    def medecine_reports(self):
        os.system('MedicineReports.py')

    def logout(self):
        c = conn.cursor()
        c.execute("update session set Date_logout=%s where Date_login=%s", (datetime.now(), self.date_now))
        c.execute("delete from currentuser where Employee_Username ='%s'" % self.username)
        self.root.destroy()



if __name__ == '__main__':
    root = Tk()
    gui = MainWindow(root)
    root.mainloop()
