import tkinter
import tkinter.filedialog as dialog

class Editor:
    """ a gui text editor """

    def __init__(self, root):
        text = tkinter.Text(root)
        text.pack()

        menubar = tkinter.Menu(root)
        filemenu = tkinter.Menu(menubar)

        filemenu.add_command(label='Save', command=lambda : self.save(root, text))
        filemenu.add_command(label='Quit', command=lambda : self.quit(root))
        menubar.add_cascade(label = 'File', menu=filemenu)

        root.config(menu=menubar)


    def save(self, root, text):
        data = text.get('0.0', tkinter.END)
        filename = dialog.asksaveasfilename(parent=root,
                                            filetypes=[('Text', '*.txt')],
                                            title='Save as...')
        writer = open(filename, 'w')
        writer.write(data)
        writer.close()

    def quit(self, root):
        root.destroy()

if __name__ == '__main__':
    window = tkinter.Tk()
    myapp = Editor(window)
    window.mainloop()