import numpy as np
def average_movement_magnitude(rawdata,onset_point,hatching_point):
    output = []
    for i in range(len(rawdata)):
        output.append(np.mean(rawdata[onset_point[i]:hatching_point[i]]))
    return output