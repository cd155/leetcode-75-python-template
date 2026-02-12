"""
Tests for LeetCode 2390: Removing Stars From a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from stack.removing_stars_from_a_string import Solution


class TestRemovingStarsFromAString:
    """Test cases for LeetCode 2390: Removing Stars From a String"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.removeStars("leet**od*e") == "lecoe"

    def test_example_2(self):
        assert self.solution.removeStars("erase*****") == ""

