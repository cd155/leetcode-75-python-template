"""
Tests for LeetCode 1207: Unique Number of Occurrences
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("unique_number_of_occurrences", src_path / "hash_map_set" / "unique_number_of_occurrences.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestUniqueNumberOfOccurrences:
    """Test cases for Unique Number of Occurrences problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.uniqueOccurrences([1, 2]) == False

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
