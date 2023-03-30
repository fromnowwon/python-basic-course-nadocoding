# 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])

print(cabinet.get(3))

# print(cabinet[5])

print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)