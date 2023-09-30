import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backend_bases import RendererBase
import os
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils import data
# import torchvision.datasets as datasets
# import torchvision.transforms as transforms
from tensorboardX import SummaryWriter
from transformers import BertModel, BertTokenizer
import torch
from transformers import get_linear_schedule_with_warmup
from transformers import BertForSequenceClassification, AdamW, BertConfig


def TRE(text:str):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    best_model = torch.load("E:/University Courses/CSE400/project code/TRE/model_TRE.pt")
    # best_model.eval()
    text = "Just kind of feel numb, you know."

    input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
    with torch.no_grad():
        # Assuming your model takes both text and audio inputs
        output = best_model(input_ids)[0]

        # Process the model output to get predictions
        # _, preds = torch.max(output, 1)
        probabilities = torch.softmax(output, dim=1)


    # print("Predicted label:", probabilities.tolist())
    # tre_res=(probabilities.tolist())[0]
    return (probabilities.tolist())[0]