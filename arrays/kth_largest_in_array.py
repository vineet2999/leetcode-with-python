"""question:
Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""


# Solution:

def k_th_largest_element(num: list[int], k: int) -> int:
    # sort the list in reverse order, return the kth element in the list
    if not num:
        return 0

    num.sort(reverse=True)
    return num[k - 1]


if __name__ == '__main__':
    value = k_th_largest_element(num=[78, 678, 999, 567, 3, 2, 1, 4, 3, 2], k=3)
    print(value)
