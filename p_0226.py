'''
class BlackBox: #클래스 명은 대문자로
    pass #아무의미 없음, 넘어가라

b1 = BlackBox() #객체 생성, b1 블랙박스의 객체 변수, 유저들의 동작이나 요청 동작 가능, 이렇게 하지 않으면 유저수만큼 만들어야 한다
b1.name = '까망이'
b1.price=200000
print(b1.name)

b2 = BlackBox()
print(b2.name) #AttributeError: 'BlackBox' object has no attribute 'name' b2.name 을 정하지 않고 프린트 하라 하니까 없다고 오류
'''
'''
#  __init__ 다른 개념에서 아예 없는 개념!!!!!!!! 언더바 2개씩, 초기화 함수
class BlackBox:
    def __init__(self, name, price): #자동으로 호출?, 객체를 만들때 그냥 알아서 작동, 객체생성시 init함수 자동으로, #self는 b1, self가 없으면 누가 호출하는지 알수 없다(ID)
        self.name = name #멤버변수
        self.price = price #멤버변수
# 더블언더바(더블언더스코어) 함수는 특정 조건(객체생성시)을 만족하면 자동으로 호출됨

b1 = BlackBox('까망이', 200000) # 클래스일경우 self는 전달하지 않고 그다음부터 차례대로 전달, 객체생성
print(b1.name, b1.price)

b2 = BlackBox('하양이', 100000)
print(b2.name)
'''
''' #파이썬은 self를 통해서 쉽게 처리되었다라고 하심
class BlackBox: # 객체 생성하면 클래스 안의 모든 함수 사용 가능
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_travel_mode(self, min): #기능구현
        print(f'{min}분 동안 여행 모드 On')

b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(10)#self는 전달 안해도 되니까 다른 전달값 없어도 된다
'''
'''
#상속
class BlackBox: #부모 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TravelBlackBox(BlackBox):     #자식 클래스, 부모 클래스를 상속받으면서 def __init__함수 부분이 똑같이 있는것처럼 작동
    #def __init__(self, name, price):
    #    self.name = name
    #    self.price = price
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON')

b1 = TravelBlackBox('까망이', 200000)
b1.set_travel_mode(5)
print(b1.name, b1.price)
'''
'''
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd): #부모 클래스로부터 상속받았는데 전달값을 추가하고 싶을때
        super().__init__(name, price) #58,59라인이 이거 한줄로 바뀌었다, 여기에는 self 전달값이 없다, 부모클래스 호출
        self.sd = sd
    def set_travel_mode(self, min):
        print(f'{min} + 분 동안 여행 모드 ON')

b2 = TravelBlackBox('하양이', 200000, 128) #디버깅 찍어보면서 순서 확인해보기!!!!!
'''
'''
#다중상속
class VideoMaker:
    def make(self):
        print('추억용 여행 영상제작')
class MailSender:
    def send(self):
        print('메일 발송')
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TravelBlackBox(BlackBox, VideoMaker, MailSender):#다중상속
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(f'{min} + 분 동안 여행 모드 ON')

b2 = TravelBlackBox('하양이', 200000, 128)
b2.make()
b2.send()
'''
'''
#메소드 오버라이딩, 이 기능이 없으면 충돌
class VideoMaker:
    def make(self):
        print('추억용 여행 영상제작')
class MailSender:
    def send(self):
        print('메일 발송')
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(f'{min} + 분 동안 여행 모드 ON')
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):     #상속을 받았는데 TravelBlackBox의 set_travel_mode와 똑같다, 여기가 만약에 없다면 116라인에서 호출되는 함수는 108라인이 실행
        print(f'{self.name} {min}분 동안 여행 모드 ON')
        self.make()
        self.send()
b2 = AdvancedTravelBlackBox('초록이', 120000, 64)
b2.set_travel_mode(15) #같은 이름의 함수가 두군데에 있는데 이럴때는 자식클래스에서 선언한 함수가 우선, 이게 메소드 오버라이딩
'''
'''
#pass 나중에 할게, 일단은 내버려둬
#예외처리
num1 =3
num2 = 0
num3 = '0'
try:    #에러 발생 가능성이 있는 수행문장
    result = num1 / num3
    print(f'연산 결과는 {result}입니다')
except TypeError:
    print('값의 형태가 이상해요')
except ZeroDivisionError:   #에러 발생시 수행문장
    print('0으로 나눌수 없어요.')
except Exception as err:
    print('에러 발생')
    print('에러명 :', err)
except:
    print('에러가 발생했어요')
else:   #정상 작동시 수행문장
    print('정상 동작했어요')
finally:    #마지막으로 수행할 문장
    print('수행 종료')
'''
#모듈, 함수의 집합, 기능들을 모아놓은것, 용도별로 모아놓은것
