'''
As the book states,
for a list of about ten million elements, the search times for where an item is found around the middle, are these:
Binary Search: 0.02
Linear Search: 105

list.sort() takes about 3500 for a list of ten million, which means that in order to profit from sorting and binary searching, we will need

3500/105 = 33.333(3)

We will need to search a list of ten million items 34 times to profit from sorting it and binary searching.
'''