"""
Tests for LeetCode 649: Dota2 Senate
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from queue.dota2_senate import Solution


class TestDota2Senate:
    """Test cases for LeetCode 649: Dota2 Senate"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.predictPartyVictory("RD") == "Radiant"

    def test_example_2(self):
        assert self.solution.predictPartyVictory("RDD") == "Dire"

