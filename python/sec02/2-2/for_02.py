# for  List of numbers 1~10 's sum
# for ~ else : for 반복문의 수행이 끝나면 else구문이 실행된다.
# 1~10까지 나열된 값을 출력하고 합을 구하자
# 1+2+3+... +9+10 =55 출력하고 싶다. / 만일에 val이 10이면 =을 출력하자
# (1+2)*(3+4)...=? 해보자
# (1+2)/(3+4)...=? 해보자
numbers = [1,2,3,4,5,6,7,8,9,10]
m_sum = 0
for val in numbers:
    if val==10:
        print(val, end='=')
    else:
        print(val, end='+')
    m_sum = m_sum+val  # m_sum += val
else:
    print(m_sum)
