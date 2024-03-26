import cv2  as cv

# 이미지 호출
img_file = "../img/apple.jpg "

# 이미지 회색조로 읽어오기
'''
img = cv.imread(img_file, 0)
# color VER으로 읽어오기 (-1)
# cv.IMREAD_GRAYSCALE (0): 회색조 -1로 시작해서 for 문으로 가지고 올 생각하지 말기
# r_img 리턴받아 그레이로 불러온 거를 컬러로 변형 해보자.
r_img=cv.cvtColor(img,cv.COLOR_GRAY2RGB) # imshow로 보면 안 바뀐다. | 포매터 변경됨

h, w = img.shape
r_h, r_w, r_ch = r_img.shape  # 높이, 너비, 채널
print(h,w) # 270 223 그레이랑 채널이 없다.
print(r_h,r_w,r_ch) # 270 223 3 채널이 있다. 색깔이 있다.
# 이미지는 보여지는 게 다가 아니다.
'''


# 이미지 원본 그대로(칼라로) 읽어오기

img = cv.imread(img_file, -1)
# imread 뒤에 읽어드리는 것을 상수값을 매겨서 가지고 오는데 0 1 2 순이 아니라 -1 부터 시작한다. 4 6 8 이런식으로 넘어간다. for문 사용 X
# 컬러

ir_img=cv.imread(img_file,0)
# # cv.IMREAD_GRAYSCALE

r_img=cv.cvtColor(ir_img, cv.COLOR_GRAY2RGB ) # 포매터 변경됨

rg_img=cv.cvtColor(img, cv.COLOR_RGB2GRAY ) # 포매터 변경됨

h, w, ch = img.shape
ir_h, ir_w = ir_img.shape
r_h, r_w, r_ch = r_img.shape # 높이, 너비, 채널
rg_h, rg_w = rg_img.shape


print(h,w, ch) # 270 223 3 채널이 있다. 색깔이 있다.
print(ir_h,ir_w) # 270 223 그레이라 채널이 없다.
print(r_h,r_w, r_ch) # 그레이를 RGB로 변환했기에 3 채널 생김
print(rg_h,rg_w)

# 이미지 출력
if img is not None:
  cv.imshow('MyImg', img) # 이미지 보기 MyImg는 창의 이름이다.
  cv.imshow('Mycvt', r_img)
  cv.imshow('Myir', ir_img)
  cv.imshow('Myrg', rg_img)
  cv.waitKey() # 아무 키나 받을때 까지 대기해라
  cv.destroyAllWindows() # 모든 보여주는 리소스 해제(소멸)
else:
    print('No image file.')
    