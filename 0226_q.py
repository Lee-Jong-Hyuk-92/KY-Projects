#Q1. 다음은 Calculator 클래스이다.
'''
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
#위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.
#즉 다음과 같이 동작하는 클래스를 만들어야 한다.
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value) #10에서 7을 뺀  3을 출력
'''

#@Q2. 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자
#단, 반드시 다음과 같은 Calculator클래스를 상속해서 만들어야한다.

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value+val>100:
            print('100 over')
        else:
            self.value+=val

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#GPT 1
#아래와 같은 클래스 Person을 생성하세요:
'''
# 클래스 속성: name, age
# 생성자: __init__(self, name, age): name과 age를 인자로 받아 객체를 초기화합니다.
# 메소드: greet(self): "{name}님이 {age}살입니다" 형식의 문자열을 반환합니다.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f'{self.name}님이 {self.age}살입니다')
p1 = Person('OPQWE', 15)
p1.greet()
'''

#GPT 2
#아래와 같은 클래스 BankAccount을 생성하세요:
'''
#클래스 속성: account_number, balance
# 생성자: __init__(self, account_number, balance=0): account_number와 초기 잔액 balance(기본값 0)을 인자로 받아 객체를 초기화합니다.
# 메소드: deposit(self, amount): 계좌에 amount만큼 입금합니다.
# 메소드: withdraw(self, amount): 계좌에서 amount만큼 출금합니다. 잔액이 출금액보다 작을 경우 “잔액이 부족합니다”라고 출력합니다.
# 예시 코드를 작성하고 테스트해보세요.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number=account_number
        self.balance=balance
        print(f'현재 계좌잔액은 {self.balance}입니다.')
    def deposit(self, amount):
        self.balance += amount
        print(f'현재 계좌잔액은 {self.balance}입니다.')
    def withdraw(self, amount):
        if self.balance-amount < 0:
            print('잔액이 부족합니다.')
            print(f'현재 계좌잔액은 {self.balance}입니다.')

account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다
'''
