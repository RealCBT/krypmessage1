import tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import base64   


class Messagekrypt():
    def __init__(self):
        
        self.master = Tk()
        self.master.iconbitmap(r'C:\Users\tiwar\Desktop\picture1_TqH_icon.ico')
        self.master.geometry("890x290")
        self.master.minsize(890,290)
        self.master.maxsize(890,290)
        self.master.title("CRYPTOGRAPHY APPLICATION")
        self.create()
        self.master.mainloop()
  
    def create(self):
        self.f1 = Frame(self.master, width =890, height = 290, 
                            relief = SUNKEN) 
        self.f1.pack(side =TOP) 

        load=Image.open(r'C:\Users\tiwar\Desktop\BG1.jpg')
        load1=load.resize((890,290))
        self.man = ImageTk.PhotoImage(load1)
        

        # Create Canvas
        canvas1 = Canvas( self.f1, width = 890,
                 height = 290)
  
        canvas1.pack(fill = "both", expand = True)
  
        # Display image
        canvas1.create_image(0,0, image = self.man,anchor=NW)
  
        self.Msg = StringVar() 
        self.key = StringVar() 
        self.result = StringVar() 

  
# labels 
        canvas1.create_text( 250, 60, text ="MESSAGE:",font = ('arial', 16, 'bold'), anchor = "w",fill="Gainsboro")

        
        self.txtMsg = Entry(self.f1, font = ('arial', 16, 'bold'), 
         textvariable = self.Msg) 
        canvas1.create_window(500,60,window=self.txtMsg)


        canvas1.create_text( 250, 100, text ="KEY:",font = ('arial', 16, 'bold'), anchor = "w",fill="WHITE")

        
        self.txtkey = Entry(self.f1, font = ('arial', 16, 'bold'), 
         textvariable = self.key) 
        canvas1.create_window(500,100,window=self.txtkey)


        canvas1.create_text( 250, 140, text ="RESULT:",font = ('arial', 16, 'bold'), anchor = "w",fill="WHITE")

        
        self.txtservice = Entry(self.f1, font = ('arial', 16, 'bold'), 
         textvariable = self.result) 
        canvas1.create_window(500,140,window=self.txtservice)

        self.btnTotal1 = Button(self.f1, padx = 16, pady = 8, fg = "black", 
                        font = ('arial', 14, 'bold'), width = 10, 
                       text = "Encrypt",bg = "silver",command=self.Ref1)
        canvas1.create_window(140,220,window=self.btnTotal1)

        
        self.btnTotal2 = Button(self.f1, padx = 16, pady = 8, fg = "black", 
                        font = ('arial', 14, 'bold'), width = 10, 
                       text = "Decrypt",bg = "silver",
                         command = self.Ref2)
        canvas1.create_window(340,220,window=self.btnTotal2)
  

        self.btnReset = Button(self.f1, padx = 16, pady = 8, 
                  fg = "black", font = ('arial', 14, 'bold'), width = 10, text = "Reset",bg = "silver",
                   command = self.Reset)
        canvas1.create_window(540,220,window=self.btnReset)
  
  

        self.btnExit = Button(self.f1, padx = 16, pady = 8,  
                 fg = "black", font = ('arial', 14, 'bold'), width = 10, text = "Exit", bg = "FireBrick", 
                  command = self.qExit)
        canvas1.create_window(740,220,window=self.btnExit)
  


    def Ref1(self): 
        print("Encrypted Message= ", (self.Msg.get())) 
  
        clear = self.Msg.get() 
        k = self.key.get() 
  
        self.result.set(self.encode(k, clear)) 


    def Ref2(self): 
        print("Decrypted Message= ", (self.Msg.get())) 
  
        clear = self.Msg.get() 
        k = self.key.get() 
  
        self.result.set(self.decode(k, clear))

        
    def encode(self,key1, clear): 
        enc = [] 
      
        for i in range(len(clear)): 
            key_c = key1[i % len(key1)] 
            enc.append(chr((ord(clear[i])+ord(key_c)) % 256))
                       
        return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  

    def decode(self,key1, enc): 
        dec = [] 
      
        enc = base64.urlsafe_b64decode(enc).decode() 
        for i in range(len(enc)): 
            key_c = key1[i % len(key1)] 
            dec.append(chr((256 + ord(enc[i])-ord(key_c)) % 256)) 
                            
        return "".join(dec)  


    def qExit(self): 
        self.master.destroy() 
  

    def Reset(self): 
        self.Msg.set("") 
        self.key.set("") 
        self.result.set("") 


if __name__ == '__main__':
    message = Messagekrypt()
