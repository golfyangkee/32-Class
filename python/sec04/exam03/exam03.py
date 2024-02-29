class Account:
    def __init__(self,account,balance,interestRate):
        self.account=account
        self.balance=balance
        self.interestRate=interestRate

    def setAccount(self,account):
        self.account=account
    def getAccount(self):
        return self.account
    def getBalance(self):
        return self.balance

    def calculateInterest(self):
        return self.getBalance * self.interestRate  # self.balance*self.interestRate

    def deposit(self,money):
        self.balance += money   # self.getBalance()

    def withdraw(self,money):
        if self.balance >=money:
            self.balance -= money
        else:
            print("Insufficient funds")

if __name__ == '__main__':

    #계좌 클래스 테스트
    account = Account("441-0290-1203", 500000, 0.073)
    print("초기 계좌 정보:", account.getAccount(), "잔액:", account.getBalance())

    # 20,000원 입금
    account.deposit(20000)
    print("입금 후:", account.getAccount(), "잔액:", account.getBalance())

    #이자 계산 및 출력
    interest = account.calculateInterest()
    print("이자:", interest)