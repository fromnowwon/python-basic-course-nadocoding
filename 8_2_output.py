# 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 때는 플러스 표시, 음수일 때는 마이너스 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬을 하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 세 자리 마다 콤마
print("{0:,}".format(100000000000))
# 세 자리 마다 콤마와 +- 부호 찍기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

#세 자리 마다 콤마와 부호와 자릿수 확보, 빈자리는 ^ 표시
print("{0:^<+30,}".format(1000000000000))

# 소수점
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (소수점 셋째 자리에서 반올림)
print("{0:.2f}".format(5/3))