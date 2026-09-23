"""
Tests for LeetCode 1732: Find the Highest Altitude
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_the_highest_altitude", src_path / "prefix_sum" / "find_the_highest_altitude.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindTheHighestAltitude:
    """Test cases for Find the Highest Altitude problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.largestAltitude([-5, 1, 5, 0, -7]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
