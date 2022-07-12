#연습문제 2.1
def celsius2fahrenheit(c):
    return c*9/5+32
print(celsius2fahrenheit(19.4))
print(round(celsius2fahrenheit(19.4),1))

#연습문제 2.2 가
def monthly_payment_plan(principal, interest, year):
    return (1 + interest / 100 / 12) ** (year * 12) * principal * (interest / 100 / 12) / ((1 + interest / 100 / 12) ** (year * 12) -1)
print(int(monthly_payment_plan(10000000, 2.8, 4)))

#연습문제 2.2 나
principal = int(input("자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.\n대출 원금이 얼마인가요? (백만원 이상)"))
interest_year = float(input("연 이자율은 몇%인가요? (0.0~9.9)"))
year = int(input("상환기간은 몇 년인가요?"))
print("대출 상환금 내역을 알려드리겠습니다.\n 대출원금: ", principal ,"원\n 연 이자율", interest_year, "매월", int(monthly_payment_plan(principal,interest_year,year)),"원씩 지불하셔야 합니다.\n 상한 완료시까지 총 상환금액은 ", int(monthly_payment_plan(principal,interest_year,year))*year*12,"원입니다.\n" )
print("\n저희 자유은행은 항상 여러분과 함께 합니다\n또 들려주세요")