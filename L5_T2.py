import collections


nums = collections.namedtuple('nums', ['a', 'b'])

nums = nums(input(), input())

c = hex(int(nums[0], 16) + int(nums[1], 16))
print(c)