import tkinter

def click():
    counter.set(counter.get() + 1)

window = tkinter.Tk()
counter = tkinter.IntVar(value=0)

frame = tkinter.Frame()
frame.pack()

button = tkinter.Button(frame, textvariable=counter, command=click)
button.pack()

window.mainloop()