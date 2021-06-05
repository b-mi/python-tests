import tkinter

width, height = 640, 480
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

canvas.create_text(100, 100, text="eee")




def motion(event):
    print('motion', event)

def drag(event):
    print('drag', event)

def press(event):
    print('press', event)

def release(event):
    print('release', event)

canvas.bind("<ButtonPress-1>", press)
canvas.bind("<ButtonRelease-1>", release)
canvas.bind("<Motion>", motion)
canvas.bind("<B1-Motion>", drag)

canvas.mainloop()
