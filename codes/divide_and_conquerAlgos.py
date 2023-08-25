'''
divide and conquer algorithms are those algo's in which we divide the given input into multiple 
subsets and then find the answer to the subset and thus finding the answer for the entire set
'''

# 1. Binary search


def binary_search(set, startindex, endindex, searchelement):
    # binary search is only valid on sorted lists
    # print(set[startindex:endindex], startindex-endindex)
    if(abs(endindex-startindex) == 1):
        # print(set[startindex] == searchelement)
        if(set[startindex] == searchelement):
            print(startindex)
            return
            # return startindex

    middle = (startindex+endindex)//2
    if(set[middle] > searchelement):
        binary_search(set, startindex, middle, searchelement)
    else:
        binary_search(set, middle, endindex, searchelement)


# merge sort
'''
merge sort is an sorting algorithm based on above only where we divide the input into 
halfsubsets until we have 2 element list which we can compare
'''


def check(set):
    for x in range(len(set)):
        if(x == 0):
            pass
        elif(set[x] > set[x-1]):
            continue
        else:
            return False
    return True


def merge_sort(set):
    print(len(set))
    if(len(set) == 1):
        print(set)
        return set
    # print(check(set), set)
    while(check(set) == False):
        mid = (len(set))//2
        # print(mid)
        newset = []
        # print(set[:mid])
        a = merge_sort(set[:mid])
        b = merge_sort(set[mid:])
        if(a[0] > b[0]):
            newset = b+a
        else:
            newset = a+b
        return newset


def test():
    # a = int(input("search element in binary search"))
    # set = [1, 3, 5, 7, 9, 12, 75, 125, 142, 643, 1563, 1777, 8999]
    # binary_search(set, 0, len(set)-1, a)
    # now for the mergessort
    set = [3, 1, 5, 7, 1, 6, 35, 12, 32, 22, 53, 13]
    print(merge_sort(set))
    # print(ab)


test()
