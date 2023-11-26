import cv2

img = cv2.imread('outputX.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edges=cv2.Canny(gray,100,200)
resized = cv2.resize(edges, (1000, 600))
cv2.imshow('edges', resized)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
resized = cv2.resize(closed, (1000, 600))
cv2.imshow("Closed", resized)
cv2.waitKey(0)
i=0
cnts,heir= cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
	x,y,w,h=cv2.boundingRect(c)
	i=i+1
	newImage=img[y:y+h,x:x+w]
	cv2.imwrite(str(i)+'.jpg',newImage)

resized = cv2.resize(img, (1000, 600))
cv2.imshow('dst_rt', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
