from pyrecord import Record
from pyrecord import Records
from pycategory import Categories
import sys
import tkinter as tk

records = Records()
categories = Categories()
root = tk.Tk()
root.title('Pymoney')
f = tk.Frame(root,borderwidth = 5)
f.grid(row = 0,column = 0)

#function
def update():
    ini_money = up_money.get()
    records._money = int(ini_money)
    money.set(records._money)

def add():
    try:
        record = add_var.get()
        try:
            records.add(str(record),categories)
        except:
            return
        i = len(records._records)-1
        lb.insert(i+1,'%10s %-15s %-15s %-5s' %(str(records._records[i]._date),str(records._records[i]._category),str(records._records[i]._acti),str(records._records[i]._cost)))
        money.set(records._money)
    except:
        return


def delete():
    index = lb.curselection()
    i = int(index[0])
    records.delete(' '.join([records._records[i]._category,records._records[i]._acti,records._records[i]._cost]))
    lb.delete(0,tk.END)
    for i,w in enumerate(records._records):
        lb.insert(i,'%-10s %-15s %-15s %-5s' %(str(w._date),str(w._category),str(w._acti),str(w._cost)))
    money.set(records._money)
    
def find_sub():
    cate = find_var.get()
    if len(cate) == 0:
        return
    cate = str(cate)
    result = categories.find_subcategories(cate)
    temp = records.find(result)
    lb.delete(0,tk.END)
    for i,w in enumerate(temp[1]):
        lb.insert(i,'%-10s %-15s %-15s %-5s' %(str(w._date),str(w._category),str(w._acti),str(w._cost)))
    money.set(temp[0])

def reset():
    lb.delete(0,tk.END)
    for i,w in enumerate(records._records):
        lb.insert(i,'%-10s %-15s %-15s %-5s' %(str(w._date),str(w._category),str(w._acti),str(w._cost)))
    money.set(records._money)


def view_cate():
    temp =[]
    temp = categories.view()
    lb.delete(0,tk.END)
    for i,w in enumerate(temp):
        lb.insert(i,str(w))


#view categories
cate_btn = tk.Button(f,text = 'Categories' ,command = view_cate)
cate_btn.grid(row = 1,column = 15)

#delete button
del_btn = tk.Button(f,text = 'Delete',command = delete)
del_btn.grid(row = 1,column = 14)

#set title
title = tk.Label(f,text = 'Pymoney',font =('Courier',15) )
title.grid(row = 1,column = 0)

#list box
lb = tk.Listbox(f,width = 60 , font = ('Courier' , 10))
for i,w in enumerate(records._records):
    lb.insert(i,'%-10s %-15s %-15s %-5s' %(str(w._date),str(w._category),str(w._acti),str(w._cost)))
lb.grid(row = 1,column = 10,columnspan = 4 ,pady = 5,sticky = tk.W + tk.N)

#find feature
find_var = tk.StringVar()
find_entry = tk.Entry(f,textvariable = find_var)
find_entry.grid(row = 10,column = 10)
find_sub_btn = tk.Button(f,text = 'Find',command = find_sub)
find_sub_btn.grid(row = 10,column = 11)
find_label = tk.Label(f,text = 'Find categories:')
find_label.grid(row = 10,column = 8)
#reset to original record
reset_btn = tk.Button(f,text = 'Reset',command = reset)
reset_btn.grid(row = 10,column = 12)

#exit button
quick_button = tk.Button(f,text = 'Exit',command = root.destroy)
quick_button.grid(row = 20,column = 10)

#add feature
add_var = tk.StringVar()
add_entry = tk.Entry(f,textvariable = add_var)
add_entry.grid(row = 15,column = 10)
add_btn = tk.Button(f,text = 'Add',command = add)
add_btn.grid(row = 15,column = 11)
add_label = tk.Label(f,text = 'Add item:')
add_label.grid(row = 15, column = 8)
#Show amount
money = tk.StringVar()
money.set(records._money)
money_label = tk.Label(f,textvariable = money,font = ('Courier',13))
money_label.grid(row = 20,column = 1)
bmoney_label = tk.Label(f,text = 'The total is $',font = ('Courier',13))
bmoney_label.grid(row = 20,column = 0)

#update feature
up_money = tk.StringVar()
up_money_entry = tk.Entry(f,textvariable = up_money)
up_money_entry.grid(row = 15,column = 14)
init_btn = tk.Button(f,text ='Update',command = update)
init_btn.grid(row = 15,column = 15)
init_label = tk.Label(f,text = 'Enter an amount:')
init_label.grid(row = 15, column = 13)

#mainloop
tk.mainloop()
records.save()

