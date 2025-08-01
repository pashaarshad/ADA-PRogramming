import itertools
def ctd(path,c):
    td=0
    for i in range(len(path)-1):
        c1=path[i]
        c2=path[i+1]
        td+=c[c1][c2]
    td += c[path[-1]][path[0]]
    return td
def tsb(c):
    nc=len(c)
    allc = set(range(nc))
    sd=float('inf')
    for path in itertools.permutations(allc):
        d=ctd(path,c)
        if d<sd:
            sd=d
            sp=path
    return sp,sd

if __name__=="__main__":
    c=[
        [0,29,20,21],
        [29,0,15,17],
        [20,150,0,28],
        [21,17,28,0]
    ]

    sp,sd=tsb(c)
    print("Shortest TSP Path",sp)
    print("Shortest TSP distance : ",sd)


