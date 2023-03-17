def makeDict(K, V):
    D = dict(zip(K, V))
    return D


K = ('Korean', 'Math', 'English', 'Science', 'Java')
V = (90.3, 85.5, 92.7, 39.4, 99.4)
D = makeDict(K, V)
print(D)

for i in K:
    print("key = ", i)
    if i not in D.keys():
        print("key error!")
print("confirmed")




