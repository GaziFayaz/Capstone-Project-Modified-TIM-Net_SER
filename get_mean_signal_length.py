import librosa
import os

# Define the path to your audio dataset
dataset_path = "E:/University Courses/CSE400/project code/Capstone-Project-Modified-TIM-Net_SER/Code/COMBINED/COMBINED_NEW"

# Initialize variables to keep track of total signal length and the number of audio files
total_signal_length = 0
num_audio_files = 0

# print(os.listdir(dataset_path))
for directory in os.listdir(dataset_path):
    if(directory!="Disgust"):
        # Iterate through audio files in the dataset
        # print(os.listdir(dataset_path+"/"+directory))
        for audio_file in os.listdir(dataset_path+"/"+directory):
            # Load the audio file
            audio_path = dataset_path+"/"+ directory+"/"+audio_file
            
            # Get the signal length in samples
            y, sr = librosa.load(audio_path)
            signal_length = len(y)
            
            # Update the total signal length and the number of audio files
            total_signal_length += signal_length
            num_audio_files += 1

# Calculate the mean signal length
mean_signal_length = total_signal_length / num_audio_files

# Print the mean signal length
print(f"Mean signal length in the dataset: {mean_signal_length} samples")