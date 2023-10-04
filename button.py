from tkinter import *
from tkinter import messagebox

top =Tk()
top.geometry("600x800")

def fun1():
    messagebox.showinfo("heloo","red button clicked")
    print(" function created ")
def fun2(a,b):
    messagebox.showinfo("heloo","blue button clicked")
    print(a+b)

b1=Button(top,text="red", command=fun1,activeforeground= "red",activebackground="black")
b2=Button(top,text="blue", command=fun2(7,8),activeforeground= "blue",activebackground="black")

b1.pack()
b2.pack()
top.mainloop()

