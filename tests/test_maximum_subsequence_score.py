"""
Tests for LeetCode 2542: Maximum Subsequence Score
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.maximum_subsequence_score import Solution


class TestMaximumSubsequenceScore:
    """Test cases for LeetCode 2542: Maximum Subsequence Score"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.maxScore([1,3,3,2], [2,1,3,4], 3) == 12

    def test_example_2(self):
        assert self.solution.maxScore([4,2,3,1,1], [7,5,10,9,6], 1) == 30

