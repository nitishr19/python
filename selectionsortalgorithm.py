'''
The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
In order to do this, a selection sort looks for the largest value as it makes a pass and,
after completing the pass, places it in the proper location
'''
# the code finds the min element in the list and move to 0th position and next min in 1st pos and so on!!!
def sel_sort(alist):
    val = len(alist)
    for i in range(val):
        min_pos =i
        print("i=",i)
        print("minpos=",min_pos)
        for j in range(i+1,val):
            print("j=",j)
            if(alist[min_pos] > alist[j]):
                min_pos = j # do when the if condition satisfies or continue if loop
                print("min during if loop=",min_pos)
                print(alist)
        alist[i],alist[min_pos]=alist[min_pos],alist[i]#change the final min_pos with i(swap)
        print(alist)

datas = [44,32,80,76,14,6,12,100]
print("The original data:",datas)
sel_sort(datas)
print(datas)
