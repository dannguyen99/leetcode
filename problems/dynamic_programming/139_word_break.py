"""
LeetCode Problem: 139 - Word Break
Link: https://leetcode.com/problems/word-break/
Difficulty: Medium

Problem Description:
Given a string `s` and a dictionary `wordDict`, return true if `s` can be segmented
into a sequence of one or more dictionary words. Words can be reused.

Examples:
Example 1: s = "leetcode", wordDict = ["leet","code"] -> Output: true
Example 2: s = "applepenapple", wordDict = ["apple","pen"] -> Output: true
Example 3: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> Output: false

Constraints:
*   1 <= s.length <= 300
*   1 <= wordDict.length <= 1000
*   1 <= wordDict[i].length <= 20
*   s and wordDict[i] are lowercase English letters.
*   All words in wordDict are unique.
"""

import pytest
from typing import List


# Solution Class - Implement the logic here
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Dynamic Programming
        [Explain your DP state and recurrence relation here]
        dp[i] = True if s[0...i-1] can be segmented.

        Time Complexity: O(N * M * K) or O(N^3) in worst case if substring check is K.
                         More precisely O(N * sum(len(word) for word in dict)) or O(N*M) if M is avg word length.
                         With optimized substring checks and set lookups, often closer to O(N*M).
        Space Complexity: O(N) for the DP array. O(L) for wordDict set where L is total length of words.

        Args:
            s (str): The input string.
            wordDict (List[str]): The dictionary of words.

        Returns:
            bool: True if s can be segmented, False otherwise.
        """
        # Your solution here
        max_word_len = 20
        wordDict = set(wordDict)
        last_valid_index = 0
        valid_index = [0]
        for i in range(1, len(s) + 1):
            if i - last_valid_index > max_word_len:
                return False
            for j in range(len(valid_index) - 1, -1, -1):
                start_segment_idx = valid_index[j]
                # If the current segment s[start_segment_idx:i] would be too long
                if i - start_segment_idx > max_word_len:
                    break  # No need to check this or any earlier start_segment_idx

                if s[start_segment_idx:i] in wordDict:
                    valid_index.append(i)
                    last_valid_index = i
                    break
        return valid_index[-1] == len(s)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_s, input_wordDict, expected_output)
test_data = [
    ("leetcode", ["leet", "code"], True),  # Example 1
    ("applepenapple", ["apple", "pen"], True),  # Example 2
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),  # Example 3
    ("a", ["a"], True),
    ("ab", ["a", "b"], True),
    ("ab", ["a", "c"], False),
    ("cars", ["car", "ca", "rs"], True),
    ("aaaaaaa", ["aaaa", "aaa"], True),
    ("aaaaaaa", ["aaaa", "aa"], False),
    ("goalspecial", ["go", "goal", "goals", "special"], True),
    ("cbbb", ["cb", "b"], True),  # "cb" + "b"
    ("ccac", ["ca", "c"], True),  # "c" + "ca" + "c"
    (
        "bccdbacdbdacddabbaaaadababadad",
        [
            "cbc",
            "bcda",
            "adb",
            "ddca",
            "bad",
            "bbb",
            "dad",
            "dac",
            "ba",
            "aa",
            "bd",
            "abab",
            "bb",
            "dbda",
            "cb",
            "caccc",
            "d",
            "dd",
            "aadb",
            "cc",
            "b",
            "bcc",
            "bcd",
            "cd",
            "cbca",
            "bbd",
            "ddd",
            "dabb",
            "ab",
            "acd",
            "a",
            "bbcc",
            "cdcbd",
            "cada",
            "dbca",
            "ac",
            "abacd",
            "cba",
            "cdb",
            "dbac",
            "aada",
            "cdcda",
            "cdc",
            "dbc",
            "dbcb",
            "bdb",
            "ddbdd",
            "cadaa",
            "ddbc",
            "babb",
        ],
        True,
    ),
]


@pytest.mark.parametrize("s_input, wordDict_input, expected", test_data)
def test_solution(s_input, wordDict_input, expected):
    solution = Solution()
    result = solution.wordBreak(s_input, wordDict_input)
    assert result == expected
