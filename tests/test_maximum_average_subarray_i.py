"""
Tests for LeetCode 643: Maximum Average Subarray I
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_average_subarray_i", src_path / "sliding_window" / "maximum_average_subarray_i.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMaximumAverageSubarrayI:
    """Test cases for Maximum Average Subarray I problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findMaxAverage([5], 1) == 5.0
