# ============ for, list_for, zip exam 활용
def exam01():
    name = ['홍길동', '홍길동1', '홍길동2', '홍길동3', '홍길동4']
    age = [21,22,23,24,25]
    # 홍길동님의 나이는 00입니다.
    for name, age in zip(name,age):
        print(f'{name}님의 나이는 {age}입니다.')

def exam02():
    # 학생이름, 성적리스트, 주전공분야 -> {}로 묶어서 -> listfor로 구현하자 [{}]for, zip => 출력을 하자 for
    name = ['홍길동', '홍길동1', '홍길동2', '홍길동3', '홍길동4']
    score = [91, 82, 23, 24, 25]
    major = ['국어', '수학', '영어', '역사', '항공']

    # 2. [{} for, zip] : zip을 사용해서 세개의 리스트를 하나로 묶고, for을 사용해서 사전리스트를 생성한다.
    students_info = [{'Name': n, 'Score': s, 'Major': m} for n, s, m in zip(name,score,major)]

    # 2-1 score가 50점 이상인 친구들만 출력

    # 3. for로 출력
    for student in students_info:
        print(student)

def exam03():
    name = ['홍길동', '홍길동1', '홍길동2', '홍길동3', '홍길동4']
    age = [21,22,23,24,25]
    # 홍길동님의 나이는 00입니다. for, zip
    res = [f'{name}님의 나이는 {age} 입니다' for name, age in zip (name,age)]
    print(res)

def exam04():
    gugudan= [f'{i}*{x}= {i*x}'  for i in range(2,10,2) for x in range(2,9,2)]
    print(gugudan)

if __name__ == '__main__':
    exam04()