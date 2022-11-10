import cv2
import matplotlib.pyplot as plt

full_img = cv2.imread('../data/dog.jpg')
full_img = cv2.cvtColor(full_img, cv2.COLOR_BGR2RGB)
plt.imshow(full_img)
plt.show()

face = cv2.imread('../DATA/dog_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
plt.imshow(face)
plt.show()

# Template Matching Methods
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',
           'cv2.TM_SQDIFF_NORMED']

height, width, channels = face.shape

for m in methods:

    full_img_copy = full_img.copy()

    method = eval(m)
    res = cv2.matchTemplate(full_img_copy, face, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(full_img_copy, top_left, bottom_right, 255, 10)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('Template Matching Result')

    plt.subplot(122)
    plt.imshow(full_img_copy)
    plt.title('Detected Point')
    plt.suptitle(m)

    plt.show()
