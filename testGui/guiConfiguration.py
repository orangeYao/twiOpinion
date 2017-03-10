# -*- coding: utf-8 -*-
import Tkinter as tk
from versionControl import greeting
import AppKit

website = "(https://apps.twitter.com)"
start_bt_ms = "Welcome! Paste your keys above. " + website 

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
        tk.Message(self, text= "Step 0. Twitter Accessing Setting",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=15, anchor='w')

        tk.Label(f1, text='Your consumer key and secret: (｡・`ω´･)' 
                        ).grid(row=0,column=0,columnspan=2,sticky='w')
        tk.Label(f1, text='Consumer key:').grid(row=1, column=0, sticky='w')
        self.l1 = tk.Entry(f1, background='white', width=30)
        self.l1.grid(row=1, column=1, sticky='w')

        tk.Label(f1, text='Consumer secret:').grid(row=2, column=0, sticky='w')
        self.l2 = tk.Entry(f1, background='white', width=30)
        self.l2.grid(row=2, column=1, sticky='w')

        tk.Label(f1, text='   ').grid(row=3, column=0, sticky='w')
        tk.Label(f1, text='Your access token and secret:' 
                        ).grid(row=4,column=0,columnspan=2,sticky='w')

        tk.Label(f1, text='Access token:').grid(row=5, column=0, sticky='w')
        self.l3 = tk.Entry(f1, background='white', width=30)
        self.l3.grid(row=5, column=1, sticky='w')

        tk.Label(f1, text='Access secret:').grid(row=6, column=0, sticky='w')
        self.l4 = tk.Entry(f1, background='white', width=30)
        self.l4.grid(row=6, column=1, sticky='w')

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, pady=30, anchor='w')

        self.label = tk.Label(f2, anchor="w",fg="white",bg="blue",text=start_bt_ms, width=45)
        self.label.pack()

        ## frame last 
        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Start !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb2.pack(side='right', padx=10)


    def hover_on(self, event=None):
        self.label.config(text="Click to generate configuration file")

    def hover_off(self, event=None):
        self.label.config(text=start_bt_ms)

    def click_ok(self, event=None):
        self.label.config(text="Configuration file has been generated! You can quit now.")
        global start_bt_ms
        start_bt_ms = "Configuration file has been generated! You can quit now."
        keys = ["consumer_key = "+self.l1.get(), "consumer_secret = "+self.l2.get(),
                "access_token = "+self.l3.get(), "access_secret = "+self.l4.get()]

        f = open("config.py", "w")
        for line in keys:
            print line
            f.write(line + '\n')

    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()


def configuration():
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

