from run_model import run_model # For TIM-Net
# from TRE import TRE

file_path = "E:/University Courses/CSE400/project code/Capstone-Project-Modified-TIM-Net_SER/Code/SER_WAV_DATA/COMBINED_NEW/Happy/03-01-01-01-01-01-03.wav"
# file_path = "C:/Users/gazif/OneDrive/Documents/Sound Recordings/Recording.wav"

text = "Well, I can see that."
# text = "Isn't it a great day to be outside"

timnet_res=run_model(file_path)
# tre_res = TRE(text)

# temp = tre_res[0]
# tre_res[0] = tre_res[3]
# tre_res[3] = tre_res[1]
# tre_res[1] = tre_res[2]
# tre_res[2] = temp

# # Weighted Averaging
# accuracy_timnet = 0.7165
# accuracy_tre = 0.7394
# weight_timnet = accuracy_timnet/(accuracy_timnet+accuracy_tre)
# weight_tre = accuracy_tre/(accuracy_timnet+accuracy_tre)
# multi_model_res=[]
# for i in range(len(timnet_res)):
#     multi_model_res.append((timnet_res[i]*weight_timnet) + (tre_res[i]*weight_tre))
# print(multi_model_res)