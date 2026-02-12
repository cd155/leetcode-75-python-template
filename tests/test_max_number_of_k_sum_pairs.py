"""
Tests for LeetCode 1679: Max Number of K-Sum Pairs
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from two_pointers.max_number_of_k_sum_pairs import Solution


class TestMaxNumberOfKSumPairs:
    """Test cases for LeetCode 1679: Max Number of K-Sum Pairs"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.maxOperations([1,2,3,4], 5) == 2

    def test_example_2(self):
        assert self.solution.maxOperations([3,1,3,4,3], 6) == 1

