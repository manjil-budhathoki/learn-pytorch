import numpy as np # for numerical arrays
import torch # for deep learning operations and pytorch tensors.

scores = [
    [60,70,77],
    [90,80,70],
]

# convert python list to numpy array
np_score = np.array(scores, dtype=np.float32)
"""
types of dtypes:
    - int32: integer values
    - float32: floating point values
    - float64: double precision floating point values
"""
print(np_score)


# NumPy array to pytorch tensor
# torch_score = torch.from_numpy(np_score)
torch_score = torch.tensor(np_score)

print(torch_score)

# Properties of pytorch tensor
print(f"Shape: {torch_score.shape}") # size of the tensor
print(f"Data type: {torch_score.dtype}") # data type of the tensor
print(f"Total elements: {torch_score.numel()}") # total number of elements in the tensor
print(f"Dimensions: {torch_score.ndim}") # number of dimensions of the tensor

# accessing elements of the tensor
first_student_math = torch_score[0,0]

print(first_student_math)
print(first_student_math.item()) # convert tensor to python scalar


# add numerical operations to the tensor
bonus_score = torch_score + 5
print(bonus_score)

