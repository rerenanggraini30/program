import cv2
imgrgb =cv2.imread("pagi.jpeg")
imggray =cv2.imread("pagi.jpeg",0)
cv2.imshow ("Gambar RGB",imgrgb)

cv2.imshow ("Gambar gray",imggray)
cv2.waitKey()
