
import os

import csv
#import sample_data
from tkinter import *
import tkinter.ttk as ttk
import csv

class sample_data:
    name="arun"
    title="Student Performance Prediction"
    titlec="STUDENT PERFORMANCE"
    total_record=0
    background='#66FFFF'
    #background='yellow'
    f_filepath="dataset\\dataset_1.csv"
    key=202012
    f_path=""
    f_name=""
    data=[]
    data1=[]
    data2=[]


########################################################### function
def read_data_set():

    TableMargin = Frame(read_data_main, width=500)
    TableMargin.place(x=50, y=110,width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO", "NAME", "CLASS", "GENDER","CGPA","M_MARK","PPG","AT","CT","TT"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('RNO', text="RNO", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('CLASS', text="CLASS", anchor=W)
    tree.heading('GENDER', text="GENDER", anchor=W)
    tree.heading('CGPA', text="CGPA", anchor=W)
    tree.heading('M_MARK', text="M_MARK", anchor=W)

    tree.heading('PPG', text="PPG", anchor=W)
    tree.heading('AT', text="AT", anchor=W)
    tree.heading('CT', text="CT", anchor=W)
    tree.heading('TT', text="TT", anchor=W)



    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=200)
    tree.column('#8', stretch=NO, minwidth=0, width=200)
    tree.column('#9', stretch=NO, minwidth=0, width=0)



    tree.pack()
    ob=sample_data
    file=ob.f_filepath

    with open(file) as f :
        reader = csv.DictReader(f, delimiter=',')

        for row in reader:
            t1 =row['RNO']
            t2 = row['NAME']
            t3 = row['CLASS']
            t4 = row['GENDER']
            t5 = row['CGPA']
            t6 = row['M_MARK']
            t7 = row['PPG']
            t8 = row['AT']

            t9 = row['CT']
            t10 = row['TT']


            tree.insert("", 0, values=(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10))
def next_page1():
    read_data_main.destroy()
    import missing_values

############################################################
read_data_main = Tk()
w=750
h=550
ws = read_data_main.winfo_screenwidth()
hs = read_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
read_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))

read_data_main.title(sample_data.title)
read_data_main.resizable(False, False)
read_data_main.configure(background=sample_data.background)
########################################################### Element design


message = Label(read_data_main, text=sample_data.titlec,bg=sample_data.background,fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(read_data_main, text="Read Data",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(read_data_main, text="Next",command=next_page1,width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

read_data_main.mainloop()
