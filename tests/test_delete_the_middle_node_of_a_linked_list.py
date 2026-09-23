"""
Tests for LeetCode 2095: Delete the Middle Node of a Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("delete_the_middle_node_of_a_linked_list", src_path / "linked_list" / "delete_the_middle_node_of_a_linked_list.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


class TestDeleteTheMiddleNodeOfALinkedList:
    """Test cases for Delete the Middle Node of a Linked List problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
        result = self.solution.deleteMiddle(head)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        assert values == [1, 3, 4, 1, 2, 6]

    def test_example_2(self):
        """Test case from example 2"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = self.solution.deleteMiddle(head)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        assert values == [1, 2, 4]

    def test_example_3(self):
        """Test case from example 3"""
        head = ListNode(2, ListNode(1))
        result = self.solution.deleteMiddle(head)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        assert values == [2]
