def threeSum(List):
    res = []
    List.sort()
    for i, a in enumerate(List):
        if i>0 and a== List[i-1]:
            continue
        l,r=i+1,len(List)-1
        while l<r:
            threesum = a+List[l]+List[r]
            if threesum > 0:
                r-=1
            elif threesum < 0:
                l+=1
            else:
                res.append([a,List[l],List[r]])
                l+=1
                while List[l]== List[l-1] and l<r:
                    l+=1
    return res




print(threeSum([-3,3,4,-3,1,2]))

