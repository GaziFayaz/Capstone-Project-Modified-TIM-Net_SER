from pydub import AudioSegment
import math

class SplitWavAudio():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")
        
    def multiple_split(self, secs_per_split):
        print(self.get_duration())
        total_secs = math.ceil(self.get_duration())
        for i in range(0, total_secs, secs_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+secs_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_secs - secs_per_split:
                print('All splited successfully')
                
                
folder = 'E:/University Courses/CSE400/project code/Capstone-Project-Modified-TIM-Net_SER/Code/COMBINED/temp'
file = '03-01-03-02-01-01-01.wav'
split_wav = SplitWavAudio(folder, file)
split_wav.multiple_split(secs_per_split=3)