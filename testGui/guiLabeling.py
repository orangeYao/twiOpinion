import Tkinter as tk
from versionControl import greeting
import AppKit
import subprocess
import threading
import time
import os
import functions

start_bt_ms = "Welcome! Think about the how you want to label tweets."
count = -1 # not updated after recalled 
Mflag = False
Kflag = False 

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Return>', self.click_ok1)
        self.master.bind('<Escape>', self.click_cancel)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        tk.Message(self, text= greeting(),
                   font='System 18 bold', justify='left', aspect=800).pack(pady=(5, 0))
        tk.Message(self, text= "Step 2. Labeling",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        global Mflag, Kflag
        Mflag = False
        Kflag = False 

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
        self.pass_input.insert(0,"./output/stream_(step1Tag)_Fetched.json")
        #self.pass_input.insert(0,"./output/stream_China_Fetched.json")
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
        self.stb = tk.Button(fb, text='Keyword1', height=1, width=6, default='active', command=self.click_ok1)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on1)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb1 = tk.Button(fb, text='Keyword2', height=1, width=6, default='active', command=self.click_ok2)
        self.stb1.pack(side='right')
        self.stb1.bind("<Enter>", self.hover_on2)
        self.stb1.bind("<Leave>", self.hover_off)

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

    def hover_on1(self, event=None):
        self.label.config(text="Click to label by keywords into class 1")

    def hover_on2(self, event=None):
        self.label.config(text="Click to label by keywords into class 2")

    def hover_off(self, event=None):
        self.label.config(text=start_bt_ms)

    def click_ok1(self, event=None):
        global Kflag
        Kflag = 1 
        self.click_ok()

    def click_ok2(self, event=None):
        global Kflag 
        Kflag = 2 
        self.click_ok()

    def click_ok(self, event=None):
        if not os.path.isfile(self.pass_input.get()):
            self.label.config(text="File "+self.pass_input.get()+" doesn't exist!")
            return 0 

        self.classes=[]
        if Kflag == 1:
            condition_s = self.user_input.get()
        elif Kflag == 2:
            condition_s = self.user_input2.get()

        condition_l = condition_s.replace("("," ").replace(")"," ").split()
        for bool_seperator in ["and", "or", "not"]:
            condition_l[:] = (value for value in condition_l if value != bool_seperator)
        if condition_s.strip() == "":
            condition_l = ['']

        tmp_count = 0
        #self.tweets = functions.readManyStrings(self.pass_input.get())
        self.tweets = functions.readManyJsons(self.pass_input.get())
        for tweet_d in self.tweets:
            tweet = tweet_d["text"] 
            condition_s_tmp = condition_s
            for condition in condition_l:
                if functions.findWholeWord(condition)(tweet) is not None:
                    condition_s_tmp = condition_s_tmp.replace(condition, "True")
                else:
                    condition_s_tmp = condition_s_tmp.replace(condition, "False")
            try:
                if eval(condition_s_tmp):
                    tmp_count += 1 
                    self.classes.append(tweet_d)
            except SyntaxError:
                self.label.config(text="SyntaxError in keywords!")
                return 0
        self.label.config(text=str(tmp_count) + " tweets are selected as class " + str(Kflag))

        tmpPath = os.path.dirname(self.pass_input.get())
        if Kflag == 1:
            functions.simpleWriteJson(self.classes, tmpPath + "/positive.json")
            functions.simpleWriteJsonText(self.classes, tmpPath + "/positive.txt")
        elif Kflag == 2:
            functions.simpleWriteJson(self.classes, tmpPath + "/negative.json")
            functions.simpleWriteJsonText(self.classes, tmpPath + "/negative.txt")


    def click_ok_manual(self, event=None):
        if not os.path.isfile(self.pass_input.get()):
            self.label.config(text="File "+self.pass_input.get()+" doesn't exist!")
            return 0 

        print "File: " + self.pass_input.get()

        self.label.config(text="Label tweets manually")
        global start_bt_ms
        start_bt_ms = "Label tweets manually"
        self.stb.config(state='disabled')
        self.stb1.config(state='disabled')
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

        #self.tweets = functions.readManyStrings(self.pass_input.get())
        self.tweets = functions.readManyJsons(self.pass_input.get())
        self.next_twi()
        self.class1=[]
        self.class2=[]
        global Mflag
        Mflag = True

    def click_cancel(self, event=None):
        if Mflag:
            tmpPath = os.path.dirname(self.pass_input.get())
            #functions.simpleWriteList(self.class1,tmpPath + "/positive.txt")
            #functions.simpleWriteList(self.class2,tmpPath + "/negative.txt")
            functions.simpleWriteJson(self.class1, tmpPath + "/positive.json")
            functions.simpleWriteJson(self.class2, tmpPath + "/negative.json")
            functions.simpleWriteJsonText(self.class1, tmpPath + "/positive.txt")
            functions.simpleWriteJsonText(self.class2, tmpPath + "/negative.txt")
        print("The user clicked 'Cancel'")
        self.master.destroy()

    def click_1(self, event=None):
        if self.next_twi() == 1:
            self.class1.append(self.tweet_element)
            self.disp_twi()

    def click_2(self, event=None):
        if self.next_twi() == 1:
            self.class2.append(self.tweet_element)
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
        self.display = self.tweets[count]["text"]
        self.tweet_element = self.tweets[count]
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

