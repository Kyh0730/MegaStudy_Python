#반복문
#수십번, 수백번 반복 작업을 코드로 구현
#for 횟수로, while 조건으로
"""
형식
for i in range(시작값, 끝값+1, 증가값):
    실행문 작성(들여쓰기 필수)
"""

#반복문 안쓴거
print("for문 구현0")
print("for문 구현1")
print("for문 구현2")
print("for문 구현3")
print("for문 구현4")
print("for문 구현5")
print("for문 구현6")
print("for문 구현7")
print("for문 구현8")
print("for문 구현9")

#반복문 쓴거
for i in range(0, 10, 1):
    print("for문 구현 %d" % i)

#증가값이 -(음수)
for i in range(9, -1, -1):
    print("for문 구현 %d" % i)

#증가값이 없을 때
for i in range(0, 10):      #디폴트 => 1
    print("for문 구현 %d" % i)

##i값 연산 (횟수 => 연산에 사용)
i = 0
sum = 0

for i in range(1,11,1):     #1부터 10까지 증가
    sum = sum + i           #1부터 10까지의 합

print("1부터 10까지의 합: %d" % sum)

#문제) 123부터 543까지 짝수만 합 구하기
sum = 0
i = 0

for i in range(123, 544, 1):
    if (i%2) == 0:
        sum = i + sum

print("123부터 543까지 짝수만 합 : %d" % sum)

#시작값, 끝값, 증가값 입력받아 합 구하기
i, sum, num1, num2, num3 = 0,0,0,0,0

num1 = int(input("시작값 입력 : "))
num2 = int(input("끝값 입력 : "))
num3 = int(input("증가값 입력 : "))

for i in range(num1, num2+1, num3):
    sum = sum + i

print(sum)

#구구단 출력
#몇 단인지 입력받아 출력하기
i, dan = 0,0
dan = int(input("출력할 단 : "))

for i in range(1,10):
    print("%d * %d = %d" % (dan, i, dan*i))

##구구단 출력
#중첩 for문, 이중 for문

i, j = 0, 0

for i in range(2,10):
    print("==========%d단==========" % i)
    for j in range(1,10):
        print("%d * %d = %d" % (i, j, i*j))



#문제1) 주사위가 2개 => 모든 경우의 수 출력
dice1, dice2 = 0,0

for dice1 in range(1,7):
    for dice2 in range(1,7):
        print("(%d , %d)" % (dice1,dice2), end = " ")
    print()


#문제2) 구구단 출력 9x9 ~ 2x2 거꾸로 출력
num1, num2 = 0, 0

for num1 in range(9,1,-1):
    print("==========%d단==========" % num1)
    for num2 in range(9,0,-1):
        print("%d * %d = %d" % (num1,num2,num1*num2))

