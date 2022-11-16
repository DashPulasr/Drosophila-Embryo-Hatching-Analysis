
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filePath = "../data/"
fileName=input("Please input filename:")
data = pd.read_csv(filePath + fileName)

def knn_norm(data, k=7, mode="max"):
    lenth = len(data)
    output_list = []
    for i in range(lenth - k):
        if mode == "max":
            output_list.append((np.max(data[i:i + k])))
        elif mode == "mean":
            output_list.append((np.mean(data[i:i + k])))
        elif mode == "min":
            output_list.append((np.min(data[i:i + k])))
    return np.hstack((np.ones(lenth-len(output_list))*output_list[0],np.array(output_list)))


output=[]
for j in range(24):
    no=j+1
    normBright = np.array(data["Item" + str(no) + ".avgBright"])
    normBright_max = knn_norm(normBright, 60, "max")
    normBright_min = knn_norm(normBright, 60, "min")
    diff = normBright_max - normBright_min
    cut= diff[0:5000]
    threshold= np.max(cut)
    output.append(np.where(diff>threshold)[0][0])
print("Hatching onset point list is:",output)
