import cv2

img = cv2.imread("BasicChessPieces.png", cv2.IMREAD_UNCHANGED)
print(img.shape)
for i in range(6):
    new_img = img[0:125, i * 134: (i+1)*132, 0:4]
    cv2.imwrite("%d.png"%i, new_img)