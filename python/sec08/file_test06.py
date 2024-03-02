try:
    import cPickle  # 임포트 cPickle
    pickle = cPickle #pickle로 대입한다, 대입시 cPickle이 없다면 프로그램은 중단이 되기 때문에 except로 이동
except:
    import pickle  #임포트 pickle

class Address:
    def __init__(self, name, addr,tel):
        self.name = name
        self.addr = addr
        self.tel = tel
    def Prn(self):  # 임의 출력 사용자 메소드
        print("%10s%10s%15s\n"%(self.name,self.addr,self.tel))

    def __repr__(self) -> str:  # 재정의 메소드
        return f'{self.name:^10s}:{self.addr:<10s} {self.tel:>10s}'


if __name__ == '__main__':
    no01= Address("홍길동","서울","02-000-000")
    with open("address.pkl",'wb') as f: # wb - dump 이고 rb - load 암기하세요
        pickle.dump(no01,f)
    with  open("address.pkl",'rb')  as f:
       res =pickle.load(f)
       print(res)   #__repr__ 호출
       res.Prn()    #Prn 호출
