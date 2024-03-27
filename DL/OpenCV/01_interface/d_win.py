import cv2
import numpy as np

file_path = '../img/apple.jpg'
img = cv2.imread(file_path)                            # 이미지를 기본 값으로 읽어서 ndarray (배열)  로 리턴    : BGR
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) # 이미지를 그레이 스케일로 읽기  = 회색조
print(img)

cv2.namedWindow('origin')                               # origin 이름으로 창 생성 - 크기 조절 X
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)              # gray 이름으로 창 생성 - 크기 조절 가능
# 이 플래그는 생성된 창이 사용자가 크기를 조정할 수 있도록 합니다.
cv2.imshow('origin', img)                               # origin 창에 이미지 표시
cv2.imshow('gray', img_gray)                            # gray 창에 이미지 표시

cv2.moveWindow('origin', 100, 100)                          # 창 위치 변경
cv2.moveWindow('gray', 200, 200)                        # 창 위치 변경

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.resizeWindow('origin', 200, 200)                    # 창 크기 변경 (창만 크기 변경, 이미지는 변경 안됨)
cv2.resizeWindow('gray', 400, 400)                      # 창 크기 변경 (창이랑 이미지도 같이 변경 됨))

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.destroyWindow("gray")                               # gray 창 닫기

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.destroyAllWindows()                                 # 모든 창 닫기
