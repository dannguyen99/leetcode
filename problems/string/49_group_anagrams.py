"""
LeetCode Problem: 49 - Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium

Problem Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
* 1 <= strs.length <= 10^4
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.
"""
import pytest
from typing import List
from collections import defaultdict  # Might be useful

# Solution Class - Implement the logic here
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.

        Approach:
        [Explain your approach here - focusing on the hash map key]

        Args:
            strs: A list of strings.

        Returns:
            List[List[str]]: A list where each inner list contains strings
                             that are anagrams of each other.
        """
        # --- Implement your solution here ---
        result = {}
        for str in strs:
            str_key = [0] * 26
            # build the str_key for the string
            for char in str:
                str_key[ord(char) - ord("a")] += 1
            str_key = tuple(str_key)
            if str_key in result:
                result[str_key].append(str)
            else:
                result[str_key] = [str]
        return [r for r in result.values()]


# --- Test Section ---

# Helper function to sort lists within lists for comparison, as order doesn't matter
def sort_list_of_lists(list_of_lists):
    for inner_list in list_of_lists:
        inner_list.sort()  # Sort strings within each group
    # Sort the outer list based on the first element of each sorted inner list
    list_of_lists.sort(key=lambda x: x[0] if x else "")
    return list_of_lists


# Define test cases as a list of tuples
# Format: (input_strs, expected_grouped_anagrams)
test_data = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
    (["abc", "bca", "bac", "xyz", "zyx"], [["abc", "bac", "bca"], ["xyz", "zyx"]]),
    (["listen", "silent", "enlist"], [["enlist", "listen", "silent"]]),
    (["", ""], [["", ""]]),  # Multiple empty strings
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("strs, expected", test_data)
def test_solution(strs, expected):
    solution = Solution()
    result = solution.groupAnagrams(strs)
    # Sort both lists for comparison as group order and order within groups doesn't matter
    sorted_result = sort_list_of_lists(result)
    sorted_expected = sort_list_of_lists(expected)
    assert sorted_result == sorted_expected


# You can add more specific test functions if needed
