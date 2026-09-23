"""
Tests for LeetCode 162: Find Peak Element
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_peak_element", src_path / "binary_search" / "find_peak_element.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindPeakElement:
    """Test cases for Find Peak Element problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findPeakElement([1, 2, 3, 1]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
