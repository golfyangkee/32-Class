import cv2      #  설치된 cv2 모듈을  참조하겠다.

img_file = "../img/apple.jpg"
img = cv2.imread(img_file,cv2.IMREAD_REDUCED_COLOR_4) # 컬러로 읽어서 해당 속성의 숫자 크기로 리턴
# 이미지를 1/4 크기로 줄여서 로드할 때 사용

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows() # 문제가 keyboardInterrupt가 걸린다. 키로 제어하는 거니까 난 왜 안 걸림...?? ㅎㅎ
else:
    print('No image file.')
    