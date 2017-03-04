import Tkinter as tk
import AppKit
from versionControl import greeting

start_bt_ms = "Welcome! Now you can start machine learning!" 
next_bt_ms = "Result will be displayed here"

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
        tk.Message(self, text= "Step 3. Learning",
                   font='System 14 bold', justify='left', aspect=800).pack(pady=(5, 0))

        ## frame 1
        f1 = tk.Frame(self)
        f1.pack(padx=60, pady=15, anchor='w')

        tk.Label(f1, text= 'The folder you wish to store data (blank default as ./output):' 
                        ).grid(row=0,column=0,columnspan=9,sticky='w')
        tk.Label(f1, text='Path:').grid(row=1, column=0, sticky='w')
        self.user_input = tk.Entry(f1, background='white', width=30)
        self.user_input.grid(row=1, column=1,columnspan=4, sticky='w')

        tk.Label(f1, text='   ').grid(row=2, column=0, sticky='w')
        tk.Label(f1, text='Number of training and testing cases to select:'
                        ).grid(row=3,column=0,columnspan=5,sticky='w')

        tk.Label(f1, text='Train:').grid(row=4, column=0, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=10)
        self.pass_input.grid(row=4, column=1, sticky='w')
        tk.Label(f1, text='Test:').grid(row=4, column=2, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=10)
        self.pass_input.grid(row=4, column=3, sticky='w')


        #buttons at bottom
        f1_5 = tk.Frame(self)
        f1_5.pack(padx=60, pady=10, anchor='w')
        var = tk.IntVar()
        tk.Label(f1_5, text= 'Select a machine learning algorithm:'
                ).grid(row=0,column=0,columnspan=9,sticky='w')
        R1 = tk.Radiobutton(f1_5, text="Support Vector Machine", variable=var, value=1
              ).grid(row=1, column=0)
        R2 = tk.Radiobutton(f1_5, text="Naive Bayes", variable=var, value=2
              ).grid(row=1, column=1)
        R3 = tk.Radiobutton(f1_5, text="Decision Tree", variable=var, value=3
              ).grid(row=1, column=2)

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, pady=30, anchor='w')

        self.programOutput = tk.StringVar()
        self.resultOutput = tk.StringVar()
        label = tk.Label(f2, anchor="w",fg="white",bg="blue", textvariable=self.programOutput, width=45).pack()
        label = tk.Label(f2, anchor="w",fg="black",bg="cyan", textvariable=self.resultOutput, width=45).pack()
        self.programOutput.set(start_bt_ms)
        self.resultOutput.set(next_bt_ms)


        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Learn !', height=1, width=6, default='active', command=self.click_ok)
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


if __name__ == "__main__": 
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True

    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

