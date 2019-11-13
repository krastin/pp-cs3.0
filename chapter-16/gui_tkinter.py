import tkinter

window = tkinter.Tk()

"""
label = tkinter.Label(window, text='This is our label.')
label.pack()
label.config(text='Second label.')
"""

data = tkinter.StringVar()
data.set('Data to display')
label = tkinter.Label(window, textvariable=data)
label.pack()

window.mainloop()