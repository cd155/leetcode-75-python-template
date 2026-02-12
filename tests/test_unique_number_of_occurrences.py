"""
Tests for LeetCode 1207: Unique Number of Occurrences
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from hash_map.unique_number_of_occurrences import Solution


class TestUniqueNumberOfOccurrences:
    """Test cases for LeetCode 1207: Unique Number of Occurrences"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.uniqueOccurrences([1,2,2,1,1,3]) == True

    def test_example_2(self):
        assert self.solution.uniqueOccurrences([1,2]) == False

    def test_example_3(self):
        assert self.solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True

