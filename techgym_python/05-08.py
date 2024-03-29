#**************************************************************************
#05-08
#**************************************************************************
from google.colab import files

uploaded_file = files.upload()
uploaded_file_name = next(iter(uploaded_file))

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(uploaded_file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

scale = 0.1
img = cv2.resize(img, None, fx=scale, fy=scale)

plt.imshow(img)