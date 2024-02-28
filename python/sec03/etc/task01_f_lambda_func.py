#------- if문을 사용해서 lambda 연습
def test01():
    num=5
    if num > 0:
        return "positive"
    else:
        return "Non-positive"


#------- if문을 사용해서 lambda 연습 :
#내가 입력한 문자열의 길이가 0 ,Empty  , Non-Empty
def test02():
    string =" "
    if len(string) == 0:
        return "Empty"
    else:
        return "Non-empty"

#------- if문을 사용해서 lambda 연습 :
#내가 입력한 숫자가  짝수이면  "Even", "Odd"
def test03():
    num = 7
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#------- if문을 사용해서 lambda 연습 :
#내가 입력한 list 객체의 요소가 없으면 ,Empty  , Non-Empty
def test04():
    my_list = []
    if len(my_list) == 0:
        return "Empty"
    else:
        return "None-empty"

#------- if문을 사용해서 lambda 연습 :
#내가 입력한 숫자가 3의 배수와 5의 배수이면 Divisible , Not divisible
def test05():
    num = 15
    if num % 3==0 and num % 5 == 0:
        return "Divisible"
    else:
        "Not divisible"


# ['a','e','i','o','u]  안에 내가 입력한 글자가 있으면   vowel  , consonant
def test06():
    char = "a"
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    else:
        return "Consonant"

if __name__ == '__main__':
    print(test01())
    print(test02())
    print(test03())
    print(test04())
    print(test05())
    print(test06())