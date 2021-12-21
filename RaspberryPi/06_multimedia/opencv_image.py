import cv2

img = cv2.imread('photo1.jpg')
img2 = cv2.resize(img, (800, 1000))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('photo1', img)
cv2.imshow('photo2', img2)
cv2.imshow('PHOTO_GRAY', gray)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('GRAY_PHOTO.jpg', gray)

cv2.destroyAllWindows()