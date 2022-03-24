# this script is intended to converto mp3 to and from wav format

from pathlib import Path
from pydub import AudioSegment


class AudioConvert:
    def __init__(self, src, src_path=None, dst="new"):
        self.path = str(Path.home() / "Music")
        if src_path:
            src = str(Path.home() / src_path) + f'/{src}'
        self.src = src
        self.dst = self.path + f'/{dst}'
    
    def mp3_to_wav(self):
        try:        
            sound = AudioSegment.from_mp3(self.src)
            sound.export(self.dst, format="wav")
            return f"success!!! your file is here: {self.dst}"
        except:
            return "someting wnet wrong check you file extention or path"

    def wav_to_mp3(self):
        try:        
            sound = AudioSegment.from_wav(self.src)
            sound.export(self.dst, format="mp3")
            return f"success!!! your file is here: {self.dst}"
        except:
            return "someting wnet wrong check you file extention or path"
