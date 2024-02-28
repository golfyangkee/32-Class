'''
강남에서 c#을 강의하고 있는데 요새는 면접보러 가면 나 C#할 줄 알아요 하는데 요즘은 ns사 에서는 C#으로
웹서비스를 할 줄 알아야 해 단내?를 한다. 란다라고 하는 것이 적용되었는데 람다는 익명형 함수야 한번쓰고 버리겠다.
이런 의미인데 이런걸 축약해서 만드는 건데 앞으로 람다가 파이썬에 많이 나오는데
이름 없는 함수, 한번만 쓰고 버리는 게 람다인데
연식이되면서 자바가 버전업을 하면서 1.8에 람다를 넣고
파이썬은 크게 윈도우 제외한 프로그램 os들은 기본적으로 파이썬이 설치가 된다.
파이썬 2버전하고 3버전이 크게 나뉘는데
2버전은 기존 시스템이 업데이트가 끝났고
파이썬 사에서 이제 2버전 업데이트 안 하겠다 함
아직까지 임베딩 시스템에서는 2버전을 쓰고 있는 곳도 있다.
3버전에 오면서 크게 바뀐거는 내부적으로 문법이 많이 바뀜
프린트 열고 닫기 , 람다 도입
2011년에 3.21버전을 썼으니까 람다를 엄청 많이 쓰고 있는데
자바를 람다를 할 수 있는 개발자
파이썬도 람다를 할 수 있는 프로그램 아닌 프로그램이 나뉜다.
3.8 버전부터 함축코드를 굉장히 많이 개발하고 있다.
파이썬은 코드를 늘리는 프로그램이 아니고 줄이는 거다.
시퀀스로 하고 싶고 람다로 하고 싶고 이런 구문을 만듦
'''
'''
  list  객체를  for문을 활용해서 연산결과를 list로 리턴 
  형식
  [ 리턴값  for  변수,, in list객체 ]   -> return 키워드가 없다. 
  List Comprehension 
  [ 표현식  for  항목,, in iterable if 조건 ]   -> return 키워드가 없다. 
  for문 모두를 list 형태로 적을 수 있어야 한다.
  '''

list1  =[1,2,3,4,5]

print( '1. 요소*요소 =>',[  x*x  for x in list1    ])
#반복 구문에서 조건에 트루인 애들만 리턴
# for x in list1이 1번
# x*x를 리스트 객체어 담아둔다. 모아둔다. 리턴이 되어서 전체 객체가 [] 리스트이다.
# list1[0] 이 x로 가고 리턴을 해서 [] 안에 모아둠
#len(list1) = 5니까 [] 안에도 5개가 남음
# [1,4,9,16,25]

print( '2.(요소, 요소*요소) =>',[(x, x*x)  for x in list1    ])
#[(1,1), (2,4), (3,9), (4,16), (5,25)]

print( '3. 요소*요소   짝수=>',[  x*x  for x in list1  if x % 2 == 0    ])
#[4,16]

print( '4. 요소*요소 =>',[  x*x  for x in range(1,6)    ])
#[1,4,9,16,25]

my_word  = ['apple','watermelon','peach','pear'] 
print( '5. 문자열을 대문자로 변환  =>',[  word.upper()  for word in my_word   ])
#[APPLE, WATERMELON, PEACH, PEAR]

# 3행*3열
# 왜 count=개수 집계는 이렇게 쓰고 sum=누적합 hap= 산술합는 이렇게 쓰고
# 상수는? 같은거는 i,j,k,l,m,n 이렇게 쓸까?
# 포트란 언어는 int나 float가 없어서 전부 다 변수가 정수형 변수이고 for문은 반복할 때 쓰는 정수로 하고 있다.
# 그 당시 사용하고 있는 시스템에서 사용하고 있는 변수를 지금까지 계속 쓰고 있어서 그렇다.

#n_list[0] = [1,2,3]
#n_list[1] = [4,5,6]
#n_list[2] = [7,8,9]
#len(n_list) = 3  / len(n_list[0]) = 3
n_list= [[1,2,3 ],[4,5,6],[7,8,9]]

# sublist  [1,2,3 ][4,5,6][7,8,9]
res_list  =  [ num for sublist in n_list  for num in sublist]
print('6. 중첩 연산  :' ,res_list)

# [ 표현식  for  항목,, in iterable if 조건 ] 1번 for  항목,, in iterable if 조건 / 2번 표현식
numbers = range(1,11)
print( '7. 1~ 10까지  even, odd  =>',['even' if x % 2 == 0 else 'odd' for x in numbers])
# 1번 문법 for x in numbers /
# 2번 표현식 'even' if x % 2 == 0 else 'odd' if를 삼항연산자로 만든거 p.127 첫문장
# for를 기점으로 문법과 표현식이 나뉜다.

numbers = [1, 2, 7, 4, 5]
all_positive = all(x > 0 for x in numbers)  # data and data and None and....
print('8번 : ',all_positive )
'''
help(all)
 Return True if bool(x) is True for all values x in the iterable.
    If the iterable is empty, return True.
'''

is_even_res  = any( num % 2==0 for num in  numbers  )
print ('9번',is_even_res )
'''
help(any)
Return True if bool(x) is True for any x in the iterable.
    If the iterable is empty, return False.
'''

