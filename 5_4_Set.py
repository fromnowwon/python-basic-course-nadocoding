# 집합 (Set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

java = {"유재석", "김태호", '양세형'}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

#	추가
python.add("김태호")
print(python)

# 삭제
java.remove("김태호")
print(java)

