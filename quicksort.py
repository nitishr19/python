#Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
# It picks an element as pivot and partitions the given array around the picked pivot.
# There are many different versions of quickSort that pick pivot in different ways.
#Mathematical analysis of quicksort shows that,
#  on average, the algorithm takes O(n log n) comparisons to sort n items. In the worst case, it makes O(n2) comparisons
# performance depends on pivot selection here the the 1st value is selected as pivot
def quick_sort(alist):
    if len(alist)<2:
        #print("only 1 element in list:",alist)
        return alist
    else:
        pivot = alist[0]
        print("Current pivot is: ",pivot)
        del(alist[0])

        left_list = []
        right_list = []


        for numbers in alist:
            print("The current number is:",numbers)
            if numbers < pivot:
                left_list.append(numbers)
                print("left list",left_list)
            else:
                right_list.append(numbers)
                print("right of pivot list:",right_list)

        return quick_sort(left_list) + [pivot] + quick_sort(right_list)

num = [7,11,2,1,8,6,3,5,4,12]
print("original list ",num)
print(quick_sort(num))