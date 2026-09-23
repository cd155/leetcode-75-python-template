"""
Tests for LeetCode 443: String Compression
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("string_compression", src_path / "array_string" / "string_compression.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestStringCompression:
    """Test cases for String Compression problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        assert self.solution.compress(chars) == 6
        assert chars[:6] == ["a", "2", "b", "2", "c", "3"]

    def test_example_2(self):
        """Test case from example 2"""
        chars = ["a"]
        assert self.solution.compress(chars) == 1
        assert chars[:1] == ["a"]

    def test_example_3(self):
        """Test case from example 3"""
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        assert self.solution.compress(chars) == 4
        assert chars[:4] == ["a", "b", "1", "2"]
