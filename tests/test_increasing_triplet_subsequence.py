"""
Tests for LeetCode 334: Increasing Triplet Subsequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array_string.increasing_triplet_subsequence import Solution


class TestIncreasingTripletSubsequence:
    """Test cases for LeetCode 334: Increasing Triplet Subsequence"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.increasingTriplet([1,2,3,4,5]) == True

    def test_example_2(self):
        assert self.solution.increasingTriplet([5,4,3,2,1]) == False

    def test_example_3(self):
        assert self.solution.increasingTriplet([2,1,5,0,4,6]) == True

