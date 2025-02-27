'''
탭 문자를 공백 문자 4개로 바꾸기
다음과 같은 형식으로 프로그램이
수행되도록 만들 것이다.

python tabto4.py src dst

tabto4.py는 우리가 작성해야 할
파이썬 프로그램 이름,
src는 탭을 포함하고 있는 원본 파일 이름,
dst는 파일 안의 탭을
공백 4개로 변환한 결과를 저장할 파일 이름이다.

예를 들어 a.txt에 있는 탭을
4개의 공백으로 바꾸어 b.txt에
저장하고 싶다면 다음과 같이 수행해야 한다.

python tabto4.py a.txt b.txt
'''
text = "hello tab world"
new_text = text.replace("tab", "    ")#문자 바꿀때
print(new_text)

'''
다시풀기
'''