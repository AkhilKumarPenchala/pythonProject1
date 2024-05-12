def SumofTwointegers(ListN,target):
    prevMap = {}
    for i, n in enumerate(ListN):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i



print(SumofTwointegers([1,3,4,5,7,11],9))



