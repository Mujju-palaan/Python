
nums = (2, 1, 2, 3, 4, 6)
def count_evens(nums):
    evenlist = []
    for evens in nums:
        if (evens % 2 == 0 ) :
            evenlist.append(evens) 
    print(len(evenlist))
count_evens(nums)
