import tkinter

def convert():
    var_output.set((var_input.get() - 32) / 1.8)

window = tkinter.Tk()

frame = tkinter.Frame()
frame.pack()

label_title = tkinter.Label(frame, text='Temperature in Fahrenheit:')
label_title.pack()

var_input = tkinter.DoubleVar()
var_output = tkinter.DoubleVar()

entry = tkinter.Entry(frame, textvariable=var_input)
entry.pack()

label_result = tkinter.Label(frame, textvariable=var_output)
label_result.pack()

button_convert = tkinter.Button(frame, text='Convert to Celsius', command=convert)
button_convert.pack()
button_quit = tkinter.Button(frame, text='Quit', command=window.destroy)
button_quit.pack()

window.mainloop()