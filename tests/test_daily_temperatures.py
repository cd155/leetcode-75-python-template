"""
Tests for LeetCode 739: Daily Temperatures
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from monotonic_stack.daily_temperatures import Solution


class TestDailyTemperatures:
    """Test cases for LeetCode 739: Daily Temperatures"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

    def test_example_2(self):
        assert self.solution.dailyTemperatures([30,40,50,60]) == [1,1,1,0]

    def test_example_3(self):
        assert self.solution.dailyTemperatures([30,60,90]) == [1,1,0]

