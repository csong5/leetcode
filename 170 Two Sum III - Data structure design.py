170 - Two Sum III - Data structure design

*Design and implement a TwoSum class. It should support the following operations: add and find.*
*add - Add the number to an internal data structure.*
*find - Find if there exists any pair of numbers which sum is equal to the value.*
For example,
	add(1); add(3); add(5);
	find(4) -> true
	find(7) -> false
```
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
		self.dic = {}
				
    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
		if not self.dic.get(number):
			self.dic[number] = 1
		else:
			self.dic[number] += 1
				
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
		for num in self.dic:
			if value - num in self.dic and (sef.dic[num] > 1 or value - num != num):
				return True
		return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
