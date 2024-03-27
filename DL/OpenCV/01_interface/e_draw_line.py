import cv2

img = cv2.imread('../img/bg.jpg')

cv2.line(img, (50, 50), (150, 50), (255,0,0))   # 파란색 1픽셀 선
cv2.line(img, (200, 50), (300, 50), (0,255,0))   # 초록색 1픽셀 선
cv2.line(img, (350, 50), (450, 50), (0,0,255))   # 빨간색 1픽셀 선


# 하늘색(파랑+초록) 10픽셀 선
cv2.line(img, (100, 100), (400, 100), (255,255,0), 10)
# 핑크 (파랑 + 빨강) 10 픽셀선
cv2.line(img, (100, 150), (400, 150), (255,0,255), 10)
# 노랑이 (그린 + 빨강) 10 픽셀선
cv2.line(img, (100, 200), (400, 200), (0,255,255), 10)
# 회색 (파랑 + 그린 + 빨강) 10 픽셀선
cv2.line(img, (100, 250), (400, 250), (100,100,100), 10)

# cv::line (InputOutputArray img, Point pt1, Point pt2, const Scalar &color, int thickness=1, int lineType=LINE_8, int shift=0)
# int lineType=LINE_8 연결선인데 끝처리 우둘투둘한 정도를 나타냄

# 4 연결선
cv2.line(img, (100, 300), (400, 350), (0,0,255), 30, cv2.LINE_4)

# 8 연결선
cv2.line(img, (100, 350), (400, 400), (255,0,255), 30, cv2.LINE_8)

# AA 연결선
cv2.line(img, (100, 400), (400, 450), (255,255,0), 30, cv2.LINE_AA)

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()