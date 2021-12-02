# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:49:55 2021

@author: Lenovo
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("Html Ide")
root.config(bg="light grey")

img1=ImageTk.PhotoImage(Image.open("open.png"))
img2=ImageTk.PhotoImage(Image.open("save.png"))
img3=ImageTk.PhotoImage(Image.open("run.png"))

name=""
html_file=""

def open_file() :
    global name,html_file
    b.delete(0,END)
    c.delete(1.0,END)
    html_file=filedialog.askopenfilename(title="Open a File",filetypes=(('Html Files','*.html'),))
    print(html_file)
    name=os.path.basename(html_file)
    formatted_name=name.split('.')[0]
    b.insert(END,formatted_name)
    root.title(formatted_name)
    html_file=open(name,'r')
    par=html_file.read()
    c.insert(END,par)
    html_file.close()
    
def save() :
    tit=b.get()
    htmlf=open(tit+'.html','w')
    data=c.get("1.0",END)
    htmlf.write(data)
    b.delete(0,END)
    c.delete(1.0,END)
    messagebox.showinfo("Info","File is saved in the same folder")
    
def run() :
    """atit=b.get()
    ahtmlf=open(atit+'.html','w')
    adata=c.get("1.0",END)
    ahtmlf.write(adata)
    path='file://' + os.path.basename(html_file)
    apath=path.split('.')[0]"""
    f = open(name, 'w')
    html_template = c.get("1.0",END)
    f.write(html_template)
    f.close()
    filename = 'file://' +os.getcwd()+'/'+name
    webbrowser.open_new_tab(filename)
    
a=Label(root,text="File name :- ",font=('Courier',15),bg="light grey")
a.place(relx=0.45,rely=0.08,anchor=CENTER)

b=Entry(root,font=('Courier',15))
b.place(relx=0.75,rely=0.08,anchor=CENTER)

c=Text(root,font=('Courier',15),height=23,width=52)
c.place(relx=0.5,rely=0.58,anchor=CENTER)

btn1=Button(root,image=img1,command=open_file)
btn1.place(relx=0.1,rely=0.08,anchor=CENTER)

btn2=Button(root,image=img2,command=save)
btn2.place(relx=0.18,rely=0.08,anchor=CENTER)

btn3=Button(root,image=img3,width=30,height=30,command=run)
btn3.place(relx=0.26,rely=0.08,anchor=CENTER)

root.mainloop()