"""
Tests for LeetCode 1318: Minimum Flips to Make a OR b Equal to c
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("minimum_flips_to_make_a_or_b_equal_to_c", src_path / "bit_manipulation" / "minimum_flips_to_make_a_or_b_equal_to_c.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMinimumFlipsToMakeAOrBEqualToC:
    """Test cases for Minimum Flips to Make a OR b Equal to c problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minFlips(2, 6, 5) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minFlips(4, 2, 7) == 1

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.minFlips(1, 2, 3) == 0
