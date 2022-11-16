import numpy as np


def Average_bout_length(rawdata,onset_point,hatching_point,window_size):
    output=[]
    for i in rawdata:

        bouts=[]
        current = (rawdata[onset_point[i]:hatching_point[i]])
        count=0
        if i % window_size != 0:
            count=0
        for j in range(len(current)):
            if i==0:
                continue
            if current[i]!=0:
                count+=1
            elif current[i]==0:
                bouts.append(count)
                count=0
        output.append(np.mean(bouts))
    return output