from pymy_audio import AudioConvert
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

def interface():
    print ('this is a comandline interface to convert audio files')
    print('supported extentions so far: MP3, WAV \n')
    #REMOVING THIS BIT IN ORDER TO USE DIALOGBOX
    #src = input('enter the audio filename?\n')
    #src_path  = input('where is your file?\n')
    #-------------------------------------------
    src = filedialog.askopenfilename() #Adding dialog box
    dts = input('what will you call the new file?\n')
    from_format = input("whats format is the file?\n")
    to_format = input("to what format?\n")
    to_rate_khz = input('to what hz rate? eg: 44100?\n')
    if 'mp3' == from_format.lower() and 'wav' == to_format.lower():
        rate = input('what bit rate for the file?\n')
        AudioConvert(src=src, src_path=src, dst=dts, rate=rate).mp3_to_wav()
    elif 'wav' == from_format.lower() and 'mp3' == to_format.lower():
        AudioConvert(src=src, src_path=src, dst=dts).wav_to_mp3()
    else:
        print("one or both are unsupported formates")

interface()
