class MyValue:  #클래스 변수와 인스턴스 변수에 각각 +1을 한 결과를 비교

    shard_value=0   #클래스 변수

    def __init__(self, value):
        self.value = value

    def add_shard_value(self):
        MyValue.shard_value +=1
    def view(self):
        print(f'instance value : {self.value}, shard_value = {MyValue.shard_value}')

if __name__ == '__main__':
    obj1= MyValue(10)
    obj2= MyValue(20)

    obj1.add_shard_value() #클래스 변수값이 증가
    obj1.add_shard_value()  # 클래스 변수값이 증가

    obj1.view() #instance value : 10, shard_value = 1
    obj2.view() #instance value : 20, shard_value = 1 (클래스 변수는 모든 인스턴스에 1로 공유된다.)