#**************************************************************************
#05-07
#**************************************************************************
import numpy as np

friends = np.array([['1','2','3'],['1','2','3']])
print(friends)
for i,friend in enumerate(friends):
    print(f" {i+1} 人目 {friend}")