import tkinter

def click():
    a = 0
    c = 0
    t = 0
    g = 0
    for character in text.get('0.0', tkinter.END):
        if character == 'A':
            a += 1
        elif character == 'C':
            c += 1
        elif character == 'T':
            t += 1
        elif character == 'G':
            g += 1
    var_label.set("Num As: %d Num Ts: %d Num Cs: %d Num Gs: %d" % (a, t, c, g))

window = tkinter.Tk()
var_label = tkinter.StringVar(value='Enter a DNA Sequence and press Count!')

frame = tkinter.Frame()
frame.pack()

text = tkinter.Text(frame, height=12, width=60)
text.pack()

button = tkinter.Button(frame, text='Count', command=click)
button.pack()

label = tkinter.Label(frame, textvariable=var_label)
label.pack()

window.mainloop()