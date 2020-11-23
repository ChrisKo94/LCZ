import h5py
import numpy as np

path = "/data/"
# Read in training data & assign features & labels
data_train = h5py.File((path + 'training.h5'), 'r')
x_tra = np.array(data_train['sen2'])
y_tra = np.array(data_train['label'])

# Read in validation data & assign features & labels
data_test = h5py.File((path + 'validation.h5'), 'r')
x_test = np.array(data_test['sen2'])
y_test = np.array(data_test['label'])

print(x_tra[1])

