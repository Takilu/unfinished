import cv2
import matplotlib.pyplot as plt
from glob import glob
import IPython.display as ipd
ipd.Video('road.mp4', width=700)

cap = cv2.VideoCapture('road.mp4')
frames = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
ret, img = cap.read()
print(img.shape)
def display_cv2_img(img, figsize=(10,10)):
    img_ = cv2.cvtColor((img, cv2.COLOR_BGR2RGB))
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(img_)
    ax.axis("off")

fig, axs = plt.subplots(5,5, figsize =(30,30))
axs= axs.flatten()

img_idx=0
for frame in range(frames):
    ret, img = cap.read()
    if ret== False:
        break
    if frame %100==0:
        axs[img_idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[img_idx].set_title(f'frame: {frame}')
        axs[img_idx].axis('off')
        img_idx +=1
plt.tight_layout()
plt.show()
cap.release()
