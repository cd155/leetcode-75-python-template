"""
Tests for LeetCode 2462: Total Cost to Hire K Workers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("total_cost_to_hire_k_workers", src_path / "heap_priority_queue" / "total_cost_to_hire_k_workers.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestTotalCostToHireKWorkers:
    """Test cases for Total Cost to Hire K Workers problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4) == 11

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.totalCost([1, 2, 4, 1], 3, 3) == 4
