
"""
Input:
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
from scipy.signal import find_peaks_cwt


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
    #if marked_point[j+1]!=0:
    no=j+1
    #plt.figure(figsize=(20,5))
    current=np.array(data["Item"+str(no)+".avgBright"])
    #normBright,normBright_max,normBright_mean,diff,normBright_mean1=normBright_MaxMin_diff(np.array(data["Item3.avgBright"]),60)
    norm_max=knn_norm(current, 60,"max")
    norm_min=knn_norm(current, 60,"min")
    diff=norm_max-norm_min
    ndiff=knn_norm(diff,8000,"mean")
    #plt.hlines(np.mean(ndiff)*1.2,0,len(ndiff),colors='orange')

    increase_point=np.where(ndiff>np.mean(ndiff)*1.2)[0][0]
    #plt.vlines(increase_point,0,np.max(ndiff),colors='green',label='first peak point')
    cut=ndiff[:increase_point]
    #plt.vlines(marked_point[no], 0,np.max(cut), linestyles='--', color='orange', label='Hatching point by Jonathan')

    x = np.linspace(0, len(cut), len(cut))
    maxs =find_peaks_cwt(cut[10000:],500)
    #plt.plot(x[maxs+10000], ndiff[maxs+10000], 'o',color='blue', label='maxs')
    maxs+=10000
    cuted=maxs[-2]
    cut=cut[maxs[-2]:maxs[-1]]
    mins =find_peaks_cwt(cut**-1,80)
    mins+=cuted
    #plt.plot(x[mins+cuted], ndiff[mins+cuted], 'o',color='red', label='mins')
    for i in range(len(mins)):
        if i ==0:
            if cut[mins[::-1][i]] > cut[mins[::-1][i-1]]:
                output.append(mins[::-1][i-1])
                break

print("Hatching complete point list is:",output)

