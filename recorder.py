import numpy as np
from PIL import ImageGrab
import cv2

fourcc = cv2.VideoWriter_fourcc(*"X264")
size = (ImageGrab.grab()).size
output = cv2.VideoWriter("output.mp4",fourcc,5.0,size)
while True:

    img = np.array(ImageGrab.grab())

    cv2.imshow("Screen",img)
    output.write(img)
    if cv2.waitKey(1) == 27 :
        break


output.release()
cv2.destroyAllWindows()