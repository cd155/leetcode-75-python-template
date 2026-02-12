"""
Tests for LeetCode 2130: Maximum Twin Sum of a Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from linked_list.maximum_twin_sum_of_a_linked_list import Solution
from linked_list.maximum_twin_sum_of_a_linked_list import ListNode

def list_to_linked(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



class TestMaximumTwinSumOfALinkedList:
    """Test cases for LeetCode 2130: Maximum Twin Sum of a Linked List"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked([5,4,2,1])
        assert self.solution.pairSum(head) == 6

    def test_example_2(self):
        head = list_to_linked([4,2,2,3])
        assert self.solution.pairSum(head) == 7

    def test_example_3(self):
        head = list_to_linked([1,100000])
        assert self.solution.pairSum(head) == 100001

