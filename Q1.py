#Mississippi (program1)
print("Enter String")

def fun(s):
    return -1*cnt[s]

s = input()

cnt = {}



for x in s:
    if x in cnt:
        cnt[x]+=1
    else:
        cnt[x] = 1

l = list(cnt)
l = sorted(l , key = fun)

for x in l:
    print(str(x) + "=" + str(cnt[x]))






