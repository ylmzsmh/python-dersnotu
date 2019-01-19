#!/usr/bin/python
# -*- coding:UTF-8 -*-

import cv2
image = cv2.imread("opencv.jpg")
cv2.imshow("orjinal resim ",image)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("değiştirilmiş resim ",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()