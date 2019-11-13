import tkinter

# The controller.
def click_up():
    counter.set(counter.get() + 1)

def click_down():
    counter.set(counter.get() - 1)

def click(var, value):
    var.set(var.get() + value)

if __name__ == '__main__':
    window = tkinter.Tk()
    
    # The model.
    counter = tkinter.IntVar()
    counter.set(0)

    # The views.
    frame = tkinter.Frame(window)
    frame.pack()
    button_up = tkinter.Button(frame, text='Click +1', command=lambda: click(counter, 1))
    button_up.pack()
    button_down = tkinter.Button(frame, text='Click -1', command=lambda: click(counter, -1))
    button_down.pack()
    label = tkinter.Label(frame, textvariable=counter)
    label.pack()
    # Start the machinery!
    window.mainloop()