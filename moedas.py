import numpy as np
import scipy.ndimage
from PIL import Image
from skimage import filters
from skimage import feature
import cv2

a = Image.open('./imagens_moedas/WhatsApp Image 2026-06-05 at 20.43.01.jpeg').convert('L')
a = np.array(a)

gray = cv2.GaussianBlur(a, (9,9), 2)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.3,
    minDist=20,
    param1=100,
    param2=30,
    minRadius=20,
    maxRadius=50
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    print("Moedas:", len(circles[0]))

    for c in circles[0]:
        x,y,r = c
        cv2.circle(gray,(x,y),r,(0,255,0),2)


cv2.imwrite("Resultado1.png", gray)
cv2.waitKey(0)

b = Image.open('./imagens_moedas/WhatsApp Image 2026-06-05 at 20.42.54.jpeg').convert('L')
b = np.array(b)

grayb = cv2.GaussianBlur(b, (9,9), 2)

circles = cv2.HoughCircles(
    grayb,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=15,
    param1=100,
    param2=30,
    minRadius=20,
    maxRadius=50
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    print("Moedas:", len(circles[0]))

    for c in circles[0]:
        x,y,r = c
        cv2.circle(grayb,(x,y),r,(0,255,0),2)


cv2.imwrite("Resultado2.png", grayb)
cv2.waitKey(0)

c = Image.open('./imagens_moedas/WhatsApp Image 2026-06-05 at 20.42.54.jpeg').convert('L')
c = np.array(b)

elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (40,13))
chapeu_preto = cv2.morphologyEx(c, cv2.MORPH_BLACKHAT, elemento_estruturante)
cv2.imwrite("Resultado3.png", chapeu_preto)
cv2.waitKey(0)

#clear_border Scikit image