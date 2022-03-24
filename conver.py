from pymy_audio import AudioConvert


def interface():
    print ('this is a comandline interface to convert audio files')
    print('supported extentions so far: MP3, WAV \n')
    src = input('enter the audio filename?\n')
    src_path  = input('where is your file?\n')
    dts = input('what will you call the new file?\n')
    from_format = input("whats format is the file?\n")
    to_format = input("to what format?\n")
    if 'mp3' == from_format.lower() and 'wav' == to_format.lower():
        AudioConvert(src=src, src_path=src_path, dst=dts).mp3_to_wav()
    elif 'wav' == from_format.lower() and 'mp3' == to_format.lower():
        AudioConvert(src=src, src_path=src_path, dst=dts).wav_to_mp3()
    else:
        print("one or both are unsupported formates")

interface()
