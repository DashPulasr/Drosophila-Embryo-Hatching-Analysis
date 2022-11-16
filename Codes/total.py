import numpy as np
def total_movement(rawdata,onset_point,hatching_point):
    return len(np.where(np.array(rawdata[onset_point:hatching_point])>=1)[0])