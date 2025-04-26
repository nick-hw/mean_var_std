import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError ("List must contain nine numbers.")
    data = np.array(list).reshape(3,3)
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
