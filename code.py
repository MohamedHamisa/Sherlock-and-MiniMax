def sherlockAndMinimax(arr, p, q):
  
    arr.sort()
    maxInd = p
    minimum = float('inf')
    for ele in arr:                   #element
        if abs(ele-p)<minimum:
            minimum = abs(ele-p)
    maximum = minimum

    minimum = float('inf')    
    for i in range(1,len(arr)):
        mid = (arr[i]+arr[i-1])//2
        if p<mid<q:
            minimum = min(mid-arr[i-1],arr[i]-mid)
            if minimum>maximum:
                maximum = minimum
                maxInd = mid




 
