from tkinter import *
from tkinter import filedialog
import encrypt
import decrypt

class choosefile:
    def __init__(self,type):
        global file_path
        self.tc=type
        self.tx = Tk()
        self.file_path = self.get_file_path()
        # Open and return file path
        #self.file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi"),("img","*.jpeg"),("pic","*.jpg")))
        #self.l1 = Label(self.tx, text = "File path: " + self.file_path).pack()
        self.l1 = Label(self.tx, text = "File path: " + self.file_path).pack()
        
        # Creating a button to search the file
        #self.b1 = Button(self.tx, text = "Open File", command = get_file_path).pack()
        self.b2 = Button(self.tx, text = "Next", command= self.abc if self.tc=="encryption" else self.xyz).pack()
        self.b3 = Button(self.tx, text = "Back", command=self.ext).pack()
        self.tx.mainloop()
        
    def ext(self):
        self.tx.destroy()
        self.dash = mainfile.Dashboard()

    def abc(self):
        self.tx.destroy()
        self.ob=encrypt.Encrypt(self.file_path)
    
    def xyz(self):
        self.tx.destroy()
        self.ob=decrypt.Decrypt(self.file_path)
    
    def get_file_path(self):
    # Open and return file path
        file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi"),("docx","*.docx")))
        return file_path

    
