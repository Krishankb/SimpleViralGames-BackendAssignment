from tkinter import * 
from backend import Database

database = Database()
selected_tuple =None

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(name_text.get(),url_text.get(),author_text.get(),published_date_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(name_text.get(),url_text.get(),author_text.get(),published_date_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),url_text.get(),author_text.get(),published_date_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],name_text.get(),url_text.get(),author_text.get(),published_date_text.get())

window = Tk()
window.wm_title("Games")

l1 = Label(window,text = "Name")
l1.grid(row = 0,column = 0)

l2 = Label(window,text= "URL")
l2.grid(row = 0, column = 2 )

l3 = Label(window,text= "Author")
l3.grid(row = 1, column = 0 )

l4 = Label(window,text= "Published Date")
l4.grid(row = 1, column = 2 )

name_text = StringVar()
e1= Entry(window,textvariable=name_text)
e1.grid(row = 0 , column=1)

url_text = StringVar()
e2= Entry(window,textvariable=url_text)
e2.grid(row = 0 , column=3)

author_text = StringVar()
e3= Entry(window,textvariable=author_text)
e3.grid(row = 1, column=1)

published_date_text = StringVar()
e4= Entry(window,textvariable=published_date_text)
e4.grid(row = 1, column=3)

list1= Listbox(window,height= 9,width = 30)
list1.grid(row = 2,column= 0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row= 2, column=2,rowspan=6,sticky='ns')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2=Scrollbar(window,orient='horizontal')
sb2.grid(row=8,column=1,sticky='ns')

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=10,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=10,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=10,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Entry",width=10,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Entry",width=10,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="close",width=10,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()