import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def window_fft(rawdata,onset_point,hatching_point):
    sns.set()
    output=[]
    for j in range(24):
        current = (rawdata[onset_point[j]:hatching_point[j]])
        split_trace=np.split(current,10)
        each_trace=[]
        for i in split_trace:
            each_trace.append(np.mean(i))
        output.append(each_trace)
    ax=sns.heatmap(output)
    plt.show()