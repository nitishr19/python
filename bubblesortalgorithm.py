'''Bubble sort, sometimes referred to as sinking sort,
 is a simple sorting algorithm that repeatedly steps
through the list to be sorted, compares each pair of adjacent items
 and swaps them if they are in the wrong order'''
def bubblesort(alist):
    values = len(alist)-1 #since list starts from 0 say(0-9)
    for i in range(values): #or given as range(values,0,-1)--->say move in reverse order from 9 to 1
        print("i=",i)# range(0,9)
        for j in range(0,values-i): # or range(i)---> from(0 to 8)
            print("j=",j)# range(0,9-1(8))
            if(alist[j] > alist[j+1]):
                alist[j],alist[j+1] = alist[j+1],alist[j]
            print(alist)




alistar = [44,22,7,88,100,26,11,8,10,110]
#print(alistar)
bubblesort(alistar)
print(alistar)


