"""
Tests for LeetCode 875: Koko Eating Bananas
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_search.koko_eating_bananas import Solution


class TestKokoEatingBananas:
    """Test cases for LeetCode 875: Koko Eating Bananas"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.minEatingSpeed([3,6,7,11], 8) == 4

    def test_example_2(self):
        assert self.solution.minEatingSpeed([30,11,23,4,20], 5) == 30

    def test_example_3(self):
        assert self.solution.minEatingSpeed([30,11,23,4,20], 6) == 23

