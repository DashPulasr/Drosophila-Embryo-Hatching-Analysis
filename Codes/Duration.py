def Duration_hatching(rawdata,onset_point,hatching_point):
    output=[]
    for i in range(len(rawdata)):
        output.append(len(rawdata[onset_point[i]:hatching_point[i]]))
    return output