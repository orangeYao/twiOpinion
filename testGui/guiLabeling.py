import Tkinter as tk
from versionControl import greeting
import AppKit
import subprocess
import threading
import time
import os
import functions

start_bt_ms = "Welcome! Think about the how you want to label tweets."
count = -1 
Mflag = False

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
        tk.Message(self, text= "Step 2. Labeling",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=15, anchor='w')

        self.f1l1 = tk.Label(f1, text='The keywords to label tweets as class 1 (positive.txt):')
        self.f1l1.grid(row=0,column=0,columnspan=2,sticky='w')
        self.f1l1L = tk.Label(f1, text='Keyword:')
        self.f1l1L.grid(row=1, column=0, sticky='w')
        self.user_input = tk.Entry(f1, background='white', width=30)
        self.user_input.grid(row=1, column=1, sticky='w')


        tk.Label(f1, text='   ').grid(row=2, column=0, sticky='w')
        self.f1l2 = tk.Label(f1, text='The keywords to label tweets as class 2 (negative.txt):')
        self.f1l2.grid(row=3,column=0,columnspan=2,sticky='w')
        self.f1l2L = tk.Label(f1, text='Keyword:')
        self.f1l2L.grid(row=4, column=0, sticky='w')
        self.user_input2 = tk.Entry(f1, background='white', width=30)
        self.user_input2.grid(row=4, column=1, sticky='w')

        tk.Label(f1, text='   ').grid(row=5, column=0, sticky='w')
        self.f1l3 = tk.Label(f1, text='The file containing fetched tweets (default in ./output):')
        self.f1l3.grid(row=6,column=0,columnspan=2,sticky='w')
        self.f1l3L = tk.Label(f1, text='Path:')
        self.f1l3L.grid(row=7, column=0, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=30)
        #self.pass_input.insert(0,"./output/stream_(step1Tag).txt")
        self.pass_input.insert(0,"./output/stream_China.txt")
        self.pass_input.grid(row=7, column=1, sticky='w')

        ##frame middle 1.5
        f1_5 = tk.Frame(self)
        f1_5.pack(padx=60, pady=(5,0), anchor='w')
        self.ctl_tx = tk.Label(f1_5, anchor="w",fg='black',state='disabled',
                    text="Manually label each tweet displayed by following buttons",width=45)
        self.ctl_tx.pack()

        self.ctl_1 = tk.Button(f1_5, text='Class1', height=1, width=6, state='disabled', command=self.click_1)
        self.ctl_1.bind('<Enter>', self.hover_1)
        self.ctl_1.bind('<Leave>', self.hover_off)
        self.ctl_1.pack(side='right')
        self.ctl_2 = tk.Button(f1_5, text='Class2', height=1, width=6, state='disabled', command=self.click_2)
        self.ctl_2.bind('<Enter>', self.hover_2)
        self.ctl_2.bind('<Leave>', self.hover_off)
        self.ctl_2.pack(side='right')
        self.ctl_3 = tk.Button(f1_5, text='Skip', height=1, width=6, state='disabled', command=self.click_3)
        self.ctl_3.bind('<Enter>', self.hover_3)
        self.ctl_3.bind('<Leave>', self.hover_off)
        self.ctl_3.pack(side='right')

        ##frame middle 1.7
        f1_7 = tk.Frame(self)
        f1_7.pack(padx=30, anchor='w')
        self.dis = tk.Message(f1_7, text="", justify='left', width=450)
        self.dis.pack()

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, anchor='w')
        self.label = tk.Label(f2, anchor="w",fg="white",bg="blue", text=start_bt_ms, width=45)
        self.label.pack()
        tk.Label(f2, anchor="w",text=" ", width=45).pack()

        ## frame last 
        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Keywords', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='Manual', height=1, width=6, command=self.click_ok_manual)
        self.stb2.pack(side='right')
        self.stb2.bind("<Enter>", self.hover_on_manual)
        self.stb2.bind("<Leave>", self.hover_off)

        self.stb3 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb3.pack(side='right')


    def hover_1(self, event=None):
        self.label.config(text="Label this tweet as group 1")

    def hover_2(self, event=None):
        self.label.config(text="Label this tweet as group 2")

    def hover_3(self, event=None):
        self.label.config(text="Skip this tweet")

    def hover_on_manual(self, event=None):
        self.label.config(text="Click to label manually, leaving keywords entries blank")

    def hover_on(self, event=None):
        self.label.config(text="Click to label by keywords")

    def hover_off(self, event=None):
        self.label.config(text=start_bt_ms)

    def click_ok(self, event=None):
        if not os.path.isfile(self.pass_input.get()):
            self.label.config(text="File "+self.pass_input.get()+" doesn't exist!")
            return 0 

        print "keyword1: " + self.user_input.get()
        print "keyword2: " + self.user_input2.get()
        print "file: " + self.pass_input.get()

    def click_ok_manual(self, event=None):
        if not os.path.isfile(self.pass_input.get()):
            self.label.config(text="File "+self.pass_input.get()+" doesn't exist!")
            return 0 

        print "file: " + self.pass_input.get()

        self.label.config(text="Label tweets manually")
        global start_bt_ms
        start_bt_ms = "Label tweets manually"
        self.stb.config(state='disabled')
        self.stb2.config(state='disabled')

        self.ctl_1.config(state='active')
        self.ctl_2.config(state='active')
        self.ctl_3.config(state='active')
        self.ctl_tx.config(state='normal')

        self.user_input.config(state='disabled')
        self.user_input2.config(state='disabled')
        self.pass_input.config(state='disabled')
        self.f1l1.config(state='disabled')
        self.f1l1L.config(state='disabled')
        self.f1l2.config(state='disabled')
        self.f1l2L.config(state='disabled')
        self.f1l3.config(state='disabled')
        self.f1l3L.config(state='disabled')

        self.stb3.config(text="Save&Quit",default='active',width=7)

        self.tweets = functions.readManyStrings(self.pass_input.get())
        self.next_twi()
        self.class1=[]
        self.class2=[]
        global Mflag
        Mflag = True

    def click_cancel(self, event=None):
        if Mflag:
            tmpPath = os.path.dirname(self.pass_input.get())
            functions.writeList(self.class1,tmpPath + "/positive.txt")
            functions.writeList(self.class2,tmpPath + "/negative.txt")
        print("The user clicked 'Cancel'")
        self.master.destroy()

    def click_1(self, event=None):
        if self.next_twi() == 1:
            self.class1.append(self.display)
            self.disp_twi()

    def click_2(self, event=None):
        if self.next_twi() == 1:
            self.class2.append(self.display)
            self.disp_twi()

    def click_3(self, event=None):
        if self.next_twi() == 1:
            self.disp_twi()

    def next_twi(self, event=None):
        global count
        count += 1
        if count >= len(self.tweets):
            self.label.config(text="Maximum number of tweets reached!")
            return 0
        self.display = self.tweets[count].strip() #\n at end of self.display
        self.dis.config(text="\nTweet No."+str(count)+": "+self.display+"\n")  
        return 1

    def disp_twi(self, event=None):
        self.label.config(text=str(len(self.class1))+" tweets in class1 / "+str(len(self.class2))+" tweets in class2.")
        global start_bt_ms
        start_bt_ms = str(len(self.class1))+" tweets in class1 / "+str(len(self.class2))+" tweets in class2." 


def labeling():
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True

    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

