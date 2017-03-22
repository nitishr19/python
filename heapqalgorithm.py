import heapq
from collections import Counter
# to print the max 3 values from list
grades = [1000,2682,600,22,44,66,88,99,101,209,4004,444]
g= sorted(grades,reverse=True)
# using normal sort method
print(g)
print(g[:3])

# using  heapq method
# (3,grades)---> lagest upto 3 nos from grades list
print(heapq.nlargest(3,grades))

# for dynamic dataset such as dict

stocks = [
    {'cp':'GOOG','values':520.40},
    {'cp':'YHO','values':300},
    {'cp':'FKT','values':120.66},
    {'cp':'AAPL','values':29.0},
    {'cp':'AZN','values':99.9}
]
print(heapq.nsmallest(2,stocks,key =lambda stock:stock['values']))

# find the feequency of words in my text

text = "Instead of using the .txt file from above (or instead of, if you want the challenge), " \
       "take this .txt file, and count how many of each “category” of each image there are. " \
       "This text file is actually a list of files corresponding to the SUN database scene recognition database, " \
       "and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file," \
       " it will be clear which part represents the scene category. To do this, " \
       "you’re going to have to remember a bit about string parsing in Python 3. " \
       "I talked a little bit about it in this post."
#TODO other methods of counter
words = text.split()
counter = Counter(words)
top_four = counter.most_common(4)
ss = counter.elements()
print(top_four)