def merge (arr,p,q,r):
    n1 = q-p+1
    n2 = r-q

    left = [0]*(n1)
    right = [0]*(n2)

    i=0
    j=0

    while i < n1:
        left[i] = arr[p+i] 
        i+=1
    while j < n2:
        right[j] = arr[q+1+j]
        j+=1
    left.append(float("inf"))
    right.append(float("inf"))

    i=0
    j=0
    k=p

    while k <= r :
        if (left[i] <= right[j] and i < n1) or j < n2:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    
def merge_sort (arr,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

    


