"""
Tests for LeetCode 2542: Maximum Subsequence Score
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_subsequence_score", src_path / "heap_priority_queue" / "maximum_subsequence_score.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMaximumSubsequenceScore:
    """Test cases for Maximum Subsequence Score problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3) == 12

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1) == 30
