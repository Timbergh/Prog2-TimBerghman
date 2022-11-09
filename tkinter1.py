from tkinter import *

root = Tk()
e = Entry(root, width=100)
e.pack()
b = Button(root, text ="Tryck mig!")
reverse = ""
x = len(str(e.get()))-1
for i in str(e.get()):
    reverse += str(e.get())[x]
    print(reverse)
    x -= 1
def click_handler(self):
    print(str(e.get()))
    lbl["text"] = e.get() + " baklänges blir: " + reverse
b.bind("<Button-1>", click_handler)
b.pack()
lbl = Label(root)
lbl.pack()
root.mainloop()

'''
ord = input("Skriv något: ")

reverse = ""
x = len(ord)-1
for i in ord:
    reverse += ord[x]
    x -= 1

print(reverse)
'''