class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
				# we will focus on an non trivial example
        # example: [2,9,9,3,7,9] -> 2 + 9 + 9 or (9 + 3 + 9)
        # i.e [(2), 9, (9), 3, 7, (9)] where (int)
        # represents the house robbed
        
        # we can already noticed that the houses we
        # need to rob are not necessarily separated
        # by ONE house (there is 2 houses between (9) and (9))
        # so it seems that to solve this problem
        # we will need dynamic programming!
        
        # the idea with dynamic programming is to
        # assume we are in a certain position and that
        # we have our result up to this position and to
        # try to come up with what we should do next
        
        # so let's assume we are on the second 9:
        # [2, 9, (9), 3, 7, 9] and that we already have
        # the maximum number we can rob from [2, 9, 9] (here 11)
        
        # the questionS are: what is the maximum number for
        # - [2, 9, 9, 3]
        # - [2, 9, 9, 3, 7]
        # - [2, 9, 9, 2, 7, 9]
        
        # for [2, 9, 9, 3]:
        # maximum nb on [2, 9, 9] is 11: [2, 9]
        # but maximum nb on [2, 9, 9, 3] is 12: [9, 3]
        # but we can't obtain 12 if we only have 11!!
        # so not only we need: the maximum nb on [2, 9, 9]
        # but we also need:    the maximum nb on [2, 9, 9] that DON'T take the last number
        
        # put it differently we need both:
        # rob([2,9,9]) and rob([2,9])
        
        # now, as 11 is obtained using the last number of [2,9,9]
        # the next best number is either 11 either max([2, 9]) + last_number
        # i.e: max(11, rob([2,9]) + 3)
        # using variables we can write:
        # - max_without_last = 9 (max of [2,9])
        # - max_with_last = 11 (max of [2,9,9])
        # temp = max_without_last
        # max_without_last = max_with_last # we modify the val of max_without_last here so we need to have a temp variable
        # if temp + last_number > max_with_last:
        #     max_with_last = temp + last_number
        
        # for [2, 9, 9, 3, 7]
        # according to the last 3 lines from previous example
        # we have, up until [2, 9, 9, 3]:
        # max_with_last = 9 + 3 = 12
        # max_without_last = 2 + 9 = 11
        # so if we can use the same rule we will have:
        # is 11 + 7 > 12 (max_without_last + last_number > max_with_last) ? YES, so:
        # max_without_last = 12
        # max_with_last = 11 + 7 = 18
        # we check that the max(max_without_last, max_with_last) = 18 is the correct answer!
        
        # for [2, 9, 9, 3, 7, 9]
        # up until [2, 9, 9, 3, 7] we have
        # max_without_last = 12
        # max_with_last = 18
        # and using the same update we have:
        # max_without_last = 18
        # max_with_last = 12 + 9 = 21 (because 12 + 9 > 18)
        # we check that max(max_without_last, max_with_last) = 21 is the correct answer!
        
        # so in the end we have our algorithm! we just
        # need to handle base cases!
        if len(nums) < 3:
            return max(nums, default=0)
        
        max_without_last, max_with_last = nums[0], max(nums[:2])
        for n in nums[2:]:
            # temp = max_without_last
            # max_without_last = max_with_last
            # max_with_last = max(max_with_last, temp + n)
            max_without_last, max_with_last = max_with_last, max(max_with_last, max_without_last + n)
        
        return max(max_without_last, max_with_last)
        
        
        # Notes:
        # we replaced
        # if temp + last_number > max_with_last:
        #     max_with_last = temp + last_number
        # with (equivalent)
        # max_with_last = max(max_with_last, temp + last_number)
        # we can even reduce the algoithm because in python
        # a, b = b, a
        # is the same as:
        # temp = a
        # a = b
        # b = temp
