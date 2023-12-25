"""
@project:Bearing_Fault_Diagnosis
@Author: Phantom
@Time:2023/12/16 下午5:10
@Email: 2909981736@qq.com
"""

import h5py
import numpy as np

a = h5py.File('data/raw_Data/JNU/data/data_all.mat')

print(a.keys())
print(a.values())

for key in a.keys():
    mat_t = np.transpose(a[key])
    print(mat_t.shape)
    # print(mat_t)
