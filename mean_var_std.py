import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    x = np.array(lst).reshape(3,3)

    result = {
        'mean': [
            x.mean(axis=0).tolist(),
            x.mean(axis=1).tolist(),
            x.mean().item()
        ],
        'variance': [
            x.var(axis=0).tolist(),
            x.var(axis=1).tolist(),
            x.var().item()
        ],
        'standard deviation' : [
            x.std(axis=0).tolist(),
            x.std(axis=1).tolist(),
            x.std().item()
        ],
        'max': [
            x.max(axis=0).tolist(),
            x.max(axis=1).tolist(),
            x.max().item()
        ],
        'min': [
            x.min(axis=0).tolist(),
            x.min(axis=1).tolist(),
            x.min().item()
        ],
        'sum': [
            x.sum(axis=0).tolist(),
            x.sum(axis=1).tolist(),
            x.sum().item()
        ]
    }
    return result


