# if는 여러 개의 elif(...: 0 more)와 하나의 else(?: 0 또는 1)를 선택적으로 가질 수 있다

def if_test01():    # 함수 안에 선언된 변수: 지역 변수
    score = int(input('input score: '))
    if 90 <= score <= 100:  # 90~100
        grade = 'A'
    elif 60 <= score < 70:  # 60~69
        grade = 'D'
    elif 80 <= score < 90:  # 80~89  elif는 범위연산자가 너무 길다. 이 함수는 순서가 바뀌어도 상관 없다.
        grade = 'B'
    elif 70 <= score < 80:  # 70~79
        grade = 'C'

    else:                   # 기타 등등
        grade = 'F'

    '''
    이런거는 딕트로 안된다 키값이 고정적이어야 하는데 10가지나 되니까
    그래서 터플로 진행한다. if_test03
    '''
    print(grade)

def if_test02():
    score = int(input('input score: '))
    if score>=90:
            grade = 'A'
    elif score<=89 and score>=80:
            grade = 'B'
    elif score<=79 and score>=70:
            grade = 'C'
    elif score<=69 and score>=60:
            grade = 'D'
    else:
            grade = 'F'
    print(grade)

def if_test03():    # 토플 형태 127p. 참고 삼항 연산자 적용
    score = int(input('input score: '))
    grade = (
        'A' if 90 <= score <= 100 else  # 원래는 코드가 한 줄인데 예쁘게 보이게 하려고 내림 127p. 참고
        'B' if 80 <= score < 90 else
        'C' if 70 <= score < 80 else
        'D' if 60 <= score < 70 else
        'F'
        # 'A' if 90 <= score <= 100 else 'B' if 80 <= score < 90 else 'C' if 70 <= score < 80 else 'D' if 60 <= score < 70 else 'F'
    )

def if_test04():
    score = int(input('input score: '))
    grade = (
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'D' if score >= 60 else
        'F'
    ) if 0 <= score <= 100 else 'Invalid score'
    print(grade)

if __name__ == '__main__':
    if_test04()

'''
삼항 연산자는 리턴하는 값이 변수에 들어가는 형태여야지만 쓸 수 있다.
하나의 이프는 여러개의 엘리프와 하나의 엘즈를 가질 수 있다.
이프 안에 조건은 정렬(order)가 아니다.
'''