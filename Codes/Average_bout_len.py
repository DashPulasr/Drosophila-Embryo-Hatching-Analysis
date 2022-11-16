import numpy as np


def Average_bout_length(rawdata,onset_point,hatching_point):
    output=[]
    for j in rawdata:
        bouts=[]
        current = (rawdata[onset_point[j]:hatching_point[j]])
        count=0
        for i in range(len(current)):
            if i==0:
                continue
            if current[i]!=0:
                count+=1
            elif current[i]==0:
                bouts.append(count)
                count=0
        output.append(np.mean(bouts))
    return output