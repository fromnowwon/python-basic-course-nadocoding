# 표준 입출력
print("파이썬", "자바", sep=",")
print("파이썬", "자바", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("파이썬", "자바", file=sys.stdout)
print("파이썬", "자바", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(5), sep=":")
    
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))
    
answer = input("아무 값이나 입력하세요: ")
print("입력 값은 " + answer)