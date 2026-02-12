"""
Tests for LeetCode 735: Asteroid Collision
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from stack.asteroid_collision import Solution


class TestAsteroidCollision:
    """Test cases for LeetCode 735: Asteroid Collision"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.asteroidCollision([5,10,-5]) == [5,10]

    def test_example_2(self):
        assert self.solution.asteroidCollision([8,-8]) == []

    def test_example_3(self):
        assert self.solution.asteroidCollision([10,2,-5]) == [10]

