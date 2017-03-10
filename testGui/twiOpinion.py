# -*- coding: utf-8 -*-
import Tkinter as tk
import subprocess
from versionControl import greeting
from versionControl import startingInfo 
from guiConfiguration import configuration 
from guiCrawling import crawling
from guiLabeling import labeling
from guiLearning import learning 
from guiInfo import info
import os

start_bt_ms = "Welcome! Contact zhiyao: xiezhiyaoa@gmail.com" 

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Return>', self.click_ok)
        self.master.bind('<Escape>', self.click_cancel)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        tk.Message(self, text= greeting(),
                   font='System 18 bold', justify='left', aspect=800).pack(pady=(5, 0))
        tk.Message(self, text= "Procedures in twiOpinion:",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame last 
        f1_5 = tk.Frame(self)
        f1_5.pack(padx=60, pady=(5,0), anchor='w')

        self.var = tk.IntVar()

        tk.Label(f1_5, text= 'Select the function you want: ( •̀ .̫ •́ )✧'
                ).grid(row=0,column=0,columnspan=9,sticky='w')

        tk.Label(f1_5, font=("Courier", 8), text= ' ').grid(row=1,column=0,columnspan=9,sticky='w')

        R1 = tk.Radiobutton(f1_5, text="Step 0. Twitter Accessing Setting", variable=self.var, value=1
              ).grid(row=2, column=0,sticky='w')
        R2 = tk.Radiobutton(f1_5, text="Step 1. Crawling From Twitter", variable=self.var, value=2
              ).grid(row=3, column=0,sticky='w')
        R3 = tk.Radiobutton(f1_5, text="Step 2. Labeling Tweets", variable=self.var, value=3
              ).grid(row=4, column=0,sticky='w')
        R4 = tk.Radiobutton(f1_5, text="Step 3. Learning and Classifying", variable=self.var, value=4
              ).grid(row=5, column=0,sticky='w')
        R5 = tk.Radiobutton(f1_5, text="Step 4. Twitter User Information", variable=self.var, value=5
              ).grid(row=6, column=0,sticky='w')

        tk.Label(f1_5, font=("Courier", 1), text= ' ').grid(row=7,column=0,columnspan=9,sticky='w')

        #### get folder
        f1_7 = tk.Frame(self)
        f1_7.pack(padx=25, anchor='w')
        self.path_check = tk.Message(f1_7, text= "  ", justify='left', width = 380)
        self.path_check.grid(row=0, column=0,columnspan=9,sticky='w')

        #### blue label
        f2 = tk.Frame(self)
        f2.pack(padx=60, anchor='w')
        self.programOutput = tk.StringVar()
        tk.Label(f2, anchor="w",fg="white",bg="blue", textvariable=self.programOutput, 
                width=36).grid(row=1, column=0,sticky='w')
        self.programOutput.set(start_bt_ms)        


        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(10, 15), anchor='e')
        self.stb = tk.Button(fb, text='Start !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb1_5 = tk.Button(fb, text='Path', height=1, width=6, command=self.click_path)
        self.stb1_5.pack(side='right', padx=10)
        self.stb1_5.bind('<Enter>', self.hover_on1)
        self.stb1_5.bind('<Leave>', self.hover_off)

        self.stb2 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb2.pack(side='right')

        self.pathDisplayed = False


    def value1(self, event=None):
        subprocess.Popen(["python", "guiGrabing.py"])

    def hover_on(self, event=None):
        if self.var.get() == 0:
            self.programOutput.set("Select the function you want")
        elif self.var.get() == 1:
            self.programOutput.set("Generate Twitter configuration file by access keys")
        elif self.var.get() == 2:
            self.programOutput.set("Crawl real-time tweets by given key words")
        elif self.var.get() == 3:
            self.programOutput.set("Label crawled tweets into two distinct classes")
        elif self.var.get() == 4:
            self.programOutput.set("Classify by given machine learning algorithm")
        elif self.var.get() == 5:
            self.programOutput.set("Learn about followers/friends of an account")

    def hover_on1(self, event=None):
        if self.pathDisplayed:
            self.programOutput.set("Click to pack up currently displayed path")
        else:
            self.programOutput.set("Click to check current working directory")

    def hover_off(self, event=None):
        self.programOutput.set(start_bt_ms)

    def click_path(self, event=None):
        self.pathDisplayed = True
        self.path_check.config(text= "        Current working directory is:  ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄\n\n" + os.getcwd() +"\n")
        self.update()  # update! otherwise error occurs if text too long 
        self.stb1_5.config(text="PackUp", command = self.click_pack)

    def click_pack(self, event=None):
        self.pathDisplayed = False 
        self.path_check.config(text= " ")
        self.stb1_5.config(text="Path", command = self.click_path)


    def click_ok(self, event=None):
        self.programOutput.set("Function started.")
        global start_bt_ms
        start_bt_ms = "Function started."

        if self.var.get() == 1:
            configuration() 
        elif self.var.get() == 2:
            crawling()
        elif self.var.get() == 3:
            labeling()
        elif self.var.get() == 4:
            learning()
        elif self.var.get() == 5:
            info()


    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()

