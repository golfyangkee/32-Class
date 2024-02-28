#range(start,end-1,step)
list1 = list(range( 100)) # 0 ~ 99 까지의 값을 나열 한 값을 저장한다. 가지고만 있다.
print(list1) # print(list1, end = "\n\n\n")
print()
print(list1[ 2]) # 2를 리턴 한다
print()
print(list1[ 12:48 ]) # 12 ~ 47까지 리턴 한다
print()
print(list1[ 12:48:2]) # 12, 14, 16, 18, ~ , 44, 46
print(list1[ 12:48:5]) # 12, 17, 22, 27, 32, 37, 42, 47
