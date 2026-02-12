"""
Tests for LeetCode 2300: Successful Pairs of Spells and Potions
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary_search.successful_pairs_of_spells_and_potions import Solution


class TestSuccessfulPairsOfSpellsAndPotions:
    """Test cases for LeetCode 2300: Successful Pairs of Spells and Potions"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.successfulPairs([5,1,3], [1,2,3,4,5], 7) == [4,0,3]

    def test_example_2(self):
        assert self.solution.successfulPairs([3,1,2], [8,5,8], 16) == [2,0,2]

