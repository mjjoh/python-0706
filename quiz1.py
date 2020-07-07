url="http://naver.com"
my_str= url.replace("http://", "")
my_str= my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

#사전 dictionary
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[100]) #cabinet.get()을 쓰면 없더라도 none이 나오고 프로그램이 멈추지 않는다.
print(cabinet.get(4, "사용 가능")) #사용 가능 출력
cabinet[45] = "조민제"
print(cabinet)

del cabinet[45]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items()) # 키, 밸류 같이 출력
cabinet.clear() #초기화

#튜플 tuple
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") #불가능
(name, age, univ, hobby) = ("조민제", 20, "SNU", "coding")
print(name, age, univ, hobby)

#집합 set
# 원소 중복 불가능, 순서 없음
set1 = {1,2,3,3,3}
print(set1) #{1,2,3}

java = {"A", "B", "C"}
python = {"C", "D"}
print(java & python) #교집합 1
print( java.intersection(python)) #교집합 2
print(java | python) #합집합 1
print(java.union(python)) #합집합 2
print(java - python) #차집합 1
print(java. difference(python)) #차집합 2
python.add("E")
java.remove("A")
print(java | python)

#자료구조 바꾸기 
menu2 = {"d", "c", "b"}
print(menu2)
menu2 = list(menu2)
print(menu2, type(menu2))

from random import *
lst= range(1,21)
lst= list(lst)
shuffle(lst)
sample(lst, 1)

winners = sample(lst, 4)

print( " -- 당첨자 발표 -- ")
print("치킨 당첨자: {0}" . format(winners[0]))
print("커피 당첨자: {0}" . format(winners[1:]))



