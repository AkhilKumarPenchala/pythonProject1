def TwoSumII(ListN,target):

    l,r=0,len(ListN)-1

    while l<r:
        curSum = ListN[l]+ListN[r]
        if curSum > target:
            r-=1
        elif curSum < target:
            l+=1
        else:
            return [ListN[l],ListN[r]]



print(TwoSumII([1,3,4,5,7,10,11],9))



