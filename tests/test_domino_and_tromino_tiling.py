"""
Tests for LeetCode 790: Domino and Tromino Tiling
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_1d.domino_and_tromino_tiling import Solution


class TestDominoAndTrominoTiling:
    """Test cases for LeetCode 790: Domino and Tromino Tiling"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.numTilings(3) == 5

    def test_example_2(self):
        assert self.solution.numTilings(1) == 1

