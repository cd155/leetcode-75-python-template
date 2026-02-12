"""
Tests for LeetCode 2095: Delete the Middle Node of a Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from linked_list.delete_the_middle_node_of_a_linked_list import Solution
from linked_list.delete_the_middle_node_of_a_linked_list import ListNode

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



class TestDeleteTheMiddleNodeOfALinkedList:
    """Test cases for LeetCode 2095: Delete the Middle Node of a Linked List"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_linked([1,3,4,7,1,2,6])
        result = self.solution.deleteMiddle(head)
        assert linked_to_list(result) == [1,3,4,1,2,6]

    def test_example_2(self):
        head = list_to_linked([1,2,3,4])
        result = self.solution.deleteMiddle(head)
        assert linked_to_list(result) == [1,2,4]

    def test_example_3(self):
        head = list_to_linked([2,1])
        result = self.solution.deleteMiddle(head)
        assert linked_to_list(result) == [2]

