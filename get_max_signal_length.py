import librosa
import os

# Define the path to your audio dataset
dataset_path = "D:/University/CSE400/Capstone-Project-Modified-TIM-Net_SER/SER_WAV_DATA/SUBESCO"

# Initialize variables to keep track of maximum signal length
max_signal_length = 0

# print(os.listdir(dataset_path))
for directory in os.listdir(dataset_path):
    # Iterate through audio files in the dataset
    # print(os.listdir(dataset_path+"/"+directory))
    for audio_file in os.listdir(dataset_path+"/"+directory):
        # Load the audio file
        audio_path = dataset_path+"/"+ directory+"/"+audio_file
        
        # Get the signal length in samples
        y, sr = librosa.load(audio_path)
        signal_length = len(y)
        
        # Update the max signal length
        if max_signal_length < signal_length:
            max_signal_length =  signal_length

# Print the max signal length
print(f"Max signal length in the dataset: {max_signal_length} samples")