import multiprocessing
from run_model import run_model # For TIM-Net
from TRE import TRE 
from multiprocessing import Process

# if __name__ == "__main__":
#     manager = multiprocessing.Manager()

file_path = "E:/University Courses/CSE400/project code/Capstone-Project-Modified-TIM-Net_SER/Code/COMBINED/COMBINED/Disgust/F_01_OISHI_S_1_DISGUST_1.wav"

text = "Just kind of feel numb, you know."

timnet_res=run_model(file_path)
tre_res = TRE(text)

# Weighted Averaging
accuracy_timnet = 0.7165
accuracy_tre = 0.7394
weight_timnet = accuracy_timnet/(accuracy_timnet+accuracy_tre)
weight_tre = accuracy_tre/(accuracy_timnet+accuracy_tre)
multi_model_res=[]
for i in range(len(timnet_res)):
    multi_model_res.append((timnet_res[i]*weight_timnet) + (tre_res[i]*weight_tre))
print(multi_model_res)