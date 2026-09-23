"""
Tests for LeetCode 2390: Removing Stars From a String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("removing_stars_from_a_string", src_path / "stack" / "removing_stars_from_a_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRemovingStarsFromAString:
    """Test cases for Removing Stars From a String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.removeStars("leet**cod*e") == "lecoe"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.removeStars("erase*****") == ""
