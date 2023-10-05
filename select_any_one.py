import urllib
from tkinter import *
import os
import urllib.request
import urllib.parse
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
    f_filepath="dataset_1.csv"
    key=202012
    f_path=""
    f_name=""
    data=[]
    data1=[]
    data2=[]


########################################################### function
def next_page():
    select_any_one_main.destroy()
    import classification


def read_data_set():
    selet_value=box_value.get()
    print(selet_value)
    TableMargin = Frame(select_any_one_main, width=500)
    TableMargin.place(x=50, y=110,width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO", "NAME", "CLASS", "GENDER", "CGPA", "M_MARK", "PPG", "AT", "CT", "TT"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('RNO', text="A", anchor=W)
    tree.heading('NAME', text="B", anchor=W)
    tree.heading('CLASS', text="C", anchor=W)
    tree.heading('GENDER', text="D", anchor=W)
    tree.heading('CGPA', text="E", anchor=W)

    tree.heading('M_MARK', text="F", anchor=W)
    tree.heading('PPG', text="G", anchor=W)
    tree.heading('AT', text="H", anchor=W)
    tree.heading('CT', text="I", anchor=W)
    tree.heading('TT', text="J", anchor=W)



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
    file="data_set/missing.csv"
    with open(file) as f, open('data_set/select_values.csv', 'w') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO", "NAME","CGPA","M_MARK","PPG","AT","CT","TT"])
        for row in reader:
            #print (row)
            t1 = row['RNO']
            t2 = row['NAME']
            t5 = row['CGPA']
            t6 = row['M_MARK']
            t7 = row['PPG']
            t8 = row['AT']
            t9 = row['CT']
            t10 = row['TT']

            # if ((t1=="RNO")):
            #     print("Incon"+str(selet_value))
            #     tree.insert("", 0, values=(t1))
            #     filewriter.writerow([t1])
            # elif ((t5=="CGPA")):
            #     print ("noo")
            #     tree.insert("", 0, values=(t5))
            #     filewriter.writerow([t1])

            if ((t1==selet_value)or(t2==selet_value)or(t5==selet_value)or(t6==selet_value)or(t7==selet_value)or(t8==selet_value)or(t9==selet_value)or(t10==selet_value)):
                #l=0#print "yes"
                tree.insert("", 0, values=(t1, t2, t5, t6, t7, t8, t9, t10))
                filewriter.writerow([t1, t2, t5, t6, t7, t8, t9, t10])
            else:
                #select_any_one_main.destroy()
                tree.insert("", 0, values=(t1,t2,t5,t6,t7,t8,t9,t10))
                filewriter.writerow([t1,t2,t5,t6,t7,t8,t9,t10])

############################################################
select_any_one_main = Tk()
w=750
h=550
ws = select_any_one_main.winfo_screenwidth()
hs = select_any_one_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
select_any_one_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
select_any_one_main.title(sample_data.title)
select_any_one_main.resizable(False, False)
select_any_one_main.configure(background=sample_data.background)
########################################################### Element design


message = Label(select_any_one_main, text=sample_data.titlec,fg="#003366",bg=sample_data.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

message1 = Label(select_any_one_main, text="Select",fg="#003366",bg=sample_data.background, width=35,height=3, font=('times', 30, 'italic bold '))
message1.place(x=00, y=5)

box_value = StringVar()
value = ttk.Combobox(select_any_one_main,width=27,textvariable=box_value)

value['values'] = (' RNO',
                          ' CGPA',
                          ' M_MARK',
                          ' PPG',
                          ' AT',
                          ' CT',
                          ' TT')

value.grid(column=3, row=15)
value.place(x=300, y=250)
value.current(1)



compare_dataset = Button(select_any_one_main, text="SELECT",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(select_any_one_main,command=next_page , text="NEXT",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

select_any_one_main.mainloop()
