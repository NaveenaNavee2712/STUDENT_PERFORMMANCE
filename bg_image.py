import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10 , 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")
plt.show()

# import matplotlib.pyplot as plt
#
# # x-coordinates of left sides of bars
# left = [1, 2, 3, 4, 5]
#
# # heights of bars
# height = [10, 24, 36, 40, 5]
#
# # labels for bars
# tick_label = ['one', 'two', 'three', 'four', 'five']
#
# # plotting a bar chart
# plt.bar(left, height, tick_label=tick_label,
#         width=0.8, color=['red', 'green'])
#
# # naming the x-axis
# plt.xlabel('x - axis')
# # naming the y-axis
# plt.ylabel('y - axis')
# # plot title
# plt.title('My bar chart!')
#
# # function to show the plot
# plt.show()




# import tkinter as tk
# from tkinter import ttk
#
# # Creating tkinter window
# window = tk.Tk()
# window.geometry('350x250')
# # Label
# ttk.Label(window, text="Select the Month :",
#           font=("Times New Roman", 10)).grid(column=0,
#                                              row=15, padx=10, pady=25)
#
# n = tk.StringVar()
# monthchoosen = ttk.Combobox(window, width=27,
#                             textvariable=n)
#
# # Adding combobox drop down list
# monthchoosen['values'] = (' January',
#                           ' February',
#                           ' March',
#                           ' April',
#                           ' May',
#                           ' June',
#                           ' July',
#                           ' August',
#                           ' September',
#                           ' October',
#                           ' November',
#                           ' December')
#
# monthchoosen.grid(column=1, row=15)
#
# # Shows february as a default value
# monthchoosen.current(1)
# window.mainloop()













# import tkinter
#
# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
#
# root = Tk()
#
# # Create a photoimage object of the image in the path
# image1 = Image.open("D:\\python\\student_performance\\images\\img1.png")
# test = ImageTk.PhotoImage(image1)
#
# label1 = tkinter.Label(image=test)
# label1.image = test
#
# # Position image
# label1.place(x=00, y=00)
#
#
#
# label1 = tkinter.Label(image=test)
#
# label1.place(x=00, y=00)
#
#
# root.mainloop()




# from tkinter.ttk import Label
#
# from PIL import Image, ImageTk
# import tkinter as tk
#
# IMAGE_PATH = 'img1.png'
# WIDTH, HEIGTH = 200, 200
#
# root = tk.Tk()
# root.geometry('{}x{}'.format(WIDTH, HEIGTH))
#
# canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
# canvas.pack()
#
# img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
# canvas.background = img  # Keep a reference in case this code is put in a function.
# bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
#
# # Put a tkinter widget on the canvas.
# button = tk.Button(root, text="Start")
# button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)
#
# root.mainloop()