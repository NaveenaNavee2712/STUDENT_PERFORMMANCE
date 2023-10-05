from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt1
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function





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




def good():
    TableMargin = Frame(ann_data_main, width=400)
    TableMargin.place(x=170, y=110, width=455, height=205)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO", "NAME", "CGPA", "M_MARK", "PPG"), height=400,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
    tree.delete()
    file = "data_set/select_values.csv"
    with open(file) as f, open('data_set/Good.csv', 'w') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO", "NAME", "CGPA", "M_MARK", "PPG"])
        number1=0
        for row in reader:
            # print row
            t11 = row['RNO']
            t12 = row['NAME']
            t13 = row['CGPA']
            t14 = row['M_MARK']
            t15 = row['PPG']
            val = float(t13)
            if (val >= 7.2):
                number1 +=1
                tree.insert("", 0, values=(t11, t12, t13, t14, t15))
                filewriter.writerow([t11, t12, t13, t14, t15])
            else:
                print()
        data = {'Grade': ['Good'],
                'Values': [number1]
                }
        df = pd.DataFrame(data, columns=['Grade', 'Values'])

        df.plot(x='Grade', y='Values', kind='bar')
        plt.show()

def average():
    TableMargin = Frame(ann_data_main, width=400)
    TableMargin.place(x=170, y=110, width=455, height=205)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO", "NAME", "CGPA", "M_MARK", "PPG"), height=400,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
    tree.delete()
    file = "data_set/select_values.csv"
    with open(file) as f, open('data_set/agverage.csv', 'w') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO", "NAME", "CGPA", "M_MARK", "PPG"])
        number2 =0
        for row in reader:
            # print row
            t11 = row['RNO']
            t12 = row['NAME']
            t13 = row['CGPA']
            t14 = row['M_MARK']
            t15 = row['PPG']

            val = float(t13)
            if ((val >= 5.0)and(val <= 7.2)):
                number2 +=1
                tree.insert("", 0, values=(t11, t12, t13, t14, t15))
                filewriter.writerow([t11, t12, t13, t14, t15])
            else:
                print()
        data = {'Grade': ['Average'],
                'Values': [number2]
                }
        df = pd.DataFrame(data, columns=['Grade', 'Values'])

        df.plot(x='Grade', y='Values', kind='bar')
        plt.show()




def poor():
    TableMargin = Frame(ann_data_main, width=400)
    TableMargin.place(x=170, y=110, width=455, height=205)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("RNO", "NAME", "CGPA", "M_MARK", "PPG"), height=400,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
    tree.delete()
    file = "data_set/select_values.csv"
    with open(file) as f, open('data_set/poor.csv', 'w') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO", "NAME", "CGPA", "M_MARK", "PPG"])
        number3 = 0
        for row in reader:
            # print row
            t11 = row['RNO']
            t12 = row['NAME']
            t13 = row['CGPA']
            t14 = row['M_MARK']
            t15 = row['PPG']

            val=float(t13)

            if (val<=5.0):
                number3 +=1
                tree.insert("", 0, values=(t11, t12, t13, t14, t15))
                filewriter.writerow([t11, t12, t13, t14, t15])
            else:
                print()

        data = {'Grade': ['Poor'],
                'Values': [number3]
                }
        df = pd.DataFrame(data, columns=['Grade', 'Values'])

        df.plot(x='Grade', y='Values', kind='bar')
        plt.show()


def next_page():
    ann_data_main.destroy()

def read_data_set1():

    TableMargin = Frame(ann_data_main, width=400)
    TableMargin.place(x=170, y=110,width=455, height=205)
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
    file="data_set/select_values.csv"
    with open(file) as f, open('data_set/svm.csv', 'w') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["RNO","NAME","CGPA","M_MARK","PPG"])
        count1 = 0
        count2 = 0
        count3 = 0
        for row in reader:
            #print row
            t11 = row['RNO']
            t12 = row['NAME']
            t13 = row['CGPA']
            t14 = row['M_MARK']
            t15 = row['PPG']

            tree.insert("", 0, values=(t11,t12,t13,t14,t15))
            filewriter.writerow([t11,t12,t13,t14,t15])
            val = float(t13)

            if (val >= 7.2):
                count1 +=1
                # print(count1)

            if ((val >= 5.0) and (val <= 7.2)):
                count2 += 1
                print(count2)

            if (val <= 5.0):
                count3 +=1
                # print("P"count3)


    data = {'Grade': ['Goood','Average','Poor'],
        'Values': [count1,count2,count3]
            }
    df = pd.DataFrame(data, columns=['Grade', 'Values'])

    df.plot(x='Grade', y='Values', kind='bar')

    plt.show()



############################################################
ann_data_main = Tk()
w=750
h=550
ws = ann_data_main.winfo_screenwidth()
hs = ann_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ann_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
ann_data_main.title(sample_data.title)
ann_data_main.configure(background=sample_data.background)
########################################################### Element design


message = Label(ann_data_main, text=sample_data.titlec,fg="#003366",bg=sample_data.background, width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(ann_data_main, text="Classification",width=20,command=read_data_set1  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=120, y=400)

resust_dataset = Button(ann_data_main , text="Grade Prediction( Good )",width=20,command=good  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)


resust_dataset = Button(ann_data_main,text="Grade Prediction( Average )",width=20,command=average  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=120, y=450)

resust_dataset = Button(ann_data_main , text="Grade Prediction( Poor )",width=20,command=poor  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=450)

resust_dataset = Button(ann_data_main , text="Close",width=20,command=next_page  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=270, y=500)



ann_data_main.mainloop()

