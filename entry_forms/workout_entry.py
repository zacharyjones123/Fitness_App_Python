from tkinter import *

if __name__ == '__main__':
    root = Tk()
    b1 = Button(root, text='Enter Exercise')
    b1.grid(row=0, column=0, padx=5, pady=5)
    b2 = Button(root, text='Reset')
    b2.grid(row=0, column=1, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.grid(row=0, column=2, padx=5, pady=5)
    l1 = Label(root, text='Exercise')
    l1.grid(row=1, column=0, padx=5, pady=5)
    b4 = Entry()
    b4.grid(row=1, column=1, padx=5, pady=5)
    l2 = Label(root, text='Num Of Sets')
    l2.grid(row=2, column=0, padx=5, pady=5)
    b5 = Entry()
    b5.grid(row=2, column=1, padx=5, pady=5)
    set1 = Label(root, text='Set 1')
    set1.grid(row=3, column=0, padx=5, pady=5)
    set1_entry = Entry()
    set1_entry.grid(row=3, column=1, padx=5, pady=5)
    set2 = Label(root, text='Set 2')
    set2.grid(row=4, column=0, padx=5, pady=5)
    set2_entry = Entry()
    set2_entry.grid(row=4, column=1, padx=5, pady=5)
    set3 = Label(root, text='Set 3')
    set3.grid(row=5, column=0, padx=5, pady=5)
    set3_entry = Entry()
    set3_entry.grid(row=5, column=1, padx=5, pady=5)
    set4 = Label(root, text='Set 4')
    set4.grid(row=6, column=0, padx=5, pady=5)
    set4_entry = Entry()
    set4_entry.grid(row=6, column=1, padx=5, pady=5)
    root.mainloop()