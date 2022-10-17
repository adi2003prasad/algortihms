'''
the pattern is 
1. move n-1 disk 
2. move nth disk 
3. shift the n-1 disk'''

'''
Arrange the disk from A to C in ascending order only where B is also a rod 
'''


def towerOfHanoi(n, rodsini, rodsfinal, rodsauxi):
    if(n == 0):
        return
    else:
        towerOfHanoi(n-1, rodsini, rodsauxi, rodsfinal)
        # towerOfHanoi(n, rodsini, rodsfinal, rodsauxi)
        print(
            f"the ring {str(n)} has been moved from {rodsini} to {rodsfinal}. ")
        towerOfHanoi(n-1, rodsauxi, rodsfinal, rodsini)


a = int(input("enter the n"))
towerOfHanoi(a, 'A', 'C', 'B')
