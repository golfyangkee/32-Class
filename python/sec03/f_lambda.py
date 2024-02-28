#------- if문을 사용해서 lambda 연습
def lambda01():
    num=5
    res  =  lambda x: "Positive"  if x > 0 else "non -positive"
    print (res(num))

#------- if문을 사용해서 lambda 연습 :
#내가 입력한 문자열의 길이가 0 ,Empty  , Non-Empty
def lambda02():
    string =" "
    check_empty = lambda s: "Empty" if len(s) == 0 else "Non-empty"
    result = check_empty(string)
    print(result)
#------- if문을 사용해서 lambda 연습 :
#내가 입력한 숫자가  짝수이면  "Even", "Odd"
def lambda03():
    num = 7
    check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
    result = check_even_odd(num)
    print(result)
#------- if문을 사용해서 lambda 연습 :
#내가 입력한 list 객체의 요소가 없으면 ,Empty  , Non-Empty
def lambda04():
    my_list = []
    check_list_empty = lambda lst: "Empty" if len(lst) == 0 else "Non-empty"
    result = check_list_empty(my_list)
    print(result)

#------- if문을 사용해서 lambda 연습 :
#내가 입력한 숫자가 3의 배수와 5의 배수이면 Divisible , Not divisible
def lambda05():
    num = 15
    check_divisible = lambda x: "Divisible" if x % 3 == 0 and x % 5 == 0 else "Not divisible"
    result = check_divisible(num)
    print(result)

# ['a','e','i','o','u]  안에 내가 입력한 글자가 있으면   vowel  , consonant
def lambda06():
    char = "a"
    check_vowel = lambda c: "Vowel" if c.lower() in ['a', 'e', 'i', 'o', 'u'] else "Consonant"
    result = check_vowel(char)
    print(result)


if __name__ == '__main__':
    lambda06()



















