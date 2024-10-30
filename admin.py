import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def adminn():

    def display_data(tree, data, columns):
    
        for item in tree.get_children():
            tree.delete(item)
    
        for row in data:
            tree.insert("", tk.END, values=row)


    def view_all_users():
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="library")
        if connection:
            cursor = connection.cursor()
            cursor.execute("Select * from users")
            rows = cursor.fetchall()
            connection.close()
        
            # Set Treeview columns and display data
            tree["columns"] = ("FirstName", "LastName", "Email", "Phone", "Password")
            tree.heading("FirstName", text="FirstName")
            tree.heading("LastName", text="LastName")
            tree.heading("Email", text="Email")
            tree.heading("Phone", text="Phone")
            tree.heading("Password", text="Password")
            display_data(tree, rows, ("FirstName", "LastName", "Email", "Phone", "Password"))


    def view_all_books():
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="library")
        if connection:
            cursor = connection.cursor()
            cursor.execute("Select * from books")
            rows = cursor.fetchall()
            connection.close()

            # Set Treeview columns and display data
            tree["columns"] = ("Title", "Author", "Genre", "Date", "Availability")
            tree.heading("Title", text="Title")
            tree.heading("Author", text="Author")
            tree.heading("Genre", text="Genre")
            tree.heading("Date", text="Date")
            tree.heading("Availability", text="Availability")
            display_data(tree, rows, ("Title", "Author", "Genre", "Date", "Availability"))


    def view_all_borrowed_books():
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="library")
        if connection:
            cursor = connection.cursor()
            cursor.execute("Select * from borrow")
            rows = cursor.fetchall()
            connection.close()
            tree["columns"] = ("Username", "BookName", "Borrow Date", "Due Date","Return Date")

            tree.heading("Username", text="Username")
            tree.heading("BookName", text="BookName")
            tree.heading("Borrow Date", text="Borrow Date")
        
            tree.heading("Due Date", text="Due Date")
            tree.heading("Return Date", text="Return Date")
            display_data(tree, rows, ("Username", "Book Name", "Due Date", "Borrow Date","Return Date"))


    admin1 = tk.Tk()
    admin1.title("Admin Page")
    admin1.geometry("700x500")
    tree = ttk.Treeview(admin1, show="headings")
    tree.place(x=10, y=150, width=680, height=300)
    # Configure Treeview scrollbars
    tree_scroll_y = ttk.Scrollbar(admin1, orient="vertical", command=tree.yview)
    tree_scroll_y.place(x=690, y=150, height=250)

    tree_scroll_x = ttk.Scrollbar(admin1, orient="horizontal", command=tree.xview)
    tree_scroll_x.place(x=10, y=400, width=680)

    tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

    btn_users = tk.Button(admin1, text="View All Users", command=view_all_users)
    btn_users.place(x=10, y=50, width=150, height=30)
    btn_books = tk.Button(admin1, text="View All Books", command=view_all_books)
    btn_books.place(x=180, y=50, width=150, height=30)
    btn_borrowed_books = tk.Button(admin1, text="View All Borrowed Books", command=view_all_borrowed_books)
    btn_borrowed_books.place(x=350, y=50, width=200, height=30)
    admin1.mainloop()
adminn()
