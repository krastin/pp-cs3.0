import tkinter

window = tkinter.Tk()

button = tkinter.Button(window, text='Hello',
font=('Courier', 14, 'bold italic'))
button.pack()

button2 = tkinter.Label(window, text='Hello', bg='green', fg='white')
button2.pack()

window.mainloop()