#while 문은 for문 처럼 명령어를 반복할 때 사용한다.
#for - 횟수로 반복
#while - 조건식이 참일때까지 실행
"""
while 변수 < 끝값:
    들여쓰기 조심
    실행문 반복
"""

i = 0
while i < 10:
    print("반복문 실행중 %d" % i)
    #i = i + 1   #증가값 없으면 무한루프
    i += 1
#0~9까지 10번

#1~10까지의 합
i,sum = 1,0
while i < 11:
    sum += i
    i += 1
print("1부터 10까지의 합 : %d" % sum)

#문제) 1~100 짝수만 더한 값 구하기
i,sum = 1,0
while i < 101:
    if (i % 2) == 0:
        sum += i
    i += 1
print("1~100까지 짝수만 더한 값 구하기 : %d" % sum)

##시작값, 끝값, 증가값 입력받아 합 구하기
i, sum, num1, num2, num3 = 0,0,0,0,0

num1 = int(input("시작값 입력 : "))
num2 = int(input("끝값 입력 : "))
num3 = int(input("증가값 입력 : "))

i = num1
while i < num2:
    sum = sum + i
    i = i + num3
print("%d부터 %d까지의 합 : %d" % (num1, num2, sum))

#구구단 2단 출력
i = 1
while i < 10:
    print("2 X %d = %d" % (i,i*2))
    i = i + 1

#문제) 구구단 2~9단까지 출력
num1, num2 = 2, 1

while num1 < 10:
    print("==========%d단========" % num1)
    while num2 < 10:
        print("%d X %d = %d" % (num1, num2, num1 * num2))
        num2 = num2 + 1   # 안쪽 while 안으로!
    num2 = 1              # 다음 단을 위해 다시 1로 초기화
    num1 = num1 + 1

#문제) 구구단 홀수단만 출력
num1, num2 = 1, 1

while num1 < 10:
    if num1 % 2 != 0:
        print("==========%d단========" % num1)
        while num2 < 10:
            print("%d X %d = %d" % (num1, num2, num1 * num2))
            num2 = num2 + 1
        num2 = 1
    num1 = num1 + 1

#무한루프 돌리기 => 입출력 사용
#while이용해서 무한반복 이용
#사용자가 종료할 때 까지 프로그램이 종료되지 않게
#ctrl + c : 인터럽트(종료) => 코드에 녹이기

sum = 0
a, b = 0,0

while True:
    a = int(input("첫 번째 숫자를 입력하세요 : "))
    b = int(input("두 번째 숫자를 입력하세요 : "))
    sum = a + b
    print("a,b 더한값 : %d" % sum)

#문제) 사칙연산 계산기
num1,num2 = 0,0
while True:
    num1 = int(input("첫 번째 숫자 입력 : "))
    op = input("연산자 입력 (+,-,*,/)")
    num2 = int(input("두 번째 숫자 입력 : "))
    if op == "+":
        print("%d + %d = %d" % (num1, num2, num1 + num2))
    elif op == "-":
        print("%d - %d = %d" % (num1, num2, num1 - num2))
    elif op == "*":
        print("%d * %d = %d" % (num1, num2, num1 * num2))
    elif op == "/":
        print("%d / %d = %d" % (num1, num2, num1 / num2))
    else:
        print("연산자 잘못 입력")


#반복문 제어(break)
#반복문을 탈출할 때 사용
#ctrl + c -> 코드로 써서 멈춘다
#종료하고 싶은 곳에 break 쓰면 끝
#for, while 둘 사용 가능

i = 0
for i in range(1,100):
    print("for문을 %d번 실행함" % i)
    break

#첫번째 숫자에 0입력하면 종료
sum = 0
a,b = 0,0

while True:
    a = int(input("첫번째 숫자 입력 : "))
    if a == 0:
        break
    b = int(input("두번째 숫자 입력 : "))
    sum = a + b
    print("%d + %d = %d" % (a,b,sum))
print("0 눌러서 종료")

#1~100 합을 반복문으로 구현
#합이 1000을 넘어갈 때의 i값이 몇인지 확인

sum, i = 0,0

for i in range(1,101):
    sum = sum + i
    if sum >= 1000:
        break
print("1000넘어갈때 i값 : %d" % i)

#continue
#블록에 남은 부분 건너뛰고 반복문 처음으로 돌아감
#3의 배수를 제외한 1~100까지의 합 구하기

sum, i = 0,0

for i in range(1,101):
    if i % 3 == 0:
        continue
    sum = sum + i
    print(i)
print(sum)

#문제)369게임 // 3배의 배수가 아님
#1,2,짝,4,5,짝,~~, 31(짝),32(짝),33(짝짝)
#1~50까지 출력

i = 0
for i in range(1, 51):
    count = 0

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:   #1의자리를 10으로 나눴을 때 나머지가 3,6,9이면 짝
        count += 1

    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9: #10의자리를 10으로 나눴을 때 몫이 3,6,9이면 짝
        count += 1

    if count == 0:
        print(i,end=' ')
    elif count == 1:
        print('짝(%d)' % i,end=' ')
    else:
        print('짝짝(%d)' % i ,end=' ')

    if i == 25:
        print()
