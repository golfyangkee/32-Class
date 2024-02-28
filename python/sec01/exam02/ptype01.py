#슬라이싱
#객체[start: end-1 : step ]
mystring = "hello world!" #str

print(mystring[0])
print(mystring[1])
print(mystring[2])
print(mystring[-1])
print(mystring[11])

print("mystring's count = "+str(len(mystring))) # +가 연결문자로 형변환 해줘야 한다.
print(f"mystring's count = {len(mystring)}") # f"" 를 쓰면 된다. 포맷더스트링

a=100
b=200
print(f"{a}\t\t\t{b}")
print(a)
print('a')
print(a+b)