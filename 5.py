n = int(input())
data = [int(input()) for _ in range(n)]


res = {}
for elem in set(data):
    index = data.index(elem)
    size = sum(data[:index + 1])  # including self
    for bigger in data[index + 1:]:  # not including
        if size > bigger:
            size += bigger
        else:
            res[elem] = 0
            break
    else:
        res[elem] = 1

for i in data:
    print(res[i])
