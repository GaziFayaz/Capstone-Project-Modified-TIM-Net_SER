import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import multiprocessing
from run_model import run_model  # For TIM-Net
import numpy as np

def models(model_number, file_path, result_list, lock):
    # Your code goes here
    # from TRE import TRE

    # angry, fear, happy, neutral, sad
    file_path = file_path

    text = "Well, I can see that."

    timnet_res = run_model(file_path, model_number[0]) # model_number is a list with only one value, so send it as the first value of the list
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
    
    
    with lock:
        result_list.append(timnet_res)

if __name__ == "__main__":
    all_res = []
    for file_number in range(10):
        
        manager = multiprocessing.Manager()
        processes = []
        values = list(range(1,11))
        model_results = manager.list()
        
        lock = manager.Lock()
        
        for model in range(10):
            file_path = f"D:/University/CSE400/Capstone-Project-Modified-TIM-Net_SER/audio-sabbir/Dataset/Angry/{file_number+1}_SM_SABBIR_ANGRY.wav"
            process = multiprocessing.Process(target=models, args=(([values[model]]), file_path, model_results, lock))
            processes.append(process)
            process.start()
            
        for process in processes:
            process.join()
            
        avg_result = [0, 0, 0, 0, 0] 
        for i in range(len(model_results)):   
            for j in range(len(model_results[i])):
                avg_result[j] += model_results[i][j]
        for i in range(len(avg_result)):
            avg_result[i] /= len(model_results)     
        print(f"{file_number+1}: {avg_result}")
        if np.array(avg_result).argmax() == 0:
            print("angry")
        elif np.array(avg_result).argmax() == 1:
            print("fear")
        elif np.array(avg_result).argmax() == 2:
            print("happy")
        elif np.array(avg_result).argmax() == 3:
            print("neutral")
        elif np.array(avg_result).argmax() == 4:
            print("sad")
            
        all_res.append(avg_result)
    
    angry, fear, happy, neutral, sad = 0,0,0,0,0
    for i in range(10):
        if np.array(all_res[i]).argmax() == 0:
            angry+=1
        elif np.array(all_res[i]).argmax() == 1:
            fear+=1
        elif np.array(all_res[i]).argmax() == 2:
            happy+=1
        elif np.array(all_res[i]).argmax() == 3:
            neutral+=1
        elif np.array(all_res[i]).argmax() == 4:
            sad+=1
        print(f"{i+1}: {all_res[i]}")
    print(f"angry: {angry}")
    print(f"fear: {fear}")
    print(f"happy: {happy}")
    print(f"neutral: {neutral}")
    print(f"sad: {sad}")
        
        
            
    