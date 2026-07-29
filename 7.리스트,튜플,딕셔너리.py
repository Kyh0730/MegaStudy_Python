#리스트
#여러개의 변수를 하나로 묶어준것
#변수를 사용할 때와 비슷하다
#리스트 이름 짓는것도 변수랑 동일

#리스트 = [1,2,3,4,5]

#단순 변수 사용
a = int(input("1번째 숫자 입력 : "))
b = int(input("2번째 숫자 입력 : "))
c = int(input("3번째 숫자 입력 : "))
d = int(input("4번째 숫자 입력 : "))

sum = a + b + c + d
print(sum)

#리스트 사용
aa = [0,0,0,0]  #비어있는 리스트x, 0이 4개가 있는 리스트o

aa[0] = int(input("1번째 숫자 입력 : "))
aa[1] = int(input("2번째 숫자 입력 : "))
aa[2] = int(input("3번째 숫자 입력 : "))
aa[3] = int(input("4번째 숫자 입력 : "))

sum = aa[0] + aa[1] + aa[2] + aa[3]
print(sum)
print(aa)

#비어있는 리스트에 항목값 추가하기
#리스트명.append(항목값)

aa = []
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)

print(aa)

#for문이랑 조합해서 항목 100개짜리 리스트 만들기
a = []
for i in range(1,101):
    a.append(0)

print(a)
print(len(a))   #len() => 항목 갯수 또는 길이 출력

#리스트 항목 4개짜리 값 입력받아 합 구하기
aa = [0,0,0,0]
sum = 0

for i in range(0,4):
    aa[i] = int(input(str(i+1) +"번째 숫자를 입력하세요 : "))
    sum = sum + aa[i]

print(sum)

##append() 사용해서 4개짜리 리스트 항목값 더하기
aa = []
sum = 0
for i in range(0,4):
    aa.append(int(input(str(i+1) + "번째 숫자를 입력하세요 : ")))
    sum = sum + aa[i]
print(sum)
print(aa)

#문제) 항목 5개짜리 리스트
#ctrl + c 누르기 전까지 안꺼지는거
#몇 번째 숫자를 수정할 지 입력받아서

aa = []
for i in range(0, 5):
    aa.append(int(input(str(i + 1) + "번째 숫자를 입력하세요 : ")))

print(aa)

while True:
    change = int(input("수정할 숫자 번호를 입력하세요 : "))
    num = int(input("몇으로 수정? : "))
    aa[change] = num
    print(aa)
