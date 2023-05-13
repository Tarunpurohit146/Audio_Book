from tkinter import *
import threading
from tkinter import filedialog
import pyttsx3
import sys
import PyPDF2
from tkinter import messagebox
root=Tk()
root.title('Audio Book')
engine=pyttsx3.init()
class speaking(threading.Thread):
    def __init__(self,sentence):
        super().__init__()
        self.word=sentence
        self.paused=False
    def run(self):
        self.running=True
        while self.word and self.running:
            if not self.paused:
                word = self.word.pop(0)
                engine.say(word)
                engine.runAndWait()
        self.running=False
    def pause(self):
        self.paused = True
    def resume(self):
        self.paused = False
    def stop(self):
        self.running=False
speak=None
def stop():
    global speak
    if speak:
        speak.stop()
        speak = None
    sublab.config(text='File')  
def read():
    global speak
    filetype=filedialog.askopenfilename(title="select file",
                                        initialdir='/',
                                        filetypes=(('text','*.txt'),('pdf','*.pdf'))
    )
    file=filetype.split('.')
    sublab.config(text=f'File:{filetype}')
    mainread=[]
    try:
        if file[1]=='txt':
            with open(filetype) as text:
                readcon=text.readlines()
                for i in readcon:
                        mainread.append(i.split())

        elif file[1]=="pdf":
            with open("test.pdf",'rb') as pdf:
                pdfread=PyPDF2.PdfFileReader(pdf)
                for i in range(pdfread.numPages):
                    pdfobj=pdfread.getPage(i)
                    mainread=[i for i in pdfobj.extractText().split('\n')]
    except:
        messagebox.showinfo('Error','File not Selected')
    speak = speaking(mainread) 
    speak.start()
def pause():
    if speak:
        speak.pause()
def unpause():
    if speak:
        speak.resume()
lab1=Label(root,text="Audio Book",font=("Comic Sans MS", 20, "bold"),foreground="white",background='#317773').place(x=130,y=30)
select_button=Button(root,text="Select File",font=("Comic sans MS",10),command=read,background="#E2D1F9",foreground='black').place(x=155,y=180)
sublab=Label(root,text="File:",font=('comic sans ms',12,"bold"),foreground="white",background="#317773")
sublab.place(x=90,y=130)
pause_button = Button(root, text="Pause", command=pause,font=('comic sans ms',10),width=10,background="#E2D1F9",foreground='black').place(x=40,y=250)
unpause_button = Button(root, text="Resume", command=unpause,font=('comic sans ms',10,),background="#E2D1F9",foreground='black',width=10).place(x=155,y=250)
stop_button = Button(root, text="Stop", command=stop,font=('comic sans ms',10),width=10,background="#E2D1F9",foreground='black').place(x=270,y=250)
root.config(background="#317773")
root.geometry('400x350')
root.mainloop()
sys.exit()