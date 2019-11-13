import tkinter

def quit():
    window.destroy()

window = tkinter.Tk()

frame = tkinter.Frame()
frame.pack()

button = tkinter.Button(frame, text='Goodbye', command=quit)
button.pack()

window.mainloop()