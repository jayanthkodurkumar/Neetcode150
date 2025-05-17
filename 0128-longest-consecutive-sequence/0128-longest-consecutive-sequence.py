#  NOTES:

# 1. The original sliding window give O(NlogN).
# 2. So what we can do is we shall use a set.
# 3. The rule is that in a LCS here the difference between each element is 1 and if two numbers are same, we count it 
# as 1 only [0,0,1] = 2 elements.
# 4. Thus we can use a set since only unique values are needed for the count as above.
# 5. We loop through the set. For an set element to be the starting point of a sequence, it should not have any prev
# element in the set (i.e) element - 1 should not be there in set.
# 6. So when we encounter an element which is starting point, we check for lcs condition and update current sequence count.
# 7. If the element is not a starting point, just skip the iteration.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        lcs = 0
        if n == 0:
            return lcs

        elements_set = set(nums)

        for element in elements_set:
            current_prev = element - 1
            if current_prev not in elements_set:
                current_longest = 1
                current_next = element + 1
                while current_next in elements_set:
                    current_longest += 1
                    current_next += 1
                lcs = max(current_longest, lcs)
        return lcs
