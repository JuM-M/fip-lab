from collections import deque
def window_max(nums, k):
    dq=deque()
    result=[]
    for i,x in enumerate(nums):
        if dq and dq[0]<=i-k:
            dq.popleft()
        while dq and nums[dq[-1]]<=x:
            dq.pop()
        dq.append(i)
        if i>=k-1:
            result.append(nums[dq[0]])
    return result

print(window_max([4, 2, 2, 5, 1, 3, 6, 0, 6, 2], 3)) 
