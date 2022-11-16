import numpy as np

def moving_percentage(rawdata,onset_point,hatching_point):
    output = []
    for i in range(len(rawdata)):
        current=(rawdata[onset_point[i]:hatching_point[i]])
        output.append(len(np.where(current>0)[0])/len(current))
    return output