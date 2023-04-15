from tkinter import *
import krypmessage1
import filespath 

class Dashboard:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.bottomframe = Frame(self.root)
        self.bottomframe.pack( side = BOTTOM )
        self.redbutton = Button(self.frame, text = 'Text Encryption', fg ='red', command=self.encrdetext)
        self.redbutton.pack( side = LEFT)
        self.greenbutton = Button(self.frame, text = 'File Ecryption', fg='brown', command=self.encs)
        self.greenbutton.pack( side = LEFT )
        self.bluebutton = Button(self.frame, text = 'File Decryption', fg='blue',command=self.decs)
        self.bluebutton.pack( side = LEFT )
        self.root.mainloop()
        
    def encrdetext(self):
        self.root.destroy()
        self.ende = krypmessage1.Messagekrypt()
        
    def encs(self):
        self.root.destroy()
        self.ob=filespath.choosefile("encryption")
        
    def decs(self):
        self.root.destroy()
        self.ob=filespath.choosefile("decryption")
        

if __name__ == '__main__':
    message = Dashboard()