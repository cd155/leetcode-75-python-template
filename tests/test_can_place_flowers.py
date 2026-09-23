"""
Tests for LeetCode 605: Can Place Flowers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("can_place_flowers", src_path / "array_string" / "can_place_flowers.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCanPlaceFlowers:
    """Test cases for Can Place Flowers problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
