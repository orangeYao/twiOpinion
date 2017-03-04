import Tkinter as tk
import subprocess
import AppKit
from versionControl import greeting
from versionControl import startingInfo 
import os
import guiConfiguration
import guiGrabing

start_bt_ms = os.getcwd() 

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
        f1_5.pack(padx=60, pady=10, anchor='w')

        self.var = tk.IntVar()

        tk.Label(f1_5, text= 'Select the function you want:'
                ).grid(row=0,column=0,columnspan=9,sticky='w')

        tk.Label(f1_5, text= ' ').grid(row=1,column=0,columnspan=9,sticky='w')

        R1 = tk.Radiobutton(f1_5, text="Step 0. Twitter Accessing Setting", variable=self.var, value=1
              ).grid(row=2, column=0,sticky='w')
        R2 = tk.Radiobutton(f1_5, text="Step 1. Crawling From Twitter", variable=self.var, value=2
              ).grid(row=3, column=0,sticky='w')
        R3 = tk.Radiobutton(f1_5, text="Step 2. Labeling Tweets", variable=self.var, value=3
              ).grid(row=4, column=0,sticky='w')
        R4 = tk.Radiobutton(f1_5, text="Step 3. Machine Learning", variable=self.var, value=4
              ).grid(row=5, column=0,sticky='w')

        tk.Label(f1_5, text= ' ').grid(row=6,column=0,columnspan=9,sticky='w')
        self.programOutput = tk.StringVar()
        tk.Label(f1_5, anchor="w",fg="white",bg="blue", textvariable=self.programOutput, 
                width=95).grid(row=7, column=0,sticky='w')
        self.programOutput.set(start_bt_ms)        


        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(10, 15), anchor='e')
        self.stb = tk.Button(fb, text='Start !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb2.pack(side='right', padx=10)


    def hover_on(self, event=None):
        if self.var.get() == 0:
            self.programOutput.set("Select the function you want.")
        elif self.var.get() == 1:
            self.programOutput.set("Step 0")
        elif self.var.get() == 2:
            self.programOutput.set("Step 1")
        elif self.var.get() == 3:
            self.programOutput.set("Step 2")
        elif self.var.get() == 4:
            self.programOutput.set("Step 3")

    def hover_off(self, event=None):
        self.programOutput.set(start_bt_ms)

    def click_ok(self, event=None):
        self.programOutput.set("Function started.")
        global start_bt_ms
        start_bt_ms = "Function started."

        if self.var.get() == 1:
            subprocess.Popen(["python","guiConfiguration.py"])
        elif self.var.get() == 2:
            subprocess.Popen(["python","guiGrabing.py"])
        elif self.var.get() == 4:
            subprocess.Popen(["python","guiLearning.py"],bufsize=0)


    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()

if __name__ == '__main__':
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

