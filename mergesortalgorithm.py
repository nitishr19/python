# Merge sort is a sorting technique based on divide and conquer technique.
# With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.
# Merge sort first divides the array into equal halves and then combines them in a sorted manner.

def mergesort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        print(left_half)
        print(right_half)
        mergesort(left_half)
        mergesort(right_half)

        i=0
        k=0
        j=0
        print("i,j,k=",i,j,k)
        while (i< len(left_half) and j < len(right_half)):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]# greater goes right
                print("alist=",alist[k])
                i = i + 1
                print("i=",i)
            else:
                alist[k] = right_half[j]#smaller comes left
                print("alist=",alist[k])
                j = j + 1
                print("j=",j)
            k = k + 1
            print("k=",k)
# when left side is greater
        while i < len(left_half):
            print("llf",len(left_half))
            alist[k] = left_half[i]# move the greatest value to left
            print("alist[k]=",alist[k])
            i = i + 1
            print("i left=",i)
            k = k + 1
            print("k left=",k)
# when right side is greater
        while j < len(right_half):
            print("lrf",len(right_half))
            alist[k] = right_half[j]#
            print("alist[k]=",alist[k])
            j = j + 1
            print("j right=", j)
            k = k + 1
            print("k right=", k)
        print("Merging ", alist)


alist = [4,9,2,6,5,1,3]
(mergesort(alist))
print(alist)