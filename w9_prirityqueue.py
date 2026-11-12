import heapq

def triage_order(priorities):
    heap=[]
    for i,x in enumerate(priorities):
        heapq.heappush(heap,(x,i))
    out=[]
    while heap:
        _,pid=heapq.heappop(heap)
        out.append(pid)
    return out

print(triage_order([3, 1, 4, 1, 5]))