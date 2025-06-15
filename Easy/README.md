Problem #1 (Two Sum | Array, Hash Table)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3
Input: nums = [3,3], target = 6
Output: [0,1]

Constraint
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.


SOLUTIONS
HashMap
We create a HashMap that contains <Integer, Integer>, the key is the element from the array and value is its index,

We create a for loop to iterate through each element of the array. Each element is mapped to the HashMap,

An operation is perforned target - element that is stored to variable pair, which represents the number needed to be added to the current element to get the target. The HashMap is checked if it already contains the number pair. If it is, then return the index of the current element and the index of pair.