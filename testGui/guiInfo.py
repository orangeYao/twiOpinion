import Tkinter as tk
from versionControl import greeting
import AppKit
from infoTwitterGet import getFollower
from infoFindEdge import followerInfo
import threading

start_bt_ms = "Get information about followers/friends of an account~"
next_bt_ms = "Output file will be displayed here"

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
        tk.Message(self, text= "Step 4. Get Followers/Friends Info",
                   font='System 14 bold', justify='left', aspect=1800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=(15,0), anchor='w')

        tk.Label(f1, text='Username whose followers/friends you hope to learn:').grid(row=0,column=0,columnspan=6,sticky='w')
        tk.Label(f1, text='Username:').grid(row=1, column=0, sticky='w')
        self.l1 = tk.Entry(f1, background='white', width=30)
        self.l1.grid(row=1, column=1, columnspan=5,sticky='w')
        self.l1.insert(0,"realDonaldTrump")


        tk.Label(f1, text='Output path:').grid(row=2, column=0, sticky='w')
        self.l2 = tk.Entry(f1, background='white', width=30)
        self.l2.grid(row=2, column=1, sticky='w')
        self.l2.insert(0, "./info")

        ## frame 1 buttons 
        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(5,0), anchor='e')
        self.stb = tk.Button(fb, text='Followers', height=1, width=6, command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)
        self.stb2 = tk.Button(fb, text='Friends', height=1, width=6, command=self.click_ok2)
        self.stb2.pack(side='right', padx=10)
        self.stb2.bind("<Enter>", self.hover_on2)
        self.stb2.bind("<Leave>", self.hover_off)

        self.stb2_5 = tk.Button(fb, text='Check', height=1, width=6, state='disabled', command=self.click_check)
        self.stb2_5.pack(side='right')
        self.stb2_5.bind("<Enter>", self.hover_on6)
        self.stb2_5.bind("<Leave>", self.hover_off)

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, anchor='w')

        tk.Label(f2, text='   ').grid(row=3, column=0, sticky='w')
        tk.Label(f2, text='The Tweeter ids you wish to learn more about:' 
                        ).grid(row=4,column=0,columnspan=10,sticky='w')

        tk.Label(f2, text='File path:     ').grid(row=5, column=0, sticky='w')
        self.l3 = tk.Entry(f2, background='white',width=30)
        self.l3.grid(row=5, column=1,columnspan=1, sticky='w')
        self.l3.insert(0, "./info/realDonaldTrump.txt")

        ## frame 2 buttons
        fb2 = tk.Frame(self)
        fb2.pack(padx=60, pady=(5,30), anchor='e')
        self.stb3 = tk.Button(fb2, text='.json', height=1, width=6, command=self.click_ok3)
        self.stb3.pack(side='right')
        self.stb3.bind("<Enter>", self.hover_on3)
        self.stb3.bind("<Leave>", self.hover_off)

        self.stb4 = tk.Button(fb2, text='.csv', height=1, width=6, command=self.click_ok4)
        self.stb4.pack(side='right', padx=10)
        self.stb4.bind("<Enter>", self.hover_on4)
        self.stb4.bind("<Leave>", self.hover_off)
            
        self.stb5_5 = tk.Button(fb2, text='Check', height=1, width=6, state='disabled', command=self.click_check2)
        self.stb5_5.pack(side='right')
        self.stb5_5.bind("<Enter>", self.hover_on6)
        self.stb5_5.bind("<Leave>", self.hover_off)

        self.stb5 = tk.Button(fb2, text='Save & Quit', height=1, width=8, command=self.click_cancel)
        self.stb5.pack(side='right', padx=10)


        ## frame last
        fb3 = tk.Frame(self)
        fb3.pack(padx=60, pady=(0, 30), anchor='e')
        self.label = tk.Label(fb3, anchor="w",fg="white",bg="blue",text=start_bt_ms, width=45)
        self.label.pack()

    def hover_on(self, event=None):
        self.label.config(text="Click to get his/her followers, at rate of 5000 ids/minute")

    def hover_on2(self, event=None):
        self.label.config(text="Click to get his/her friends, at rate of 5000 ids/minute")

    def hover_on3(self, event=None):
        self.label.config(text="Click to learn about these ids in \'.json\' format, 100 ids/s")

    def hover_on4(self, event=None):
        self.label.config(text="Click to learn about these ids in \'.csv\' format, 100 ids/s")

    def hover_on6(self, event=None):
        self.label.config(text="Click to check getting process")

    def hover_off(self, event=None):
        self.label.config(text=start_bt_ms)

######
    def click_ok(self, event=None):
        self.followFriend = "followers"
        self.midthread()

    def click_ok2(self, event=None):
        self.followFriend = "friends" 
        self.midthread()

    def midthread(self, event=None):
        global start_bt_ms
        start_bt_ms = "Started, output in \'"+self.l2.get()+"/"+self.l1.get()+".txt\'" 
        self.label.config(text=start_bt_ms)

        newthread = threading.Thread(target=self.threadGet)
        newthread.daemon = True
        newthread.start()

    def threadGet(self, event=None):
        self.stb2_5.config(default='active', state='active')
        self.disable()
        print "thread!"
        getFollower(self.l1.get(), self.l2.get(), self.followFriend)

    def click_check(self, event=None):
        tmpLines = sum(1 for line in open(self.l2.get() + "/" + self.l1.get() + ".txt"))
        self.label.config(text=str(tmpLines)+" "+ self.followFriend +" already found")
        print "click check"


######
    def click_ok3(self, event=None):
        self.outFormat = ".json"
        self.midthread2()

    def click_ok4(self, event=None):
        self.outFormat = ".csv"
        self.midthread2()

    def midthread2(self, event=None):
        global start_bt_ms
        start_bt_ms = "Started, output in \'" + self.l3.get()[0:-4] + self.outFormat + "\'" 
        self.label.config(text=start_bt_ms)

        self.lines_to_get = sum(1 for line in open(self.l3.get())) 
        newthread = threading.Thread(target=self.threadGet2)
        newthread.daemon = True
        newthread.start()

    def threadGet2(self, event=None):
        self.stb5_5.config(default='active', state='active')
        self.disable()
        print "thread2!"
        followerInfo(self.l3.get(), self.outFormat)

    def click_check2(self, event=None):
        tmpLines = sum(1 for line in open(self.l3.get()[0:-4] + self.outFormat))
        self.label.config(text=str(self.lines_to_get)+" lines to learn, "+str(tmpLines)+" lines already learned")
        print "click check 2"

######
    def disable(self, event=None):
        self.l1.config(state='disabled')
        self.l2.config(state='disabled')
        self.l3.config(state='disabled')
        self.stb.config(state='disabled')
        self.stb2.config(state='disabled')
        self.stb3.config(state='disabled')
        self.stb4.config(state='disabled')


    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()


def info():
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

