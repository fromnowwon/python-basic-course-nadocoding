# 리스트

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

subway.pop()
print(subway)

subway.append("유재석")
print(subway)

# 갯수
print(subway.count("유재석"))

# 정렬
num_list = [4, 5, 6, 1, 4]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

# 값 지우기
num_list.clear()
print(num_list)

# 리스트 확장
num_list = [4, 5, 6, 1, 4]
mix_list = ["조세호", 3, True]
num_list.extend(mix_list)
print(num_list)