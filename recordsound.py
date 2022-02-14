from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound as ps
recordsound = Tk()
recordsound.title('record sound')
recordsound.geometry("450x50")
recordsound.resizable(0,0)
name_record=ttk.Label(recordsound,text='Name record :')
name_record.place(x=10,y=12)
Entry_name=ttk.Entry(recordsound,width=30)
Entry_name.place(x=100,y=12)
button_record=ttk.Button(recordsound,text='Record')
button_record.place(x=290,y=10)

button_play=ttk.Button(recordsound,text='Play')
button_play.place(x=370,y=10)
def recordnow():

    if Entry_name.get()=='':
        messagebox.showinfo("Record","please enter name")
    else:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                wiki=r.recognize_google(audio)
            tts = gTTS(wiki, lang='en')
            tts.save(Entry_name.get()+".mp3")
            messagebox.showinfo("Record","Text Converted Successfully ")
        except Exception as e:
            messagebox.showinfo("Record","sorry is error")
button_record.configure(command=recordnow)

def playnow():
    if Entry_name.get() == '':
        messagebox.showinfo("Record","please enter name")
        
    else:
       ps(Entry_name.get()+".mp3")

button_play.configure(command=playnow)
recordsound.mainloop()
