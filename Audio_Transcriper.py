import whisper
import tkinter
from tkinter import filedialog
import customtkinter
import os
import pathlib
from pathlib import Path
from tkinter import *

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Audio Transcription")

def filePath():
    global output_path 
    output_path = filedialog.askopenfilename()
    outputPathText = customtkinter.CTkLabel(app, text=output_path) 
    outputPathText.pack()



audioPathText = customtkinter.CTkButton(app, text="Select File for Transcriping", command=filePath)  
audioPathText.pack()


def show():
    label.config( text = clicked.get() )

#Transcriper
def Transcriper ():
    model = whisper.load_model("medium")
    result = model.transcribe(output_path)
    loading = "Loading..."
    loadingMessage = customtkinter.CTkLabel(app, text=loading)
    loadingMessage.pack()
    
    with open("transcription.txt", "w") as f:
        f.write(result["text"])
        loading = "Done!"

transcripe = customtkinter.CTkButton(app, text="Transcripe File", command=Transcriper) 
transcripe.pack(padx=10, pady=10)


# Run app
app.mainloop()