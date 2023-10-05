from tkinter import *
import os

import csv

from tkinter import *
import tkinter.ttk as ttk
import csv

#######################################################class function
class sample_data:
    name="arun"
    title="Student Performance Prediction"
    titlec="STUDENT PERFORMANCE"
    total_record=0
    background='#66FFFF'
    #background='yellow'
    f_filepath="dataset_1.csv"
    key=202012
    f_path=""
    f_name=""
    data=[]
    data1=[]
    data2=[]

########################################################### function
def next_page():
    attribut_extraction_data_main.destroy()
    import select_any_one

def read_data_set():
    TableMargin = Frame(attribut_extraction_data_main, width=500)
    TableMargin.place(x=50, y=110,width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO","NAME","CGPA","M_MARK","PPG"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('RNO', text="RNO", anchor=W)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('CGPA', text="CGPA", anchor=W)
    tree.heading('M_MARK', text="M_MARK", anchor=W)
    tree.heading('PPG', text="PPG", anchor=W)


    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)




    tree.pack()
    ob=sample_data
    file="data_set/missing.csv"
    with open(file) as f, open('data_set/attributes.csv', 'w') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO","NAME","CGPA","M_MARK","PPG"])
        for row in reader:
            #print row
            t1 = row['RNO']
            t2 = row['NAME']
            t3 = row['CGPA']
            t4 = row['M_MARK']
            t5 = row['PPG']


            tree.insert("", 0, values=(t1,t2,t3,t4,t5))
            filewriter.writerow([t1,t2,t3,t4,t5])

############################################################
attribut_extraction_data_main = Tk()
w=750
h=550
ws = attribut_extraction_data_main.winfo_screenwidth()
hs = attribut_extraction_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
attribut_extraction_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
attribut_extraction_data_main.title(sample_data.title)
attribut_extraction_data_main.resizable(False, False)
attribut_extraction_data_main.configure(background=sample_data.background)

########################################################### Element design


message = Label(attribut_extraction_data_main, text=sample_data.titlec,bg=sample_data.background,fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(attribut_extraction_data_main, text="Feature Extraction",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(attribut_extraction_data_main,command=next_page , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

attribut_extraction_data_main.mainloop()
