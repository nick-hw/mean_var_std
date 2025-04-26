import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError ("List must contain nine numbers.")
    data = np.array(list).reshape(3,3)
    #data = np.array([0,1,2,3,4,5,6,7,8]).reshape(3,3)
    mean_data = [data.mean(axis = 0).tolist(), data.mean(axis=1).tolist(), data.mean()]
    var_data = [data.var(axis = 0).tolist(), data.var(axis=1).tolist(), data.var()]
    std_data = [data.std(axis = 0).tolist(), data.std(axis=1).tolist(), data.std()]
    max_data = [data.max(axis = 0).tolist(), data.max(axis=1).tolist(), data.max()]
    min_data = [data.min(axis = 0).tolist(), data.min(axis=1).tolist(), data.min()]
    sum_data = [data.sum(axis = 0).tolist(), data.sum(axis=1).tolist(), data.sum()]

    calculations = {'mean':mean_data,
                    'variance':var_data,
                    'standard deviation':std_data,
                    'max':max_data,
                    'min':min_data,
                    'sum':sum_data}
    return calculations

calculate([0,1,2,3,4,5,6,7,8])
calculate([9,1,5,3,3,3,2,9,0])
data3 = np.array([0,1,2,3,4,5,6,7,8])
data3.tolist()



    # mean_data = [list(arr) for arr in mean_data1]
    # var_data = [list(arr) for arr in var_data1]
    # std_data = [list(arr) for arr in std_data1]
    # max_data = [list(arr) for arr in max_data1]
    # min_data = [list(arr) for arr in min_data1]
    # sum_data = [list(arr) for arr in sum_data1]