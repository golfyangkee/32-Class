for n, m in enumerate(['abc', 'def', 'ghi']):
   print(n,m)    # index , value 를  출력 한다. 

for n, m in enumerate(['abc', 'def', 'ghi'], start=100):
   print(n,m)    # index , value 를  출력 한다.

'''
enumerate 내장 함수이다. 라벨링 할 때 사용한다.
   enumerate(iterable, start=0)
 
   Return an enumerate object.
   (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
   
   인덱스로 프린트 해줌
'''