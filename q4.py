# 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고
# 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
# python memo.py -a "Life is too short"

#원하는 메모 파일에 저장
with open('simple_memo.txt', 'w', encoding='utf-8') as f:
    f.write(input('저장하고싶은 내용을 입력하세요'))
#추가 기능?
#조회기능?

'''
다시풀기
'''