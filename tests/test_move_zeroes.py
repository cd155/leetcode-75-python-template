"""
Tests for LeetCode 283: Move Zeroes
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("move_zeroes", src_path / "two_pointers" / "move_zeroes.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMoveZeroes:
    """Test cases for Move Zeroes problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_example_2(self):
        """Test case from example 2"""
        nums = [0]
        self.solution.moveZeroes(nums)
        assert nums == [0]
