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
    change = int(input("수정할 숫자 번호를 입력하세요(0~5) : "))
    num = int(input("몇으로 수정? : "))
    aa[change] = num
    print(aa)


#리스트의 생성과 초기화
aa = []
bb = [1,2,3]                #리스트에 정수 사용
cc = ['파이썬', "공부중"]     #문자,문자열 가능
dd = [10,20," 파이썬"]       #데이터형식 혼용 가능

#리스트 생성 후 첨자(자리값)을 통해 접근
#자리값을 의미하는 첨자는 양수, 음수 사용가능
#양수 => 왼쪽부터 0~10
#음수 => 오른쪽부터 -1 ~ -10

aa = [10,20,30,40,50]
print(aa[0])
print(aa[1])
print(aa[-1])
print(aa[-2])


#자리값 범위 지정
#[시작값:끝값+1]

aa = [10,20,30,40,50]
print(aa[0:3])
print(aa[:3])       #시작값 안쓰면 디폴트 첫번째부터

print(aa[1:3])
print(aa[1:])       #끝값도 동일

#문제) for,while 1~100까지 3의 배수만 출력
#리스트 1 => 3,6,9,~
#리스트 2 => 99,96,~~~

#for문
num = []
for i in range(1,101):
    if i % 3 == 0:
        num.append(i)
print(num)

num = []
for i in range(100,-1,-1):
    if i % 3 == 0:
        num.append(i)
print(num)

#while 문
num = []
i = 0
while i<100:
    if i % 3 == 0:
        num.append(i)
    i += 1
print(num)

num = []
i = 100
while i>1:
    if i % 3 == 0:
        num.append(i)
    i -= 1
print(num)


#리스트 연산
aa = ["정","보","보","안"]
bb = ["취","약","점"]
print(aa + bb)
print(aa * 3)

#리스트 안에 항목 값 바꾸기
aa = ["정","보","보","안"]
aa[2] = "가"
print(aa)


aa[:2] = "취","약"
print(aa)

##리스트 안에 리스트
aa = [10,20,30,40,50]
aa[1] = [15,25,35]
print(aa)


#리스트 안에 항목값 삭제
del(aa[3])
print(aa)

del(aa[1])
print(aa)

del(aa[0:3])
print(aa)


#### 리스트에서 사용하는 함수 ####
list = [40,20,10,30]
print(list)

list.append(50)
print(list)
#append => 추가

list.pop()
print(list)
#가장 오른쪽 항목 삭제

list.sort()     #정렬
print(list)
#주의 - 원본데이터에 영향을 미침

list.reverse()
print(list)
#순서 거꾸로 쓰기
#주의 - 원본데이터에 영향을 미침

print(list.index(20))
#항목의 자리값 출력

list.insert(2,222)
print(list)
#지정위치(index)에 값(object)을 삽입하고 나머지 오른쪽으로 밈

list.remove(222)
print(list)
#항목값 검색해서 삭제

list.extend([55,555,52,55,55])
print(list)
#리스트를 확장, 이어쓰기 느낌
list = [40,20,10,30,55,55,55]
print(list.count(55))
#항목값 리스트에 몇 개인지 확인

print(len(list))
#리스트 길이확인


#문제) 리스트 항목 10개
#입력1) index 자리 검색
#입력2) insert 항목 입력
#입력3) count할 항목값 입력

aa = [1,2,3,4,5,6,7,8,9,10]
while True:
    print(aa)
    b = input("index,insert,count 선택")
    if b == "index":
        b_input = int(input("자리값을 검색할 항목 선택(1~10) : "))
        print(b_input,"번째 항목의 자리값은 ",aa.index(ba))
    elif b == "insert":
        b_index = int(input("지정할 위치 : "))
        b_OB = int(input("넣을 값 : "))
        aa.insert(b_index,b_OB)
        print(aa)
    elif b == "count":
        b_count = int(input("count할 항목값 입력 : "))
        print(b_count,"의 갯수는 ",aa.count(da))
    else:
        break

##튜플
#리스트 = []
#튜플 = ()
#읽기전용 리스트
#튜플의 항목값을 수정하기 힘들어 읽기 전용으로 쓴다
#성별 =(남성, 여성) 서울시 구목록 = (서초구, 강남구,,,)

