# testing old code for tkinter
from tkinter import *
fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')
root = Tk()
entries = {}
for field in fields:
    row = Frame(root)
    lab = Label(row, width=22, text=field+": ", anchor='w')
    ent = Entry(row)
    ent.insert(0,"0")
    row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
    lab.pack(side = LEFT)
    ent.pack(side = RIGHT, expand = YES, fill = X)
    entries[field] = ent

root.bind('<Return>', lambda event: fetch(entries))
b1 = Button(root, text = 'Final Balance',command=None)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text='Monthly Payment',command=None)
b2.pack(side = LEFT, padx = 5, pady = 5)
root.mainloop()