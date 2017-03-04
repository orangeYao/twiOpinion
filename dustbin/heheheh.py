import Tkinter as tk

def OnClickA(event):
    print "you clicked on", event.widget
    event.widget.config(text="Thank you!")


def OnClickB(event, obj):
    print "you clicked on", obj
    obj.config(text="Thank you!")

root = tk.Tk()
l1 = tk.Label(root, text="Click me")
l2 = tk.Label(root, text="No, click me!")
l1.pack()
l2.pack()

l1.bind("<1>", OnClickA)
l2.bind("<1>", lambda event, obj=l2: OnClickB(event, obj))

root.mainloop()
