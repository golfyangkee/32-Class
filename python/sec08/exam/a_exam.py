#apple.jpg을 읽어서 apple_copy.png로 저장을 해보자.

# 파일을 읽어서
print("============read=====")
with open("../apple.jpg",'rb') as f:
    res=f.read()

# 파일을 저장하자.
with open("apple_copy.png",'wb') as f:
    f.write(res)