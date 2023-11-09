from tkinter import *


my_window = Tk()
my_canvas = Canvas(my_window, width=400, height=400, background='white')
my_canvas.grid(row=0, column=0)
my_canvas.create_line(0, 0, 400, 400, fill='red', width=5)
my_canvas.create_line(400, 0, 0, 400, fill='green', width=10)
my_canvas.create_line(200, 0, 200, 400, fill='blue', width=15)
my_canvas.create_line(0, 200, 400, 200, fill='purple', width=20)

my_window.mainloop()
