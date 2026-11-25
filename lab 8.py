s1 = "ATCCGTAC"
s2 = "CGAT"
g = -2

n, m = len(s1), len(s2)
a = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    a[i][0] = i * g
for j in range(m + 1):
    a[0][j] = j * g

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s = 2 if s1[i - 1] == s2[j - 1] else -1
        a[i][j] = max(a[i - 1][j - 1] + s, a[i - 1][j] + g, a[i][j - 1] + g)

for row in a:
    print(row)

r1, r2 = "", ""
i, j = n, m
path = [(i, j)]
while i > 0 or j > 0:
    if i > 0 and j > 0 and a[i][j] == a[i - 1][j - 1] + (2 if s1[i - 1] == s2[j - 1] else -1):
        r1, r2 = s1[i - 1] + r1, s2[j - 1] + r2
        i, j = i - 1, j - 1
    elif i > 0 and a[i][j] == a[i - 1][j] + g:
        r1, r2 = s1[i - 1] + r1, "-" + r2
        i -= 1
    else:
        r1, r2 = "-" + r1, s2[j - 1] + r2
        j -= 1
    path.append((i, j))

print("Traceback:", path)
print(r1)
print(r2)
print("Score:", a[n][m])
