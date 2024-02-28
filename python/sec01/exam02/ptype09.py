u = '바나나 포도 수박'
t = u.split()   # 문자열 내의 단어 리스트
print( t)
print(type(t))

t2 = ':'.join(t)  # 리스트 t 내부의 각 원소들을 ':'로 연결한 문자열 반환
print (type(t2))
print (t2)

t3=':'.join(['ab','pq','rs'])
print(t3)
print(type(t3))

t4='.'.join(('cd','or','xy'))
print(t4)