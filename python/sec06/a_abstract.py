#추상클래스  : abc.py  / dataclasses.py /  collections.abc
from abc import abstractmethod, ABCMeta
'''
★★★★★ 암기
 ******추상메소드를 가진 클래스는 추상클래스가 되고 객체 생성 불가능 // 다른 프로그램과 다른 점   *******
 (Can't instantiate abstract class AA without an implementation for abstract method 'prn')
  1)선조가 가진 추상메소드를 후손이 재정의하지 않으면 객체를 생성할 수 없다
  2)재 정의하지 않는 후손은 추상클래스를 된다.  
  
  Tip: 추상클래스란? 다형성과 동적 바인딩(다양한 형태의 기능(성질을 가지고 있는)을 가진 후손클래스들을 추상 메소드로 통일하는 구조)
        - 추상클래스 객체 생성 불가, 후손이 추상메소드 반드시 재정의, 재정의하지 않으면 후손은 추상클래스가 된다.
        - 객체 생성이란 생성자를 통해 객체 생성을 해서 내가 만든 자료형을 동적메모리에 올려 놓고 내가 사용하겠어. 이 클래스를 사용한다.
 1) 만들어 놓고 통일
 2) 쓰다보니 만들어야 겠다.
'''
#추상클래스  모든 클래스는 선조클래스가 Object 이고 init으로 객체 생성 기능실행
class Base(metaclass=ABCMeta) : # 난 객체 생성 안하는 추상클래스 . 단, 후손에게 강제로 추상메소드를 재정의 시킨다.

    #추상화 @을 함수위 에 지정할 수 있다.
    @abstractmethod   #추상메소드
    def start(self):
       pass
    @abstractmethod
    def stop(self):
        pass

class Cat(Base) :
    def start(self):
        print('Cat  start')
    def stop(self):
        print('Cat stop')
class Duck(Base) :
    def start(self):
        print('Duck  start')
    def stop(self):
        print('Duck stop')
class Puppy(Base):
    def start(self):
        print('Puppy  start')
    def stop(self):
        print('Pyppy stop')

def my_class(m:Base):        # 정적바인딩타입 명시
    # :base라고 안 해도 되긴 한다 왜냐면 base만 받으니까 정적바인딩으로 만드는 느낌?
     m.start()
     m.stop()
def my_class(r):        # 동적바인딩타입 명시
    r.start()
    r.stop()
'''
마이클래스 입장에서는 어떻게 데이터를 받냐면
추상클래스는 객체는 생성할 수 없어도 주소는 받을 수 있다.
나는 베이스라는 클래스를 m이라고 하고 Cat()라는 주소를 받겠다.
Cat는 base와 cat 주소가 있다.

베이스의 m은 마이클래스 호출할 때 Duck를 넘겼으면 duck 도 base duck 클래스 및 주소가 있다,
base의 m 하게 되면 puppy도 base주소와 puppy 주소가 있다.
= 연산자는 같은 주소를 참조하겠다는 의미이다.

cat한테 base 있는 주소가 있다
베이스는 자기 자신은 객체 생성이 어려우니 후손을 통해서 메모리에 로드(올릴 수 있다.)
더 설명해주심
'''
if __name__ == '__main__':
    my_class(Cat())     # Base를 가지고 있는 Cat
    my_class(Duck())    # Base를 가지고 있는 Duck
    my_class(Puppy())   # Base를 가지고 있는 Puppy
    #my_class(Base())   # 에러남 base()가 객체 생성 불가 추상클래스는 객체 생성 불가












