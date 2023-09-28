import os
import librosa
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.models import load_model
from Model import TIMNET_Model
import pandas as pd
from TIMNET import TIMNET
import numpy as np
from typing import Tuple
from tqdm import tqdm
import librosa.display
from tensorflow.keras.utils import to_categorical

def get_feature(file_path: str, feature_type:str="MFCC", mean_signal_length:int=90789, embed_len: int = 39):
    feature = None
    signal, fs = librosa.load(file_path)# Default setting on sampling rate
    s_len = len(signal)
    if s_len < mean_signal_length:
        pad_len = mean_signal_length - s_len
        pad_rem = pad_len % 2
        pad_len //= 2
        signal = np.pad(signal, (pad_len, pad_len + pad_rem), 'constant', constant_values = 0)
    else:
        pad_len = s_len - mean_signal_length
        pad_len //= 2
        signal = signal[pad_len:pad_len + mean_signal_length]
    if feature_type == "MFCC":
        mfcc =  librosa.feature.mfcc(y=signal, sr=fs, n_mfcc=embed_len)
        feature = np.transpose(mfcc)
    return feature

def generate_csv(file_path:str, feature_type: str="MFCC", embed_len: int = 39, mean_signal_length:int = 90789, class_labels: Tuple = ("angry", "boredom", "disgust", "fear", "happy", "neutral","sad")):
    temp_size_ = True
    feature_vector = get_feature(file_path = file_path, feature_type=feature_type, mean_signal_length=mean_signal_length, embed_len = embed_len)
    if temp_size_:
        print(f"### Feature Size:{feature_vector.shape} ###")
        temp_size_ = False
    x, y = process_csv(feature_vector)
    y = to_categorical(y, num_classes=len(class_labels))
    data = {"x": x, "y": y}
    return data

def process_csv(feature_vector, mfcc_len: int = 39, class_labels: Tuple = ("angry", "boredom", "disgust", "fear", "happy", "neutral","sad"), flatten: bool = False):
    x = []
    y = []
    for i, directory in enumerate(class_labels):
        x.append(feature_vector)
        y.append(i)
        # print("appended in y: ", i)
    return np.array(x), np.array(y)

def extract_feature(file_path:str, feature_type_:str="MFCC", mean_signal_length:int=90789, class_labels:Tuple = ("angry", "boredom", "disgust", "fear", "happy", "neutral","sad")):
    data = generate_csv(file_path=file_path, class_labels=class_labels, feature_type=feature_type_, mean_signal_length=mean_signal_length)
    return data



# CLASS_LABELS = ("Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise")
CLASS_LABELS = ("angry", "happy", "neutral", "sad")

# print(extract_feature(file_path="E:/University Courses/CSE400/project code/TIM-Net_SER/Code/COMBINED/COMBINED/Angry/03-01-03-02-01-01-03.wav"))


# "./MFCC/COMBINED.npy"
# print(get_feature("E:/University Courses/CSE400/project code/TIM-Net_SER/Code/COMBINED/COMBINED/Angry/03-01-03-02-01-01-03.wav"))
# data = np.load("./MFCC/IEMOCAP.npy", allow_pickle=True).item()
data = extract_feature(file_path="E:/University Courses/CSE400/project code/Capstone-Project-Modified-TIM-Net_SER/Code/COMBINED/COMBINED/Disgust/F_01_OISHI_S_1_DISGUST_1.wav")
# print(data["x"].shape)
x_source= data["x"]
y_source = data["y"]

print(x_source.shape[1:])
model = TIMNET_Model( input_shape=x_source.shape[1:], class_label= CLASS_LABELS)
loaded_model = model.run_prediction(x_source, y_source)
print("Model Created")
pred = loaded_model.predict(x_source)        
print(pred[0])
# return pred[0]


# model.load_weights("E:/University Courses/CSE400/project code/TIM-Net_SER/Code/Models/COMBINED_46_2023-09-26_00-01-24/5-fold_weights_best_3.hdf5")
