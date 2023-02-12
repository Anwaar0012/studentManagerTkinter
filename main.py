import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

# pymsql,pymysql.connector,sqlite 

win=tk.Tk()
win.geometry("1200x700")
win.config(bg="lightgrey",border=12,relief=tk.GROOVE)
win.title("Student Management System")
title_label=tk.Label(win,text="Student Management System",font="Arial 25 bold",bg="lightgrey",border=12,relief=tk.GROOVE)
title_label.pack(side=tk.TOP,fill=tk.X)

# Frames 
detail_frame=tk.LabelFrame(win,text="Enter your details",font="Arial 25",border=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=15,y=70,width=450,height=570)

data_frame=tk.Frame(win,border=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=465,y=80,width=705,height=562)

# ********** Variables **************
rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
fathername=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()
search_by=tk.StringVar()
# Labels and Entries 
rollno_label=tk.Label(detail_frame,text="Roll No   ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
rollno_label.grid(row=0,column=0,padx=2,pady=4,sticky=tk.W)

rollno_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=rollno)
rollno_entry.grid(row=0,column=1,padx=2,pady=4)

name_label=tk.Label(detail_frame,text="Name      ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
name_label.grid(row=1,column=0,padx=2,pady=4,sticky=tk.W)

name_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=name)
name_entry.grid(row=1,column=1,padx=2,pady=4)

class_label=tk.Label(detail_frame,text="Class     ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
class_label.grid(row=2,column=0,padx=2,pady=4,sticky=tk.W)

class_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=class_var)
class_entry.grid(row=2,column=1,padx=2,pady=4)

section_label=tk.Label(detail_frame,text="Section   ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
section_label.grid(row=3,column=0,padx=2,pady=4,sticky=tk.W)

section_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=section)
section_entry.grid(row=3,column=1,padx=2,pady=4)

contact_label=tk.Label(detail_frame,text="Contact   ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
contact_label.grid(row=4,column=0,padx=2,pady=4,sticky=tk.W)

contact_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=contact)
contact_entry.grid(row=4,column=1,padx=2,pady=4)

fathername_label=tk.Label(detail_frame,text="Father Name ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
fathername_label.grid(row=5,column=0,padx=2,pady=4,sticky=tk.W)

fathername_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=fathername)
fathername_entry.grid(row=5,column=1,padx=2,pady=4)

# address_label=tk.Label(detail_frame,text="Address",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
# address_label.grid(row=6,column=0,padx=2,pady=4,sticky=tk.NW)

# address_entry=tk.Text(detail_frame,width=20,height=6, font="Arial 17 bold",relief=tk.SUNKEN)
# address_entry.grid(row=6,column=1,padx=2,pady=4)

address_label=tk.Label(detail_frame,text="Address   ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
address_label.grid(row=6,column=0,padx=2,pady=4,sticky=tk.W)

address_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=address)
address_entry.grid(row=6,column=1,padx=2,pady=4)

gender_label=tk.Label(detail_frame,text="Gender    ",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
gender_label.grid(row=7,column=0,padx=2,pady=4,sticky=tk.W)

gender_combo=ttk.Combobox(detail_frame,font="Arial 15 bold",state="readonly",textvariable=gender)
gender_combo["values"]=("Male","Female","Others")
gender_combo.grid(row=7,column=1,padx=2,pady=4,sticky=tk.W)

dob_label=tk.Label(detail_frame,text="Date of Birth",font="Arial 17 bold",bg="lightgrey",relief=tk.SUNKEN)
dob_label.grid(row=8,column=0,padx=2,pady=4,sticky=tk.W)

dob_entry=tk.Entry(detail_frame,font="Arial 17 bold",relief=tk.SUNKEN,textvariable=dob)
dob_entry.grid(row=8,column=1,padx=2,pady=4)

# function to display data from mysql table
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
        # print(row)
    conn.close()
    
def add_func():
    if rollno.get() =="" or name.get() =="" or class_var.get() =="":
        messagebox.showerror('error','please fill all the fields')
    else:
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
        cur=conn.cursor()
        cur.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),fathername.get(),class_var.get(),section.get(),contact.get(),address.get(),gender.get(),dob.get()))
        conn.commit()
        conn.close()
        
        # this will fetch data as we add the data 
        fetch_data()
       
