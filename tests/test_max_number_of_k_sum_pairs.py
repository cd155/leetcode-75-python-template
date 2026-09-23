"""
Tests for LeetCode 1679: Max Number of K-Sum Pairs
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("max_number_of_k_sum_pairs", src_path / "two_pointers" / "max_number_of_k_sum_pairs.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMaxNumberOfKSumPairs:
    """Test cases for Max Number of K-Sum Pairs problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxOperations([1, 2, 3, 4], 5) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxOperations([3, 1, 3, 4, 3], 6) == 1
