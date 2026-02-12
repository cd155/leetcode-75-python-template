"""
Tests for LeetCode 901: Online Stock Span
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from monotonic_stack.online_stock_span import Solution


class TestOnlineStockSpan:
    """Test cases for LeetCode 901: Online Stock Span"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        obj = Solution()
        assert obj.next(100) == 1
        assert obj.next(80) == 1
        assert obj.next(60) == 1
        assert obj.next(70) == 2
        assert obj.next(60) == 1
        assert obj.next(75) == 4
        assert obj.next(85) == 6

