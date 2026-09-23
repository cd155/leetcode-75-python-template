"""
Tests for LeetCode 2215: Find the Difference of Two Arrays
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_the_difference_of_two_arrays", src_path / "hash_map_set" / "find_the_difference_of_two_arrays.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindTheDifferenceOfTwoArrays:
    """Test cases for Find the Difference of Two Arrays problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.findDifference([1, 2, 3], [2, 4, 6])
        assert [sorted(result[0]), sorted(result[1])] == [[1, 3], [4, 6]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
        assert [sorted(result[0]), sorted(result[1])] == [[3], []]
