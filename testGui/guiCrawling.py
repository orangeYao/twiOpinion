import Tkinter as tk
from versionControl import greeting
import AppKit
import subprocess
import threading
import time
import twitter_stream_download
import readJson
import os

start_bt_ms = "Welcome! Think about the keyword you want to know."

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
        tk.Message(self, text= "Step 1. Crawling",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=15, anchor='w')

        self.f1l1 = tk.Label(f1, text='The tag or keyword you wish to grab from Twitter:')
        self.f1l1.grid(row=0,column=0,columnspan=2,sticky='w')
        self.f1l1L = tk.Label(f1, text='Keyword:')
        self.f1l1L.grid(row=1, column=0, sticky='w')
        self.user_input = tk.Entry(f1, background='white', width=30)
        self.user_input.grid(row=1, column=1, sticky='w')


        tk.Label(f1, text='   ').grid(row=2, column=0, sticky='w')
        self.f1l2 = tk.Label(f1, text='The folder you wish to store data (default as ./output):')
        self.f1l2.grid(row=3,column=0,columnspan=2,sticky='w')


        self.f1l2L = tk.Label(f1, text='Path:')
        self.f1l2L.grid(row=4, column=0, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=30)
        self.pass_input.insert(0,"./output")
        self.pass_input.grid(row=4, column=1, sticky='w')
    

        ##frame middle 1.5
        f1_5 = tk.Frame(self)
        f1_5.pack(padx=60, pady=(5,10), anchor='w')
        self.ctl_tx = tk.Label(f1_5, anchor="w",fg='black',state='disabled',
                    text="Control crawling by following buttons after started:",width=45)
        self.ctl_tx.pack()

        self.ctl_1 = tk.Button(f1_5, text='Stop', height=1, width=6, state='disabled', command=self.click_1)
        self.ctl_1.bind('<Enter>', self.hover_1)
        self.ctl_1.bind('<Leave>', self.hover_off)
        self.ctl_1.pack(side='right')
        self.ctl_2 = tk.Button(f1_5, text='Fetch', height=1, width=6, state='disabled', command=self.click_2)
        self.ctl_2.bind('<Enter>', self.hover_2)
        self.ctl_2.bind('<Leave>', self.hover_off)
        self.ctl_2.pack(side='right')
        self.ctl_3 = tk.Button(f1_5, text='Check', height=1, width=6, state='disabled', command=self.click_3)
        self.ctl_3.bind('<Enter>', self.hover_3)
        self.ctl_3.bind('<Leave>', self.hover_off)
        self.ctl_3.pack(side='right')

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, pady=(10,10), anchor='w')
        self.label = tk.Label(f2, anchor="w",fg="white",bg="blue", text=start_bt_ms, width=45)
        self.label.pack()

        tk.Label(f2, anchor="w",text=" ", width=45).pack()


        ## frame last 
        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Start !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb2.pack(side='right', padx=10)


    def hover_1(self, event=None):
        self.label.config(text="Fetch contents, stop current crawling process and quit")

    def hover_2(self, event=None):
        self.label.config(text="Fetch meaningful contents of tweets for training in next step")

    def hover_3(self, event=None):
        self.label.config(text="Check number of tweets have been crawled")

    def hover_on(self, event=None):
        self.label.config(text="Click to start crawling")

    def hover_off(self, event=None):
        self.label.config(text=start_bt_ms)

    def click_ok(self, event=None):
        print "keyword: " + self.user_input.get()
        print "folder: " + self.pass_input.get()
        if self.user_input.get().strip() == "":
            self.label.config(text="Error: Indicate keywords before start crawling") 
            return 0

        try:
            execfile("config.py", {})
        except IOError:
            self.label.config(text="Error: Configuration file doesn't exist")
            return 0
        except SyntaxError:
            self.label.config(text="Error: Format error in configuration file")
            return 0


        self.file_name = self.pass_input.get() + "/stream_" + self.user_input.get() + ".json"
        print self.file_name

        self.label.config(text="Crawling has started!")
        global start_bt_ms
        start_bt_ms = "Crawling has started!"
        self.stb.config(state='disabled')
        self.stb2.config(state='disabled')

        self.ctl_1.config(state='active')
        self.ctl_2.config(state='active')
        self.ctl_3.config(state='active')
        self.ctl_tx.config(state='normal')

        self.user_input.config(state='disabled')
        self.pass_input.config(state='disabled')
        self.f1l1.config(state='disabled')
        self.f1l1L.config(state='disabled')
        self.f1l2.config(state='disabled')
        self.f1l2L.config(state='disabled')

        if not os.path.exists(self.pass_input.get()):
            os.makedirs(self.pass_input.get())

        newthread = threading.Thread(target=self.threadCrawl)
        newthread.daemon = True
        newthread.start()

    def threadCrawl(self, event=None):
        print "thread!" 
        twitter_stream_download.main(self.user_input.get(), self.pass_input.get())

    def click_cancel(self, event=None):
        print "The user clicked 'Cancel'"
        self.master.destroy()

    def click_1(self, event=None):
        print "Stop" 
        readJson.main(self.file_name)
        self.master.destroy()

    def click_2(self, event=None):
        lines = readJson.main(self.file_name)
        tmp = "Fetch: " + str(lines) + " lines of contents are fetched" 
        self.label.config(text=tmp)
        print "Fetch"

    def click_3(self, event=None):
        if os.path.isfile(self.file_name):
            lines = sum(1 for line in open(self.file_name))
        else:
            lines = 0
        tmp = "Check: " + str(lines) + " tweets have been crawled"
        self.label.config(text=tmp)
        global start_bt_ms
        start_bt_ms = tmp 
        print "Check" 

def crawling():
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True

    fixbug = "/Users/wuwenzhen/python/tweets/developSoftware/dustbin/py2app/venv/lib/python2.7/site-packages/pip/_vendor/requests/cacert.pem"
#    fixbug = certifi.where()
    if os.path.isfile(fixbug):
        os.environ['REQUESTS_CA_BUNDLE'] = fixbug 
    # otherwise SSLError: [Errno 20]

    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

