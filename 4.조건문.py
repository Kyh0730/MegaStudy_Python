#조건이 참일 경우에 다음줄에 실행할 명령을 입력한다
#들여쓰기!!!! 조심하기!!!! 실행문은 들여쓰기로 인식함!!!!!

a = 100

#조건문 작성 (조건문이 참 => 실행)
if a < 100:                         #조건문 작성 (조건문이 참 => 실행)
    print("참값, 100보다 작음")       #실행문 작성
    print("실행문 2개 이상 사용가능")
else:                               #조건이 아닐때
    print("거짓값, 100보다 큼")
    print("실행문 2개 이상 사용가능")


print("실행문 끝")


##홀짝 맞추기
a = int(input("숫자를 입력하세요 : "))
if a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


#문제) 숫자 입력받기
#50 업&다운 출력하기
num = int(input("숫자를 입력하세요:"))
if num > 50:
    print("50 초과입니다.")
elif num < 50:
    print("50 미만입니다.")
else:
    print("50 입니다.")


##학점 계산기
score = int(input("학점을 입력하세요 : "))

if score >= 90 :
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")


#elif 구문 => 조건이 여러개 일 때
score = int(input("학점을 입력하세요 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#문제) 숫자 3개 입력받으세요
#3개의 숫자 중에 가장 큰 숫자를 출력해주세요

a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))
c = int(input("세 번째 숫자 입력 : "))

if a>b and a>c:
    print("가장 큰 숫자는",a)
elif b>c:
    print("가장 큰 숫자는",b)
else:
    print("가장 큰 숫자는",c)


#사칙연산 계산기 ver3
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
op = input("연산자를 입력하세요(+,-,*,/) : ")
num2 = int(input("두 번째 숫자를 입력하세요 : "))

if op == "+":
    print("%d + %d = %d 입니다" % (num1,num2,num1+num2))
elif op == "-":
    print("%d - %d = %d 입니다" % (num1, num2, num1 - num2))
elif op == "*":
    print("%d * %d = %d 입니다" % (num1, num2, num1 * num2))
elif op == "/":
    if num1<num2:
        print("뒤 숫자가 더 큽니다")
    num2 = int(input("두 번째 숫자를 다시 입력하세요 : "))
    print("%d / %d = %d 입니다" % (num1, num2, num1 / num2))
else:
    print("연산자를 잘못 입력했습니다.")


#문제) "/" 연산할 때 => 뒤 숫자가 더 큽니다.


#문제) 과목점수 5개 입력받기
#4과목중 1개 과목이라도 40점 미만이면 과락 => 탈락입니다
#4과목 평균 점수가 60점 이상이면 합격입니다.
#4과목 평균 점수가 60점 미만이면 탈락입니다

score1 = int(input("첫 번째 과목의 점수를 입력하세요 : "))
score2 = int(input("두 번째 과목의 점수를 입력하세요 : "))
score3 = int(input("세 번째 과목의 점수를 입력하세요 : "))
score4 = int(input("네 번째 과목의 점수를 입력하세요 : "))
average = (score1+score2+score3+score4) / 4

if (score1 < 40) or (score2 < 40) or (score3 < 40) or (score4 < 40):
    print("과락(탈락)입니다. ")
elif average >= 60:
    print("합격입니다.")
else:
    print("탈락입니다.")




