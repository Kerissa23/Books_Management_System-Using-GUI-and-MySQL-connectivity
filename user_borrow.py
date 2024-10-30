import tkinter as tk
import tkinter.messagebox
import mysql
import mysql.connector
from tkinter import ttk

def borrow():

    def borrowed():
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="library")
        mycursor = mydb.cursor()
        sql="update books set Availability = 0 where Title = '"+book.get()+"'"
        mycursor.execute(sql)
        tkinter.messagebox.showinfo(title="Borrowed",message="This Book is Borrowed")
        mycursor.close()
        

    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="library")
    mycursor = mydb.cursor()
    sql="select * from books"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    mycursor.close()

    def populate_treeview(rows):
        data = rows
        for row in data:
            tree.insert("", tk.END, values=row)
    
    # Set up the main Tkinter window
    root = tk.Tk()
    book = tk.StringVar()
    root.title("User Data")
    root.geometry("600x400")

    # Set up the Treeview
    columns = ("Title", "Author", "Genre", "Published_Date", "Availability")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")
    tree.heading("Published_Date", text="Published_Date")
    tree.heading("Availability", text="Availability")
    tree.pack(fill=tk.BOTH, expand=True)

    # Populate Treeview with data from the database
    populate_treeview(rows)

    horizontal_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=horizontal_scrollbar.set)
    lbl = tk.Label(root,text="Enter BookName:")
    entry = tk.Entry(root,textvariable=book)
    btn = tk.Button(root,text="Borrow",command=borrowed)
    # Pack the Treeview and scrollbar
    tree.pack(fill=tk.BOTH, expand=True)
    horizontal_scrollbar.pack(fill=tk.X, side=tk.BOTTOM)
    lbl.pack(pady=5,side=tk.LEFT)
    entry.pack(pady=6,side=tk.LEFT)
    btn.pack(pady=6,side=tk.RIGHT)
    root.mainloop()
    

root2 = tk.Tk()
root2.title("Library")
style = ttk.Style()
style.theme_use("clam")  # Available themes: 'clam', 'default', 'alt', 'classic', etc.

# Configure styles for widgets
style.configure("TButton", font=("Helvetica", 12), padding=6, relief="flat", background="#1abc9c", foreground="white")
style.map("TButton", background=[("active", "#16a085")])  # Button background on hover

style.configure("TLabel", font=("Arial", 12), background="#ecf0f1", foreground="#2c3e50")
style.configure("TEntry", padding=5, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#34495e", foreground="white")
style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", rowheight=25)
    
lbl = ttk.Label(root2,text="Welcome to our Library Store").grid(row=1,column=0)
btn1 = ttk.Button(root2,text="Borrow Book",command=borrow).grid(row=2,column=0)
root2.geometry("400x400")
root2.mainloop()
