import tkinter as tk
import mysql.connector
import tkinter.messagebox
from sign_up import signup
from tkinter import ttk


def admin():
    def authenticate():
        if admin.get() == "admin" and password1.get()=="admin123":
            tkinter.messagebox.showinfo(title="Valid",message="Welcome")
            with open("admin.py") as f:
                code = f.read()
                exec(code)
        else:
            tkinter.messagebox.showinfo(title="Not Authorized",message="Please Try Again.")
    root4 = tk.Tk()
    admin = tk.StringVar(root4)
    password1 = tk.StringVar(root4)
    root4.title("Admin Page")
    lblname = tk.Label(root4,text="Enter AdminName:").grid(row=1,column=0)
    tk.Entry(root4,textvariable=admin).grid(row=1,column=1)
    lblpass = tk.Label(root4,text="Enter Password:").grid(row=2,column=0)
    tk.Entry(root4,show='*',textvariable=password1).grid(row=2,column=1)
    btn = tk.Button(root4,text="Login",command=authenticate).grid(row=3,column=0)
    root4.geometry("400x400")
    root4.mainloop()


def sign_in():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "library")
    mycursor = mydb.cursor()
    sql = "select * from users where FirstName = '"+user.get()+"' and Password = '"+password.get()+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if result != []:
        tkinter.messagebox.showinfo(title="Valid",message="Welcome")
        with open("user_borrow.py") as f:
            code = f.read()
            exec(code)
    else:
        tkinter.messagebox.showinfo(title="NotValid",message="Incorrect Username or Password")



root = tk.Tk()
user = tk.StringVar()
password = tk.StringVar()
root.title("Library Management System Login")

# Apply a theme for ttk widgets
style = ttk.Style()
style.theme_use("alt")  # Available themes: 'clam', 'default', 'alt', 'classic', etc.

# Configure styles for widgets
style.configure("TButton", font=("Helvetica", 12), padding=6, relief="flat", background="#1abc9c", foreground="white")
style.map("TButton", background=[("active", "#16a085")])  # Button background on hover

style.configure("TLabel", font=("Arial", 12), background="#ecf0f1", foreground="#2c3e50")
style.configure("TEntry", padding=5, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#34495e", foreground="white")
style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", rowheight=25)

lbluser = ttk.Label(text="UserName").grid(row=1,column=0)
ttk.Entry(textvariable=user).grid(row=1,column=2)
lblpassword = ttk.Label(text = "Password").grid(row=3,column=0)
ttk.Entry(show='*',textvariable=password).grid(row=3,column=2)

btn = ttk.Button(text="Sign in",command=sign_in).grid(row=5,column=1)
btn1 = ttk.Button(text="Sign up",command=signup).grid(row = 5,column=2)
btn2 = tk.Button(text="admin",command=admin).grid(row=7,column=0)
root.geometry("400x400")
root.mainloop()
