# this script is intended to converto mp3 to and from wav format

from pathlib import Path
from pydub import AudioSegment
import subprocess

class AudioConvert:
    def __init__(self, src, src_path=None, dst="new", rate=16):
        self.path = str(Path.home() / "Music")
        if src_path:
            src = str(Path.home() / src_path) + f'/{src}'
        self.src = src
        self.dst = self.path + f'/{dst}'
        self.rate = rate
    
    def mp3_to_wav(self):
        try:
            self.dst += ".wav"
            sound = AudioSegment.from_mp3(self.src)
            sound.export(self.dst,format="wav")
            name = '/24-' + self.dst.split('/')[-1]
            command = f'sox {self.dst} -b {self.rate} {self.path + name}'
            subprocess.call(command, shell=True)
            return f"success!!! your file is here: {self.dst}"
        except:
            return "someting wnet wrong check you file extention or path"

    def wav_to_mp3(self):
        try:
            self.dst += ".mp3"
            sound = AudioSegment.from_wav(self.src)
            sound.export(self.dst, format="mp3")
            return f"success!!! your file is here: {self.dst}"
        except:
            return "someting wnet wrong check you file extention or path"
