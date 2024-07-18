def check(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            count+=1
    return count
arr=[1,36,8,24,6,12]
print(check(arr))
