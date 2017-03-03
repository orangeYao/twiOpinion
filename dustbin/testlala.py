import Tkinter as tk

class simpleapp_tk(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = tk.Button(self,text=u"Click me !", command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self, anchor="w",fg="white",bg="blue", textvariable=self.labelVariable)
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())   
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

        #tk.Button(self, text='OK', default='active', command=self.click_ok).pack(side='right')
        #tk.Button(self, text='Cancel', command=self.click_cancel).pack(side='right')

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

    def click_ok(self):
        print("The user clicked 'OK'")

    def click_cancel(self):
        print("The user clicked 'Cancel'")


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
