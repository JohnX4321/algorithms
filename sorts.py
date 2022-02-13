// insertion sort o(n) / o(n2)
def insertionsort(a):
    n=len(a)
    for j in range(2,n):
    key=a[j]
    i=j-1
    while i>0 and a[i]>key:
        a[i+1]=a[i]
        i-=1
    a[i+1]=key

//merge sort o(nlogn)
def mergesort(a=[],p,q,r):
    n1=q-p+1
    n2=r-q
    l,r=[],[]
    for i in range(1,n1):
        l[i]=a[p+i-1]
    for i in range(1,n2):
        r[i]=a[q+j]
    l[n1+1]=1/0
    r[n2+1]=1/0
    i,j=1,1
    for k in range(p,r):
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1

//bubble sort o(n2)
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n,i+1,-1):
            if a[j]<a[j-1]:
                tmp=a[j]
                a[j]=a[j-1]
                a[j-1]=tmp


//heapsort o(nlogn)
def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def maxheapify(a,i):
    l=left(i)
    r=right(i)
    if l<=len(a) and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<=len(a) and a[r]>a[largest]:
        largest=r
    if largest!=i:
        tmp=a[i]
        a[i]=a[largest]
        a[largest]=tmp
        maxheapify(a.largest)

def buildmaxheap(a):
    a.size=len(a)
    for i in range(len(a)/2,1,-1):
        maxheapify(a,i)

def heapsort(a):
    for i in range(len(a),2,-1):
        tmp=a[1]
        a[1]=a[i]
        a[i]=tmp
        a.heapsize-=1
        maxheapify(a,1)
//quicksort o(nlogn) / o(n2)

//counting sort o(k+n)

//radix sort o(d(n+k))

//bucket sort o(n) / o(n2)
