"""
Tests for LeetCode 328: Odd Even Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from linked_list.odd_even_linked_list import Solution
from linked_list.odd_even_linked_list import ListNode

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



class TestOddEvenLinkedList:
    """Test cases for LeetCode 328: Odd Even Linked List"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked([1,2,3,4,5])
        result = self.solution.oddEvenList(head)
        assert linked_to_list(result) == [1,3,5,2,4]

    def test_example_2(self):
        head = list_to_linked([2,1,3,5,6,4,7])
        result = self.solution.oddEvenList(head)
        assert linked_to_list(result) == [2,3,6,7,1,5,4]

