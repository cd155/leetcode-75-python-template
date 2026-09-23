"""
Tests for LeetCode 452: Minimum Number of Arrows to Burst Balloons
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("minimum_number_of_arrows_to_burst_balloons", src_path / "intervals" / "minimum_number_of_arrows_to_burst_balloons.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMinimumNumberOfArrowsToBurstBalloons:
    """Test cases for Minimum Number of Arrows to Burst Balloons problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
