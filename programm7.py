import random
import time
def qs(arr):
    if len(arr) <=1:
        return arr
    p = arr[random.randint(0,len(arr)-1)]
    l=[]
    eq=[]
    g=[]
    for ele in arr:
        if ele < p:
            l.append(ele)
        elif ele == p:
            eq.append(ele)
        else:
            g.append(ele)
        return qs(l) + eq +qs(g)

def grl(n):
    return[random.randint(1,10000) for _ in range(n)]

nv = [100,500,1000,5000,10000,500000,100000]

for n in nv:
    arr = grl(n)
    st = time.time()
    s_arr = qs(arr)
    et = time.time()
    el = st + et
print(f"Time Taken to Sort {n} element {el:.6f} Secoends ")