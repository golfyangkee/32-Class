# 재귀함수(팩토리얼 계산, 피보나치 수열), 하노이탑 중요★ 송도에 있는 SQL LG CNS 회사가 문제가 나왔는데 못 풀어서 마카 주고 풀어보라고 했는데 비전공자의 시험은 재귀함수를 꼭 물어본다.
# 수학 기호 읽는 거를 벽에 붙어선 읽어보기
# 수열: 일반항, 유한, 무한, 수열의 종류 (나열된 원소의 정렬), 등차수열, 등비수열, 피보나치 수열
# 수열: 숫자나 기호의 나열이며 일정한 규칙이나 패턴에 따라 정렬되어 있는 것

def factorial(n):
    print(f'---------{n}')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 피보나치 수열 : 이전 두 숫자의 합이 현재 숫자가 되는 수열
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    # print(factorial(5))
    res=fibonacci(10)
    print("피보나이츠 수열의 10번째 값 : ", res)