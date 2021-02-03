import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

import pafy
#import cv2

from skimage.metrics import structural_similarity as ssim

st.write("# Load image from local")
img = st.file_uploader(label="Upload image", accept_multiple_files=False)
if img:
	#st.image(img, width=600)

	fig,ax = plt.subplots()
	ax.imshow(Image.open(img))
	st.pyplot(fig)

#img_open = Image.open(img)
#st.write(type(img_open))

# Convert

'''
url = "https://www.youtube.com/watch?v=VvL5Q7YVyWM"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
cam = cv2.VideoCapture(best.url)

_,frame = cam.read()
cv2.imshow("image", frame)

#cam.release()
#cv2.destroyAllWindows()
'''