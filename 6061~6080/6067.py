#6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
n = input()
n = int(n)

if n<0 :
  if n%2==0 :
    print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')
...