tt = (10,20,30)
print(tt)

tt.append(40)
#튜플은수정이 안되서 append함수 에러발생

tt2 = 10,20,30
print(tt2)
#변수에 항목을 여러개 넣으면 자동으로 튜플 생성

tt3 = (10,)
print(tt3)
#항목 하나짜리 튜플 만들기

tt4 = (10,20,30)
print(tt4[1])
print(tt4[0]+tt4[1]+tt4[2])
#데이터 수정 말고는 리스트 사용하는법과 비슷하다

tt5 = (10,20,30,40,50)
#튜플 => 리스트 => 데이터 수정 => 튜플

list_5 = list(tt5)      #튜플 => 리스트
print(list_5)

list_5.append(55)       #데이터 수정
print(list_5)

tt5 = tuple(list_5)     #리스트 => 튜플
print(tt5)

#문제) 고객정보 튜플 만들기
customer1 = (
    ['회원번호','이름','성별','전화번호'],
)
num = 0
#회원가입, 정보수정, 삭제
#회원번호자리 4자리 확보 후 자동으로 1씩 증가
#무한반복
while True:
    op = int((input("회원가입(1),정보수정(2),삭제(3) 선택 : ")))
    if op == 1:
        c_name = input("이름입력 : ")
        c_gender = input("성별입력 : ")
        c_phone = input("번호입력: ")
        new_customer = list(customer1)
        num = num + 1
        member_num = "%04d" % num
        new_customer.append([member_num,c_name,c_gender,c_phone])
        customer1 = tuple(new_customer)
    elif op == 2:
        fix_customer = list(customer1)

        fix_num = input("수정할 회원번호: ")
        fix_customer1 = int(input("수정할 정보 선택 (1)이름 (2)성별 (3)전화번호 : "))

        for i in range(1, len(fix_customer)):
            if fix_customer[i][0] == fix_num:
                if fix_customer1 == 1:
                    fix_customer[i][1] = input("수정할 이름 : ")
                elif fix_customer1 == 2:
                    fix_customer[i][2] = input("수정할 성별 : ")
                elif fix_customer1 == 3:
                    fix_customer[i][3] = input("수정할 전화번호 : ")
                print("수정완료")
                break
        customer1 = tuple(fix_customer)
    else:
        del_mem = input("삭제할 회원번호 입력 : ")
        del_customer = list(customer1)

        for i in range(1, len(del_customer)):
            if del_customer[i][0] == del_mem:
                del del_customer[i]
                print("삭제 완료")
                break

        customer1 = tuple(del_customer)
    for i in range(1, len(customer1)):
        print("[회원번호:", customer1[i][0],
              "이름:", customer1[i][1],
              "성별:", customer1[i][2],
              "전화번호:", customer1[i][3], "]")



##딕셔너리
#딕셔너리, 사전
#딕셔너리 = {키1:값1, 키2:값2}
dic = {1:'a',2:'b',3:'c'}
print(dic[1])

student1 = {"학번":1001, "이름":"김영한", "학과":"컴공"}
print(student1)

student1["학번"] = "1002"
print(student1)
#키값으로 항목 값에 접근해 수정

student1["연락처"] = "0102131231"
print(student1)
#append() 사용 안해도 추가 가능

del(student1["학번"])
print(student1)
#del 함수로 키:값 삭제 가능

##딕셔너리에서 사용하는 함수
student1.get("이름")      #키가 갖고있는 항목값 출력
print(student1['이름'])

student1.get('주소')      #키값 없을때 get함수 쓰면 null값 출력
print(student1['주소'])   #print하면 에러

print(student1.keys())          #딕셔너리가 가지고 있는 모든 키 출력
print(list(student1.keys()))    #출력할 때 dict_keys 제거하고 출력(리스트로 출력)

print(student1.values())        #딕셔너리가 가지고 있는 모든 항목값 출력
print(list(student1.values()))  #출력할 때 dict_values 제거하고 출력(리스트로 출력)

print(student1.items())

print('이름' in student1)     #키값 기준으로 검색한게 있으면 True, 없으면 False 출력