# Exercise 1 - Create a tensor

import numpy as np
import torch

measurements = [
    [1.2, 1.5],
    [0.9, 1.1],
    [1.7, 1.8]
]

# convert to numpy array
np_measurements = np.array(measurements, dtype=np.float32)

# convert to pytorch tensor
torch_measurements = torch.tensor(np_measurements)

print(f"No. of Dimensions: {torch_measurements.ndim}")
print(f"Total elements: {torch_measurements.numel()}")
print(f"Second Tensors: {torch_measurements[1]}")

"""
Exercise 2 - Think before coding
"""
x = torch.tensor([
    [2, 4],
    [6, 8]
])

print(x.shape)
print(x.ndim)
print(x.numel())
print(x[1, 0].item())