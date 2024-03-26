import cv2

img_file = "../img/apple.jpg"
save_file = '../img/apple_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 로드
cv2.imshow('img_file', img)  # 회색이미지 결과를 보여줌
# cv2.imshow(img_file, img) -> 이렇게하면 img_file 이름창이 아닌 경로를 이름창으로 해서 보여줌

cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
# cvt로 해상도 조절해서 압축파일로 나가는 플래그
# 색상영역 컴버전 시켜주는 게 있다.
# apple_gray.jpg

cv2.waitKey()

#  apple.jpg   -> apple02.jpg     :  사과이미지를 읽어서  apple02.jpg로 저장
img = cv2.imread(img_file, 1)  #  -> Mat | ndarray[Any, dtype[generic]] | ndarray
# 1을 사용하여 원본대로 읽어들이라는 의미

cv2.imwrite("../img/apple02.jpg", img)

# 원본 용량 9.25, 새로 저장한 사진 용량 : 17.39 왜??
# apple_gray.jpg = 14.94
#  imread 함수를 사용하여 이미지를 읽을 때, 원본 이미지 파일이 압축되어 있을 수 있습니다.
#  예를 들어, JPEG 형식의 이미지는 손실 압축을 사용하여 파일 크기를 줄일 수 있습니다.
#  그러나 imread 함수는 압축된 이미지를 압축 해제하고 메모리에 로드하기 때문에 압축 형식의 차이로 인해 저장된 이미지의 용량이 달라질 수 있습니다.

print(img, type(img), type ( img_file ))


#cv2.destroyAllWindows()
