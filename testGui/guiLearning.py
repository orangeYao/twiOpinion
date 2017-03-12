import Tkinter as tk
from versionControl import greeting
import AppKit
from learningFunction import learnfunction
import os

start_bt_ms = "Welcome! Now you can start machine learning!" 
next_bt_ms = "Result will be displayed here"
learn_flag = False

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
        f1.pack(padx=60, pady=10, anchor='w')

        tk.Label(f1, text= 'The folder you stored labeled data (default as ./output/):' 
                        ).grid(row=0,column=0,columnspan=9,sticky='w')
        tk.Label(f1, text='Path:').grid(row=1, column=0, sticky='w')
        self.user_input = tk.Entry(f1, background='white', width=30)
        self.user_input.insert(0,"./output/")
        self.user_input.grid(row=1, column=1,columnspan=4, sticky='w')

        
        tk.Label(f1, text='   ').grid(row=2, column=0, sticky='w')
        tk.Label(f1, text= 'The file containing unlabeled tweets you hope to learn:' 
                        ).grid(row=3,column=0,columnspan=9,sticky='w')
        tk.Label(f1, text='File:').grid(row=4, column=0, sticky='w')
        self.pass_input = tk.Entry(f1, background='white', width=30)
        self.pass_input.insert(0,"./output/unknown.txt")
        self.pass_input.grid(row=4, column=1,columnspan=4, sticky='w')


        tk.Label(f1, text='   ').grid(row=5, column=0, sticky='w')
        tk.Label(f1, text='Number of labeled and unlabeled tweets (blank default as maximum):'
                        ).grid(row=6,column=0,columnspan=5,sticky='w')

        tk.Label(f1, text='Labeled:').grid(row=7, column=0, sticky='w')
        self.pass_inputL = tk.Entry(f1, background='white', width=10)
        self.pass_inputL.grid(row=7, column=1, sticky='w')
        tk.Label(f1, text='Unlabeled:').grid(row=7, column=2, sticky='w')
        self.pass_inputR = tk.Entry(f1, background='white', width=10)
        self.pass_inputR.grid(row=7, column=3, sticky='w')

        #buttons at bottom

        self.radio_var = tk.IntVar()
        print self.radio_var.get()

        f1_5 = tk.Frame(self)
        f1_5.pack(padx=60, pady=(5,10), anchor='w')
        tk.Label(f1_5, text= 'Select a machine learning algorithm:'
                ).grid(row=0,column=0,columnspan=9,sticky='w')
        tk.Radiobutton(f1_5, text="SVM", value=1, command = self.r1,
              indicatoron=0).grid(row=1, column=0)
        tk.Radiobutton(f1_5, text="MultinomialNB",value=2, command = self.r2,
              indicatoron=0).grid(row=1, column=1)
        tk.Radiobutton(f1_5, text="BernoulliNB",value=3, command = self.r3,
              indicatoron=0).grid(row=1, column=2)
        tk.Radiobutton(f1_5, text="Decision Tree",value=4, command = self.r4,
              indicatoron=0).grid(row=1, column=3)

        ##frame 2
        f2 = tk.Frame(self)
        f2.pack(padx=60, pady=(10,10), anchor='w')

        self.label1 = tk.Label(f2, anchor="w",fg="white",bg="blue", text=start_bt_ms, width=45)
        self.label1.pack()
        self.label2 = tk.Label(f2, anchor="w",fg="black",bg="cyan", text=next_bt_ms, width=45)
        self.label2.pack()

        fb = tk.Frame(self)
        fb.pack(padx=60, pady=(0, 15), anchor='e')
        self.stb = tk.Button(fb, text='Learn !', height=1, width=6, default='active', command=self.click_ok)
        self.stb.pack(side='right')
        self.stb.bind("<Enter>", self.hover_on)
        self.stb.bind("<Leave>", self.hover_off)

        self.stb2 = tk.Button(fb, text='FileInfo', height=1, width=6, command=self.click_info)
        self.stb2.pack(side='right', padx=5)
        self.stb3 = tk.Button(fb, text='Quit...', height=1, width=6, command=self.click_cancel)
        self.stb3.pack(side='right')


    def r1(self, event=None):
        self.radio_var.set(1)

    def r2(self, event=None):
        self.radio_var.set(2)

    def r3(self, event=None):
        self.radio_var.set(3)

    def r4(self, event=None):
        self.radio_var.set(4)

    def hover_on(self, event=None):
        if self.radio_var.get() == 1:
            self.label1.config(text="Support Vector Machine, may take a while (^0^)/")
        elif self.radio_var.get() == 2:
            self.label1.config(text="Naive Bayes classifier multinomial model, may take a while (^0^)/")
        elif self.radio_var.get() == 3:
            self.label1.config(text="Naive Bayes classifier Bernoulli model, may take a while (^0^)/")
        elif self.radio_var.get() == 4:
            self.label1.config(text="Decision tree, may take a while (^0^)/")
        elif self.radio_var.get() == 0:
            self.label1.config(text="Select a machine learning algorithm before starting")


    def hover_off(self, event=None):
        self.label1.config(text=start_bt_ms) 

    def click_ok(self, event=None):
        global learn_flag
        global start_bt_ms
        learn_flag = False
        if self.radio_var.get()<1 or self.radio_var.get()>4: 
            self.label1.config(text="Error: select algorithm you want before learning~")
            return 0

        if not learn_flag: 
            self.click_info()
            print "not learn_flag is: " + str(learn_flag)
        if learn_flag:
            print "learn_flag is: " + str(learn_flag)
            accur, sup, not_sup = learnfunction (self.user_input.get()+"/", self.pass_input.get(),
                    int(self.pass_inputL.get()), int(self.pass_inputR.get()), self.radio_var.get())

            global next_bt_ms
            start_bt_ms = "The accuracy of classifier: "+accur
            next_bt_ms = "Class 1 number: "+sup+", class 2 number: "+not_sup
            self.label1.config(text=start_bt_ms)
            self.label2.config(text=next_bt_ms)

    def click_info(self, event=None):
        file1 = self.user_input.get()+"/positive.txt"
        file2 = self.user_input.get()+"/negative.txt"

        global start_bt_ms
        if os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(self.pass_input.get()):
            info = "Indicated labeled file exist, " 
            line_num = min(sum(1 for line in open(file1)), sum(1 for line in open(file2)))
            info += "maximum line num is: " + str(line_num)
            self.pass_inputL.delete(0, tk.END)
            self.pass_inputL.insert(0, line_num)
            start_bt_ms = info
            self.label1.config(text=info)

            info2 = "Indicated unlabeled file exist, "
            line_num2 = sum(1 for line in open(self.pass_input.get()))
            info2 += "line num is: " + str(line_num2)
            self.pass_inputR.delete(0, tk.END)
            self.pass_inputR.insert(0, line_num2)
            self.label2.config(text=info2)
            global learn_flag
            learn_flag = True

        elif not os.path.isfile(file1): 
            start_bt_ms = "Error: Labeled file 'positive.txt' doesn't exist in the path~"
            self.label1.config(text=start_bt_ms)
            self.label2.config(text=next_bt_ms)
        elif not os.path.isfile(file2):
            start_bt_ms = "Error: Labeled file 'negative.txt' doesn't exist in the path~"
            self.label1.config(text=start_bt_ms)
            self.label2.config(text=next_bt_ms)
        else:
            start_bt_ms = "Error: Indicated unlabeled file doesn't exist~"
            self.label1.config(text=start_bt_ms)
            self.label2.config(text=next_bt_ms)


    def click_cancel(self, event=None):
        print "The user clicked 'Cancel'"
        self.master.destroy()


def learning():
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

