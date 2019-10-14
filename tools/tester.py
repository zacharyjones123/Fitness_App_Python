import tkinter as tk

parent = tk.Tk()

parent.grid_columnconfigure(1, weight=1)

canvas = tk.Canvas(parent, highlightbackground="black", highlightthickness=1)
scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)
# group of widgets
for i in range(20):
    tk.Label(frame, text='label %i' % i).pack()
# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.grid(row=0, column=0)
scroll_y.grid(row=0, column=1, columnspan=2, sticky="nsew")

parent.mainloop()