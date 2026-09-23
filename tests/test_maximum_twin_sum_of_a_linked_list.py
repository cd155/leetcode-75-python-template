"""
Tests for LeetCode 2130: Maximum Twin Sum of a Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_twin_sum_of_a_linked_list", src_path / "linked_list" / "maximum_twin_sum_of_a_linked_list.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestMaximumTwinSumOfALinkedList:
    """Test cases for Maximum Twin Sum of a Linked List problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
        assert self.solution.pairSum(head) == 6

    def test_example_2(self):
        """Test case from example 2"""
        head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
        assert self.solution.pairSum(head) == 7

    def test_example_3(self):
        """Test case from example 3"""
        head = ListNode(1, ListNode(100000))
        assert self.solution.pairSum(head) == 100001
