from  collections import defaultdict

def case01():
      artist  =['아이유','조성진',   '비틀즈', 'abc']
      music =[ '가을아침','베토벤5번', 'imagine', None]
      res  = defaultdict(list) # 기본 dict를 만들고  키 , 밸류로 생성된 것을 추가해서 출력 해보자 .
      #dict로 생성
      for i, k in enumerate(artist):
          res[k].append(music[i])
      for i in res.values():
          print(i)
      pass

def case02():
    counter  = defaultdict(int)
    print(counter)
    my_list  =  [1,2,3,4,0.5]
    for num in  my_list:
        counter[num] +=1.5
    for num, count  in counter.items():
        print(f' {num} : {count}' )

if __name__ == '__main__':
    case02()