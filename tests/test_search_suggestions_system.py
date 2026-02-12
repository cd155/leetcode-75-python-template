"""
Tests for LeetCode 1268: Search Suggestions System
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from trie.search_suggestions_system import Solution


class TestSearchSuggestionsSystem:
    """Test cases for LeetCode 1268: Search Suggestions System"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.suggestedProducts(
            ["mobile","mouse","moneypot","monitor","mousepad"], "mouse"
        ) == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

