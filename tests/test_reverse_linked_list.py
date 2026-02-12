"""
Tests for LeetCode 206: Reverse Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from linked_list.reverse_linked_list import Solution
from linked_list.reverse_linked_list import ListNode

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



class TestReverseLinkedList:
    """Test cases for LeetCode 206: Reverse Linked List"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked([1,2,3,4,5])
        result = self.solution.reverseList(head)
        assert linked_to_list(result) == [5,4,3,2,1]

    def test_example_2(self):
        head = list_to_linked([1,2])
        result = self.solution.reverseList(head)
        assert linked_to_list(result) == [2,1]

    def test_example_3(self):
        result = self.solution.reverseList(None)
        assert linked_to_list(result) == []

