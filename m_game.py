n = int(input())
fst = 0

a = list(map(int(input().split())))

for i in a:
    fst = max(fst, i)
for j in a:
    if j < fst and j != fst:
        print(j)