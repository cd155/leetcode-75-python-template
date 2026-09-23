"""
Tests for LeetCode 2336: Smallest Number in Infinite Set
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("smallest_number_in_infinite_set", src_path / "heap_priority_queue" / "smallest_number_in_infinite_set.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
SmallestInfiniteSet = module.SmallestInfiniteSet


class TestSmallestNumberInInfiniteSet:
    """Test cases for Smallest Number in Infinite Set problem"""

    def test_example_1(self):
        """Test case from example 1"""
        smallestInfiniteSet = SmallestInfiniteSet()
        smallestInfiniteSet.addBack(2)
        assert smallestInfiniteSet.popSmallest() == 1
        assert smallestInfiniteSet.popSmallest() == 2
        assert smallestInfiniteSet.popSmallest() == 3
        smallestInfiniteSet.addBack(1)
        assert smallestInfiniteSet.popSmallest() == 1
        assert smallestInfiniteSet.popSmallest() == 4
        assert smallestInfiniteSet.popSmallest() == 5
