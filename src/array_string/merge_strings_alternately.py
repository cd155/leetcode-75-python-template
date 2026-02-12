"""
LeetCode 1768: Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding 
letters in alternating order, starting with word1. If a string is longer 
than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately.
        
        Args:
            word1: First string
            word2: Second string
            
        Returns:
            Merged string with alternating characters
        """
        result = []
        i = 0
        
        # Add characters alternately
        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        # Add remaining characters from word1
        while i < len(word1):
            result.append(word1[i])
            i += 1
        
        # Add remaining characters from word2
        while i < len(word2):
            result.append(word2[i])
            i += 1
        
        return ''.join(result)
