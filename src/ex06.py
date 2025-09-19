kol = int(input())
k1 = 0
k2 = 0
for _ in range(kol):
    data = input().split()
    if data[3] == "True":
        k1 += 1
    else:
        k2 += 1
print(k1, k2)
