sentence= """
나는 사람이고,
파이썬은 쉬워요
"""

print(sentence)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0번째 포함, 2번째는 배제
print("월 : " + jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

pyt = "Python is Amazing"
print(pyt.lower())
print(pyt.upper())
print(pyt[0].isupper())
print(len(pyt))
print(pyt.replace("Python", "She"))

index = pyt.index("n")
print(index)
index = pyt.index("n", index + 1) #2번째 n 찾기
print(index)

질문 = "a" in "abc"
print(질문)

print(pyt.find("ㅁㅇ머ㅏ")) # -1이 나옴. 
#print(pyt.index("She")) 오류가 남.

print(pyt.count("n"))

# +는 문자열 붙여쓰기, 콤마는 띄어쓰기
print("나는 %d살입니다." % 20) #d는 정수
print("나는 %s을 좋아해요." % "파이썬") #s는 문자
print("Apple 은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." %("빨간", "파란"))

#2번째 방법
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))

age=20 #직접 변수 만들기
color= "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("난 나고\n넌 너야") #\n은 줄바꿈
print("저는 \"조민제\"입니다") #\\는 문장 내에서 \
#/r: 커서를 맨 앞으로 이동
print("blue moon\rfull")
#\b: backspace \t:탭
print("half\tmoon")

#리스트 []

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))
subway.append("하하")
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.count("유재석"))

num_list = [5,2,4,3,1]

num_list.reverse() #순서 거꾸로
print(num_list)
# 모두 지우기는 num_list.clear()

list1 = [3,2,1]
list2 = ["sk" ,"lg"]
list1.extend(list2) #리스트 통합
print(list1) 

weather= input()
if weather == "비" or weather =="눈":
    print("우산")
elif weather == "미세먼지":
    print("마스크")
else:
    print("아무것도 아님")

temp = int(input("기온은 어때요?"))
if 30<=temp:
    print("나가지 마")
elif 10<= temp <30:
    print("괜찮아요")
elif 0<= temp<10:
    print("외투를 챙기세요")
else:
    print("나가지 마")

