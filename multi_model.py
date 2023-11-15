from run_model import run_model # For TIM-Net
import numpy as np
# from TRE import TRE

results = [] #for bulk test
# angry, fear, happy, neutral, sad = 0
for i in range(32):
    file_path = f"sound recordings/sad_{i+1}.wav"

    text = "Well, I can see that."

    timnet_res=run_model(file_path)
    results.append(timnet_res) 
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
angry, fear, happy, neutral, sad = 0,0,0,0,0
for i in range(32):
    if np.array(results[i]).argmax() == 0:
        angry+=1
    elif np.array(results[i]).argmax() == 1:
        fear+=1
    elif np.array(results[i]).argmax() == 2:
        happy+=1
    elif np.array(results[i]).argmax() == 3:
        neutral+=1
    elif np.array(results[i]).argmax() == 4:
        sad+=1
    print(f"{i+1}: {results[i]}")
print(f"angry: {angry}")
print(f"fear: {fear}")
print(f"happy: {happy}")
print(f"neutral: {neutral}")
print(f"sad: {sad}")