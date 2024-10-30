import tkinter as tk
import tkinter.messagebox
import mysql.connector
from tkinter import ttk

def signup():

    def signupp():
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "library")
        mycursor = mydb.cursor()
        sql = "insert into users values ('"+user.get()+"','"+lastname.get()+"','"+email.get()+"',"+str(phone.get())+",'"+password.get()+"')"
        mycursor.execute(sql)
        mydb.commit()
        print("Successful Sign up")

    root1 = tk.Tk()
    root1.configure(bg="#ecf0f1")

    root1.title("Sign-up")
    # Apply a theme for ttk widgets
    style = ttk.Style()
    style.theme_use("clam")  # Available themes: 'clam', 'default', 'alt', 'classic', etc.

    # Configure styles for widgets
    style.configure("TButton", font=("Helvetica", 12), padding=6, relief="flat", background="#1abc9c", foreground="white")
    style.map("TButton", background=[("active", "#16a085")])  # Button background on hover

    style.configure("TLabel", font=("Arial", 12), background="#ecf0f1", foreground="#2c3e50")
    style.configure("TEntry", padding=5, font=("Arial", 10))
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#34495e", foreground="white")
    style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", rowheight=25)
    user = tk.StringVar()
    lastname = tk.StringVar()
    email = tk.StringVar()
    phone = tk.IntVar()
    password = tk.StringVar()
    lbluser = ttk.Label(root1,text="Enter UserName:").grid(row=0,column=0,padx=10,pady=5,sticky="W")
    ttk.Entry(root1,textvariable=user).grid(row=0,column=1)
    lblsurname = ttk.Label(root1,text="Enter LastName").grid(row=1,column=0,padx=10,pady=5,sticky="W")
    ttk.Entry(root1,textvariable=lastname).grid(row=1,column=1,padx=10,pady=5)
    lblmail = ttk.Label(root1,text="Email:").grid(row=2,column=0,padx=10,pady=5,sticky="W")
    ttk.Entry(root1,textvariable=email).grid(row=2,column=1,padx=10,pady=5)
    lblphone = ttk.Label(root1,text="Phone:").grid(row=3,column=0,padx=10,pady=5,sticky="W")
    ttk.Entry(root1,textvariable=phone).grid(row=3,column=1,padx=10,pady=5)
    lblpass = ttk.Label(root1,text="Password:").grid(row=4,column=0,padx=10,pady=5,sticky="W")
    ttk.Entry(root1,textvariable=password).grid(row=4,column=1,padx=10,pady=5)
    btn = ttk.Button(root1,text="Sign-up",command=signupp).grid(row=5,column=0,padx=10,pady=5)
    root1.geometry("400x400")
    root1.mainloop()
    # def signupp():
    #     mydb = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "library")
    #     mycursor = mydb.cursor()
    #     sql = "insert into users values ('"+user.get()+"','"+lastname.get()+"','"+email.get()+"',"+str(phone.get())+",'"+password.get()+"')"
    #     mycursor.execute(sql)
    #     mydb.commit()
    #     print("Successful Sign up")
    
    
    # btn = tk.Button(root1,text="Sign-up",command=signupp).grid(row=5,column=0)
    # root1.geometry("400x400")
    # root1.mainloop()  
    # mydb = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "library")
    # mycursor = mydb.cursor()
    # sql = "insert into users values ('"+user.get()+"','"+lastname.get()+"','"+email.get()+"',"+str(phone.get())+",'"+password.get()+"')"
    # mycursor.execute(sql)
    # mydb.commit()
    # print("Successful Sign up")


# root1 = tk.Tk()
# user = tk.StringVar()
# lastname = tk.StringVar()
# email = tk.StringVar()
# phone = tk.IntVar()
# password = tk.StringVar()

# root1.title("Sign-up")
# lbluser = tk.Label(root1,text="Enter UserName:").grid(row=0,column=0)
# tk.Entry(root1,textvariable=user).grid(row=0,column=1)
# lblsurname = tk.Label(root1,text="Enter LastName").grid(row=1,column=0)
# tk.Entry(root1,textvariable=lastname).grid(row=1,column=1)
# lblmail = tk.Label(root1,text="Email:").grid(row=2,column=0)
# tk.Entry(root1,textvariable=email).grid(row=2,column=1)
# lblphone = tk.Label(root1,text="Phone:").grid(row=3,column=0)
# tk.Entry(root1,textvariable=phone).grid(row=3,column=1)
# lblpass = tk.Label(root1,text="Password:").grid(row=4,column=0)
# tk.Entry(root1,textvariable=password).grid(row=4,column=1)
# btn = tk.Button(root1,text="Sign-up",command=signup).grid(row=5,column=0)
# root1.geometry("400x400")
# root1.mainloop()  
