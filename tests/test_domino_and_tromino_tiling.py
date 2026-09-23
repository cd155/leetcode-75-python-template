"""
Tests for LeetCode 790: Domino and Tromino Tiling
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("domino_and_tromino_tiling", src_path / "dp_1d" / "domino_and_tromino_tiling.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestDominoAndTrominoTiling:
    """Test cases for Domino and Tromino Tiling problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.numTilings(3) == 5

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.numTilings(1) == 1
