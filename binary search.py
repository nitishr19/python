# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean. THIS TIME, WITH THE EXTRA: USING BINARY SEARCH.

alist = [1,4,6,8,11,100,222,654,900]
def found(alist,num):
    if num in alist:
        return True
    else:
        return False

print(found(alist,10))
print(found(alist,1))
print(found(alist,109))
print(found(alist,103))
print(found(alist,4))
print(found(alist,100))
# Binary search using slicing through middle elements
def binary_search(my_list,num):
    while True:

        middle = len(my_list) // 2 # middle is 4 lists starts from 0 so 5th element

        if my_list[middle] == num:# if middle ele of list is == num
            return True
        elif num < my_list[middle]:# num is < than 5th ele
            my_list = my_list[:middle]# update lists upto middle
        elif num > my_list[middle]:# if num > 5th ele (middle element in lists here in this example)
            my_list = my_list[middle:]# update lists from middle to end
        if len(my_list) == 1:# if len(lists) ==1 return false
            return False


print("binary search results")
# print(len(alist))

print(binary_search(alist,11))
print(binary_search(alist,0))
print(binary_search(alist,100))
print(binary_search(alist,110))
print(binary_search(alist,200))
print(binary_search(alist,900))


