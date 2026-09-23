"""
Tests for LeetCode 1431: Kids With the Greatest Number of Candies
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("kids_with_the_greatest_number_of_candies", src_path / "array_string" / "kids_with_the_greatest_number_of_candies.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestKidsWithTheGreatestNumberOfCandies:
    """Test cases for Kids With the Greatest Number of Candies problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.kidsWithCandies([12, 1, 12], 10) == [True, False, True]
