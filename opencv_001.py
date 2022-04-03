    ###? 카메라 출력/파일 불러오기

import cv2
import numpy as np

print(cv2.__version__)  #파이썬 버전출력

PATH = "./image/n001.jpg"

img = cv2.imread(PATH)
cv2.imshow("test", img)
cv2.waitKey()
cv2.destroyAllWindows()