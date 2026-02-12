"""
Tests for LeetCode 2336: Smallest Number in Infinite Set
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.smallest_number_in_infinite_set import Solution


class TestSmallestNumberInInfiniteSet:
    """Test cases for LeetCode 2336: Smallest Number in Infinite Set"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        obj = Solution()
        obj.addBack(2)
        assert obj.popSmallest() == 1
        assert obj.popSmallest() == 2
        assert obj.popSmallest() == 3
        obj.addBack(1)
        assert obj.popSmallest() == 1
        assert obj.popSmallest() == 4

