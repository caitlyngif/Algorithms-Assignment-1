"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if (x <= 1):
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    
    pass

def longest_run(mylist, key):
    current = 0
    longest = 0
    for i in range(len(mylist)):
        if(mylist[i] == key):
            current += 1
            if(current > longest):
                longest = current
        else:
            current = 0
    return longest

    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    n = len(mylist)

    if(n == 0):
        return Result(0, 0, 0, False)
    
    if(n == 1):
        if(mylist[0] == key):
            return Result (1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    
    mid = n // 2
    leftHalf = mylist[:mid]
    rightHalf = mylist[mid:]

    L = longest_run_recursive(leftHalf, key)
    R = longest_run_recursive(rightHalf, key)

    if(L.left_size == mid): # entire left half is a run of the key
        left_size = L.left_size + R.left_size
    else:
        left_size = L.left_size
    
    if(R.right_size == n - mid): # entire right half is a run of the key
        right_size = R.right_size + L.right_size
    else:
        right_size = R.right_size

    if(L.longest_size >= R.longest_size):
        longest = L.longest_size
    else:
        longest = R.longest_size
    
    if(L.right_size + R.left_size > longest):
        longest_size = L.right_size + R.left_size
    else:
        longest_size = longest
    
    return Result(left_size, right_size, longest_size, False)

    pass



