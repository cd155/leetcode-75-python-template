"""
Tests for LeetCode 208: Implement Trie (Prefix Tree)
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from trie.implement_trie_prefix_tree import Solution


class TestImplementTriePrefixTree:
    """Test cases for LeetCode 208: Implement Trie (Prefix Tree)"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        trie = Solution()
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        trie.insert("app")
        assert trie.search("app") == True

