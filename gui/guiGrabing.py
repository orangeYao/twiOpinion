import Tkinter as tk
import AppKit


start_bt_ms = "Welcome! Think about the keyword you want to know."

def testOuput():
    print "test it"

def greeting():
    return "Welcome to twiOpinion 0.1.3!" 


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        #self.master.bind('<Return>', self.click_ok)
        #self.master.bind('<Escape>', self.click_cancel)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        testOuput()    

        tk.Message(self, text= greeting(),
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))
        tk.Message(self, text= "Step 1. Crawling",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=15, anchor='w')

        tk.Label(f1, text='The tag or keyword you wish to grab from Twitter:'
                        ).grid(row=0,column=0,columnspan=2,sticky='w')
        tk.Label(f1, text='Keyword:').grid(row=1, column=0, sticky='w')
        self.user_input = tk.Entry(f1, background='white', width=30)
        self.user_input.grid(row=1, column=1, sticky='w')


        tk.Label(f1, text='   ').grid(row=2, column=0, sticky='w')
        tk.Label(f1, text='The folder you wish to store data (blank default as ./output):'
                        ).grid(row=3,column=0,columnspan=2,sticky='w')

        tk.Label(f1, text='Path:').grid(row=4, column=0, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=30)
        self.pass_input.grid(row=4, column=1, sticky='w')

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, pady=30, anchor='w')

        self.programOutput = tk.StringVar()
        label = tk.Label(f2, anchor="w",fg="white",bg="blue", textvariable=self.programOutput, width=45).pack()
        self.programOutput.set(start_bt_ms)

        ## frame last 
        self.changeButton = tk.BooleanVar()
        self.changeButton.set(True)

        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Start !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb2.pack(side='right', padx=10)


    def hover_on(self, event=None):
        self.programOutput.set("click to start grabing")

    def hover_off(self, event=None):
        self.programOutput.set(start_bt_ms) 


    def click_ok(self, event=None):
        self.programOutput.set("Grabing has started!")

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
    print "what here?"

