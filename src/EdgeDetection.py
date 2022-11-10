import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/cat.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# Trying to find best value for threshold in Canny:
med_val = np.median(img)
lower = int(max(0, 0.7 * med_val))
upper = int(min(255, 1.3 * med_val))
edges = cv2.Canny(image=img, threshold1=lower, threshold2=upper)
plt.imshow(edges)
plt.show()

# sometimes in order to not picking up minor edges, it's better to blur the image
blurred_img = cv2.blur(img, ksize=(2, 2))
edges = cv2.Canny(image=blurred_img, threshold1=lower, threshold2=upper)
plt.imshow(edges)
plt.show()

# sometimes you'll get the perfect result just by using normal threshold
edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
plt.imshow(edges)
plt.show()
