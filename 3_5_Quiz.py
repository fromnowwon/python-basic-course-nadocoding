from random import *

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이낼 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외

# 출력문 예제: 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

date = str(randint(4, 28));

print("오프라인 스터디 모임 날짜는 매월 " + date + "일로 선정되었습니다.");