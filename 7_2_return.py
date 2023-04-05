# 전달값과 반환값
def open_account():
    print("계좌가 생성되었습니다.")
    
def deposit(balance, money):
    print("입금되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
	if balance >= money:
			print("출금되었습니다. 잔액은 {0}원입니다.".format(balance - money))
			return balance - money
	else:
			print("출금 실패. 잔액은 {0}원입니다.".format(balance))
			return balance
	
def withdraw_night(balance, money):
	commission = 100
	return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
