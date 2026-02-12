"""
Tests for LeetCode 435: Non-overlapping Intervals
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from intervals.non_overlapping_intervals import Solution


class TestNonOverlappingIntervals:
    """Test cases for LeetCode 435: Non-overlapping Intervals"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1

    def test_example_2(self):
        assert self.solution.eraseOverlapIntervals([[1,2],[2,3]]) == 0

    def test_example_3(self):
        assert self.solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2

