
def for_test01():
	for res in [1,2,3,4]:
		print(f'{res}', end=' ')
def for_test02():
	for res in (1,2,3,4):
		print(f'{res}', end=' ')
def for_test03():
	print(range(10), list(range(10)), list(range(0,100,2)))	# range 개념은 0~9까지 풀어 넣는게 아니고 가지고 있다 라는 의미
	for x in range(10):
		print(f'{x}', end=' ')
	print('\n')
	print(range(10))

def for_test05():	# 100 포함입니다.
	# 0~100까지 정수, 5의 배수만 출력하고 싶다. range(), for 사용해서 출력해보자
	for x in range(0,101,5):
		print(f'{x}', end=' ')
	print('\n=====================================')
	# 100~0까지 정수를 역순으로 출력하고 싶다. range(), for 사용해서 출력해보자
	for x in range(100,-1,-1):
		print(f'{x}', end=' ')
	'''
	res = range(100,-1,-1)
	for x in res:
		print(f'{x}', end=' ')
	'''
def for_test04():
	fruit  = ['apple','watermelon','peach','pear']

	# in 연산자는 data or data or... or None 이런 뜻이다. 내부적으로 or로 비교필터링한다. 있는 지 없는지 확인한다.
	# 10 in [1,2,3,4,10] 뒤에 객체 []는 시퀀스 형태여야 하고 터플, 리스트, 레인지, str 같은 형태여야 한다.
	# for 이하는 True 구문 else는 False 구문
	print(len(fruit))

	if "apple" in fruit or len(fruit) > 5 :

		for m_f in fruit:

			print(m_f)

if __name__ == '__main__':
    for_test05()

'''
TabError: inconsistent use of tabs and spaces in indentation

탭 에러 : 공백과 탭을 겹쳐서 쓰거나 할 때 나오는 에러 메세지

continue는 시작부분으로 이동
break는 for문 내부 블록을 빠져나옴

range(start,stop-1,step)

중첩 for or 중첩 제어문을 굉장히 많이 해서
제어문 자체가 cross로 중첩을 많이 가져서
for문은 굉장히 숙달되어야 한다.

'''

'''
sum= 0
for i in range(1,11):
	sum += i
sum = sum + i
1	= 0 + 1
3	= 1 + 2
6	= 3 + 3
10 	= 6 + 4
...
'''
