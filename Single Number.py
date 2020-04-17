
'''
function returns the only unique number present in the nums list
'''

def singleNumber(self, nums: List[int]) -> int:
    num = nums[0]
    for i in nums[1:]:
         num = num^i
    return num
        
