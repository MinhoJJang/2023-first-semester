def makeDict(K, V):
    D = dict(zip(K, V))
    return D


K = ('Korean', 'Math', 'English')
V = (90.3, 85.5, 92.7)
D = makeDict(K, V)

for i in K:
    print("key = ", i)
    if i not in D.keys():
        print("error!")
print("confirmed")


