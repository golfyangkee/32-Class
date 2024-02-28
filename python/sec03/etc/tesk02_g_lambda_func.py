#-----------for문

#1)목록을 주면  요소**2 를 구한후  []로 리턴
def test01():
    numbers=[1,2,3,4,5]
    squared_numbers =[x**2  for  x in numbers]
    return squared_numbers

#2)문자열 목록을 대문자로 변환
def test02():
    strings = ["apple", "banana", "cherry"]
    uppercase_strings = [s.upper() for s in strings]
    return uppercase_strings

#3) 목록에서 짝수를 필터링 하자.
def test03():
    numbers = [1, 2, 3, 4, 5]
    filtered_numbers = [x for x in numbers if x % 2 != 0]
    return filtered_numbers

#4) 목록에서  하위 문자열 찾기
def test04():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    # 문자열 자체를 리턴하기 때문에  lambda s: s an포함 여부 상관없이 문자열만 리턴 된다.
    filtered_strings = [s for s in strings if substring in s]
    return filtered_strings

def test04_res():
    strings = ["apple", "banana", "cherry"]
    substring = "an"
    filtered_strings = [s for s in strings if substring in s]
    return filtered_strings

#5) 각 문자열에서 마지막 문자를 추출하자.
def test05():
    strings = ["apple", "banana", "cherry"]
    last_chars = [ s[-1] for s in strings]
    return last_chars

#6) 각 단어의 첫글wk를 대문자로 표시하기
def test06():
    str ="process finished with exit code"
    res_words = [w.capitalize() for w in str.split()]
    return res_words

if __name__ == '__main__':
    print(test01())
    print(test02())
    print(test03())
    print(test04())
    print(test04_res())
    print(test05())
    print(test06())