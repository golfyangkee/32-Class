import cv2
# cv::rectangle (InputOutputArray img, Point pt1, Point pt2, const Scalar &color, int thickness=1, int lineType=LINE_8, int shift=0)

img = cv2.imread('../img/bg.jpg')

# 좌상, 우하 좌표로 사각형 그리기, 선 두께는 default 1
cv2.rectangle(img, (50, 50), (150, 150), (255,0,0) )
cv2.rectangle(img, (200, 200), (300, 300), (0,255,0) )

# 좌상, 우하 좌표로 사각형 그리기, 선 두께는 default 10
cv2.rectangle(img, (300, 300), (350, 350), (255,0,255) , thickness=10)

# 사각형 채워서 그리기  thickness=-1
cv2.rectangle(img, (100, 400), (150, 450), (255,20,255) , thickness=-1 )

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()