# get data on relese row and set into boxes      
def get_cursor(event):
     # this function fetch tha data of selected row 
     selected_row=student_table.focus()
     content=student_table.item(selected_row)
     row=content["values"]
     #  set the values of student table tree into our variables 
     rollno.set(row[0])
     name.set(row[1])
     fathername.set(row[2])
     class_var.set(row[3])
     section.set(row[4])
     contact.set(row[5])
     address.set(row[6])
     gender.set(row[7])
     dob.set(row[8])
    #  search_by.set(row[8])
    #  print(row)
          
 
def clear():
    # This function will clear all boxes enteries 
     rollno.set("")
     name.set("")
     fathername.set("")
     class_var.set("")
     section.set("")
     contact.set("")
     address.set("")
     gender.set("")
     dob.set("")
    
        
def update():
    conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
    cur=conn.cursor()
    cur.execute("UPDATE data SET name=%s,fathername=%s,class=%s,section=%s,contact=%s,address=%s,gender=%s,dob=%s WHERE rollno=%s",(name.get(),fathername.get(),class_var.get(),section.get(),contact.get(),address.get(),gender.get(),dob.get(),rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()
    
def delete():
    conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
    cur=conn.cursor()
    cur.execute("DELETE FROM data  WHERE rollno=%s",(rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()

        
    


# Buttons 
button_frame=tk.Frame(detail_frame,border=12,bg="lightgrey",relief=tk.GROOVE)
button_frame.place(x=10,y=380,width=400,height=132)

add_button=tk.Button(button_frame,text="Add",bg="lightgrey",font="Arial 13 bold",border=8,width=16,command=add_func)
add_button.grid(row=0,column=0,padx=3,pady=4)

update_button=tk.Button(button_frame,text="update",bg="lightgrey",font="Arial 13 bold",border=8,width=16,command=update)
update_button.grid(row=0,column=1,padx=4,pady=4)

delete_button=tk.Button(button_frame,text="Delete",bg="lightgrey",font="Arial 13 bold",border=8,width=16,command=delete)
delete_button.grid(row=1,column=0,padx=4,pady=4)

clear_button=tk.Button(button_frame,text="Clear",bg="lightgrey",font="Arial 13 bold",border=8,width=16,command=clear)
clear_button.grid(row=1,column=1,padx=4,pady=4)

search_frame=tk.Frame(data_frame,border=12,bg="lightgrey",relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_label=tk.Label(search_frame,text="Search",font="Arial 14 bold",bg="lightgrey",relief=tk.GROOVE)
search_label.grid(row=0,column=0,padx=2,pady=4)

search_combo=ttk.Combobox(search_frame,font="Arial 15 bold",state="readonly",textvariable=search_by)
search_combo["values"]=("Name","Roll No","contact","Father's Name","class","section","D.O.B")
search_combo.grid(row=0,column=1,padx=2,pady=4,sticky=tk.W)

search_button=tk.Button(search_frame,text="Search",bg="lightgrey",font="Arial 13 bold",border=8,width=12)
search_button.grid(row=0,column=2,padx=12,pady=4,sticky=tk.SE)

showall_button=tk.Button(search_frame,text="Show All",bg="lightgrey",font="Arial 13 bold",border=8,width=12)
showall_button.grid(row=0,column=3,padx=4,pady=4,sticky=tk.SE)

# Data Base Frame 
main_frame=tk.Frame(data_frame,bd=11,bg="lightgrey",relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Roll No","Name","Father's Name","Class","Section","Contact","Address","Gender","D.O.B"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)
y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)
student_table.heading("Roll No",text="Roll NO")
student_table.heading("Name",text="Name")
student_table.heading("Father's Name",text="Father's Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("Address",text="Address")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")
student_table['show']="headings"

student_table.column("Roll No",width=100)
student_table.column("Name",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("Address",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)
student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
# print(a)
student_table.bind("<ButtonRelease-1>",get_cursor)

win.mainloop()